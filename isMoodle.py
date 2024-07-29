import requests
from bs4 import BeautifulSoup

def is_moodle_site(url):
    try:
        # Normalize URL to not end with a '/'
        normalized_url = url.rstrip('/')
        print(f"Normalized URL isMoodle: {normalized_url}")

        # Check if /login/forgot_password.php returns a 2xx status code
        forgot_password_url = f"{normalized_url}/login/forgot_password.php"
        response = requests.get(forgot_password_url, timeout=10)
        # print(f"DEBUG: status code: {response.status_code}")
        if response.status_code // 100 == 2:
            print(f"Response code is 2xx")
            return True

        # Fetch the start page content
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Check if the HTML content contains "M.yui"
            if "M.yui" in soup.text:
                print(f"Page has M.yui file")
                return True

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

    return False