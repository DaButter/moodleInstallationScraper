import requests
import time

from isMoodle import is_moodle_site
from getEleidiaResponseCode import get_page_data
from exportToCSV import write_results_to_csv

def is_base_url(url):
    parsed_url = requests.utils.urlparse(url)
    return parsed_url.path in ('', '/', '/?')

def search_bing(query, count, offset):
    subscription_key = 'your_api_key'
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    urls = []

    params = {"q": query, "count": count, "offset": offset}
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200:
        for item in data.get('webPages', {}).get('value', []):
            urls.append(item['url'])
        return urls
    elif response.status_code == 429:
        print(f"Error 429: Too Many Requests. You need to wait before making more requests.")
        return 429
    else:
        print(f"Error searching Bing: {response.status_code}")
        print(response.text)
        return response.status_code

def main():
    # query = "site:at moodle"
    # query = "site:ch moodle"
    # query = "site:li moodle"
    query = "site:de moodle edu"
    count = 10
    offset = 0
    urls = []
    total_results_needed = 100
    max_retries = 5
    initial_delay = 1
    max_delay = 60

    while offset < total_results_needed:
        # attempt = 0
        # delay = initial_delay
        # successful = False
        new_urls = search_bing(query, count, offset)
        # while attempt < max_retries:
        #     new_urls = search_bing(query, count, offset)
        #     if new_urls == 429:
        #         print(f"Retrying after {delay} seconds due to 429 error... (Attempt {attempt + 1} of {max_retries})")
        #         time.sleep(delay)
        #         delay = min(delay * 2, max_delay)  # Exponential backoff with cap
        #         attempt += 1
        #     elif new_urls is not None:
        #         successful = True
        #         break
        #     else:
        #         successful = True
        #         break

        # if not successful:
        #     print("Max retries reached or failed to get data. Exiting...")
        #     break

        base_urls = [url for url in new_urls if is_base_url(url)]
        if new_urls and new_urls != 429 and len(new_urls) > 0:
            if base_urls:
                urls.extend(base_urls)
                print(f"Found {len(base_urls)} new URLs with query {query} at offset {offset}")
                offset += count
            else:
                print(f"No new base URLs found with query {query} at offset {offset}")
                offset += count
        else:
            print(f"Nothing on offset {offset}")
            break

        if new_urls == 403:
            print("Epic fail 203")
            break
        # initial_delay = 1  # Reset initial delay after a successful request

    print(f"Total URLs collected: {len(urls)}")
    # for url in urls:
    #     print(url)

    # check if sites are moodle
    moodle_sites = []
    for url in urls:
        if is_moodle_site(url):
            moodle_sites.append(url)
    # for site in moodle_sites:
    #     print(site)

    # get /local/elediafile/version.php response code and page titles
    results = []
    for url in moodle_sites:
        results.append(get_page_data(url))

    # for debugresult in results:
    #     print(debugresult)

    # write to CSV file
    csv_file = 'moodle_status.csv'
    write_results_to_csv(results, csv_file)

    # finish
    print(f"Found {len(moodle_sites)} Moodle sites.")
    print("Good job bro! :)")


if __name__ == "__main__":
    main()
