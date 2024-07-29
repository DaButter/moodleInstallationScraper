## Task Overview
The task involved scraping Moodle installations from German-speaking countries (Germany, Switzerland, Austria, and Liechtenstein) to collect URLs of Moodle main pages. The project aimed to gather between 1200 and 2500 unique URLs and generate a CSV file containing specific details about each URL.

## Objectives
* Scrape Moodle installations from German-speaking domains.
* Filter URLs to retain only the main pages and not deeper path pages.
* Collect unique URLs and avoid duplicates.
* Generate a CSV file with the required format, including URL, status code, page title, and any email addresses found.

## Methodology
Using Bing Search API:

Queries like site:de moodle, site:ch moodle, site:at moodle, and site:li moodle were used.
The search results were filtered to include only main pages (e.g., https://example.com/).

## Filtering URLs:

Extracted URLs were parsed to remove duplicates, ensuring only the base URL was considered.
Query parameters and deeper paths were ignored to maintain only the main pages.
Extracting Page Details:

For each URL, an HTTP request was made to retrieve the HTML content.
BeautifulSoup was used to parse the HTML and extract the page title and any email addresses present.
A status code check was performed for a specific endpoint (/local/elediafile/version.php) to verify the URL's validity.

## Results
Total Unique URLs Collected: ~1500
The results were saved in a CSV file containing the following columns:
1. URL
2. Status Code
3. Page Title
4. Email Addresses (if any)