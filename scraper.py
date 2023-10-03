import requests
from bs4 import BeautifulSoup

# Paste the URL you want to scrape
url = 'https://cryptoart.io/artists'

# Set a User-Agent header to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Send an HTTP GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check the HTTP status code
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the title of the page
    title = soup.title.string
    print(f"Title: {title}")
    
    # Extract all the links on the page, excluding disallowed paths
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and not any(disallowed_path in href for disallowed_path in ['/search', '/api/health', '/cdn-cgi/']):
            print(f"Link: {href}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
