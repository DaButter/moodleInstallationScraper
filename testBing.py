import requests


def test_bing_search(subscription_key):
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": "Microsoft", "count": 1}

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        print("Test request successful!")
        data = response.json()
        print(data)
    else:
        print(f"Error searching Bing: {response.status_code}")
        print(response.text)  # Print the response body for more details


# Replace with your actual subscription key
# test_bing_search('your_api_key')
