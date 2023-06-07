
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

# Get the target URL from the user
user_url = str(input('[+] Enter Target URL To Scan: '))

# Initialize a queue to store URLs to be processed
urls = deque([user_url])

# Set to store scraped URLs and emails
scraped_urls = set()
emails = set()

count = 0
try:
    # Loop until there are URLs to process or a limit is reached
    while len(urls):
        count += 1
        if count == 100:
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        # Find email addresses in the response and add them to the set
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, features="lxml")

        # Find all anchor tags and extract their href attributes
        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            # Add new links to the queue if they haven't been processed before
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

# Print all the scraped email addresses
for mail in emails:
    print(mail)
