"""
Use woocommerce API Python library, to make API calls to list all (100+) products. 
Create a csv file that will have a list of products and their 'price' 
(there are 3 kinds of prices just use the field 'price'). So the csv will 
have two columns 'name' and 'price'.

*In order to create the above script there must be more than 100 products on the website.
This script "add_products" to a WooCommerce website.
"""

import os
import random
import string

# Setup the WooCommerce API Connection
from woocommerce import API

wcapi = API(
    url="http://frenchy-petes.local",
    consumer_key=os.environ.get('API_KEY'),
    consumer_secret=os.environ.get('API_SECRET'),
    version="wc/v3",
    timeout=60
)

# Variable to specify the number of products to be added
add_products = 120

# Create random names and prices for the products
for i in range(add_products):
    name = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
    price = str(round(random.uniform(0.0, 100.0), 2))

    # Variable to specify what product data needs to be created
    data = {
        'name': name,
        'regular_price': price,
    }
    
    # Variable to make a request to the WC API to create a new product with specified data
    rs_api = wcapi.post('products', data).json()
    
    # Print the current iteration of the loop to inform of where at in the creation process
    print(i)
