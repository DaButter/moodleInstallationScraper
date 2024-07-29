from isMoodle import is_moodle_site
from getEleidiaResponseCode import get_page_data
from exportToCSV import write_results_to_csv
import csv
from main import is_base_url
from urllib.parse import urlparse

# Function to extract the base URL
def get_base_url(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

def main():
    new_urls = []
    # Open the CSV file and read its contents
    with open('all_client_urls.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract the URL from the current row and append it to the new_urls list
            new_urls.append(row['URL'])

    # with open('./results_csv/ALL_moodle_status.csv', mode='r', encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         Extract the URL from the current row and append it to the new_urls list
    #         new_urls.append(row['URL'])

    # with open('./results_csv/AT_moodle_status.csv', mode='r', encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         # Extract the URL from the current row and append it to the new_urls list
    #         new_urls.append(row['URL'])

    # Print the URLs to verify
    print(new_urls)
    print(f"Total URLs: {len(new_urls)}")

    base_urls = [url for url in new_urls if is_base_url(url)]
    print(f"Total base URLs: {len(base_urls)}")

    # Use a set to filter out duplicate base URLs
    unique_base_urls = set(get_base_url(url) for url in base_urls)

    # Convert the set back to a list
    unique_urls = list(unique_base_urls)
    print(f"Unique URLs: {len(unique_urls)}")

    # check if sites are moodle
    moodle_sites = []
    for url in unique_urls:
        if is_moodle_site(url):
            moodle_sites.append(url)

    # get /local/elediafile/version.php response code and page titles
    results = []
    for url in moodle_sites:
        results.append(get_page_data(url))

    # write to CSV file
    csv_file = 'moodle_status.csv'
    write_results_to_csv(results, csv_file)

    # finish
    print(f"Found {len(moodle_sites)} Moodle sites.")
    print("Good job bro! :)")

if __name__ == "__main__":
    main()
