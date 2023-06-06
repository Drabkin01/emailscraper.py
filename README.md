# Email-Scraper.py

This repository contains a Python script for an email scraper. The script extracts email addresses from a given URL and its linked pages. It utilizes the BeautifulSoup library to parse HTML content and the requests library to make HTTP requests.

## Prerequisites

To run this script, you need to have Python installed on your system. Additionally, you should have the following libraries installed:

- BeautifulSoup (`bs4`)
- requests

You can install these libraries using `pip` with the following command:

```
pip install beautifulsoup4 requests
```

## Usage

To use the email scraper, follow these steps:

1. Clone the repository to your local machine or download the script directly.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Execute the script by running the following command:

   ```
   python email_scraper.py
   ```

4. You will be prompted to enter the target URL to scrape. Provide the complete URL, including the protocol (e.g., `http://` or `https://`).

5. The script will start scraping the specified URL and its linked pages. It will print any email addresses found during the process.

## Example

Here's an example usage of the script:

```
[+] Enter Target URL To Scrape: https://example.com

[1] Scraping https://example.com
[2] Scraping https://example.com/about
[3] Scraping https://example.com/contact

Found email addresses:
- john.doe@example.com
- jane.doe@example.com
```

In this example, we scrape the URL `https://example.com` and its linked pages. The script finds two email addresses (`john.doe@example.com` and `jane.doe@example.com`) during the process.

## Notes

- The script uses a breadth-first search algorithm to crawl through the web pages and extract email addresses.
- It keeps track of scraped URLs and avoids processing the same URL multiple times to prevent infinite loops.
- The script handles common exceptions, such as missing schema or connection errors when making requests.
- It uses regular expressions to extract email addresses from the HTML content.
- The extracted email addresses are printed at the end of the script.

Feel free to customize and modify the script according to your specific needs. Happy scraping!
