"""
Use woocommerce API Python library, to make API calls to list all (100+) products. 
Create a csv file that will have a list of products and their 'price' 
(there are 3 kinds of prices just use the field 'price'). So the csv will 
have two columns 'name' and 'price'.
"""

import os

# Setup the WooCommerce API Connection
from woocommerce import API

wcapi = API(
    url="http://frenchy-petes.local",
    consumer_key=os.environ.get('API_KEY'),
    consumer_secret=os.environ.get('API_SECRET'),
    version="wc/v3",
    timeout=60
)

# Empty list to store all of the products
all_products = []

# Set initial and per_page values to use pagination to retrieve all customers
page = 1
per_page = 50

 # Create a while loop to retrieve products per page, until all products are retrieved
while True:
    # Variable to call the WC API and retrieve products per_page
    products = wcapi.get("products", params={"page": page, "per_page": per_page}).json()
    
    # Increment the page number for the next iteration
    page += 1

    # Break the loop if the current page has no products
    if len(products) == 0:
        break

    # Extract all product names and prices and append them to the list
    for product in products:
        all_products.append((product['name'], product['price']))


# Prepare the CSV file by giving it a heading for the columns
filename = 'products.csv'
with open(filename, 'w') as file:
    file.write("Name, Price\n")

    # Extract product names and prices and print to the CSV file
    for product in all_products:
        file.writelines(f"{product[0]}, {product[1]}\n") # Products are accessed by index

print("A CSV file with all products has been created successfully!")
