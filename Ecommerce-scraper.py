from bs4 import BeautifulSoup
import urllib.request
import requests

# Step 1: Requesting the web page
page_url = 'https://blacktownmarkets.com.au/au/products-second-hand-items-for-sale'
response = requests.get(page_url)

# Step 2: checking if the request is successful
if response.status_code == 200:
    print("Website Permission Granted")

    #Step 3: Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    #Step 4 Find all product names and prices
    Names = soup.find_all('h5', class_="fw-600 mb-1")
    Prices = soup.find_all('h5', class_="fw-600 text-theme")

    #Step 5: Print names and prices if lengths match
    if len(Names) == len(Prices):
        for name, price in zip(Names, Prices):
            print(name.text.strip(), price.text.strip())  # .strip() removes extra spaces
    else:
        print("Mismatch in number of names and prices.")
else:
    print("Permission denied")







