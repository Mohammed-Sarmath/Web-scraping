from bs4 import BeautifulSoup
import urllib.request
import requests

# Request the web page
page_url = 'https://blacktownmarkets.com.au/au/products-second-hand-items-for-sale'
response = requests.get(page_url)

# Check if it's sucessfull(200 means successfull) 
if response.status_code == 200:
    print("Website Permission Granted")

    # Parse it
    soup = BeautifulSoup(response.text, 'html.parser')

    # All the product names and prices were in the 'h5' tag element with each class name, below code is appropriate
    Names = soup.find_all('h5', class_="fw-600 mb-1")
    Prices = soup.find_all('h5', class_="fw-600 text-theme")

    # If the length matches, below for loop prints all names and prices together at once with the help of 'zip'
    if len(Names) == len(Prices):
        for name, price in zip(Names, Prices):
            print(name.text.strip(), price.text.strip())  # .strip() removes extra spaces
    else:
        print("Mismatch in number of names and prices.")
else:
    print("Permission denied")







