import requests
from bs4 import BeautifulSoup
import re

# TODO: get emails from both version check and standard urls ???
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def get_version_php_status(url):
    try:
        normalized_url = url.rstrip('/')
        version_url = f"{normalized_url}/local/elediafile/version.php"
        print(f"Get PHP version: {version_url}")
        response = requests.get(version_url, timeout=10)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error fetching {version_url}: {e}")
        return ""

def get_page_data(url):
    result = {}
    result['URL'] = url
    result['STATUSCODE'] = get_version_php_status(url)
    try:
        response = requests.get(url, timeout=10)
        # response.encoding = response.apparent_encoding  # Ensure the correct encoding is used

        soup = BeautifulSoup(response.content, 'html.parser')

        # === GET PAGE TITLE ===
        page_title = soup.title.text if soup.title else None
        # Fallback to meta title
        if not page_title:
            meta_title = soup.find('meta', attrs={'name': 'title'})
            if meta_title and 'content' in meta_title.attrs:
                page_title = meta_title['content']
        # Fallback to Open Graph title
        if not page_title:
            og_title = soup.find('meta', property='og:title')
            if og_title and 'content' in og_title.attrs:
                page_title = og_title['content']
        # Fallback to the first H1 tag
        if not page_title:
            h1 = soup.find('h1')
            if h1:
                page_title = h1.text.strip()

        # If all else fails, set a default message
        result['PAGETITLE'] = page_title if page_title else "No Title Found"
        print(f"Got page title: {result['PAGETITLE']}")

        # === GET EMAIL ===
        emails = re.findall(email_pattern, soup.get_text())
        result['EMAIL'] = ', '.join(emails) if emails else ""

    except requests.RequestException as e:
        result['PAGETITLE'] = "LOHS Error fetching title"
        result['EMAIL'] = ""

    return result