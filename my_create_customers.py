"""
Write a script that will get a list of all users for the website. 
The script should output a csv file with list of all email addresses.

*In order to create the above script users for the website need to be created.
This script creates "number_of_users" for a WooCommerce website.
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

# Variable to specify the number of users to be created
number_of_users = 150

# Create random emails by creating a for loop to join a random string and email domain
for i in range(number_of_users):
    random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(11))
   
    # Variable to specify what customer data needs to be created
    data = {'email': f'{random_string}@email.com',
            'password': 'ljfdsjiojfosi'}

    # Variable to make a request to the WC API to create a new customer with specified data
    rs_api = wcapi.post('customers', data) # customers is the endpoint, data is the payload
    
    # Assert status code to confirm that customer was created or not
    assert rs_api.status_code == 201, f"Expected status code 201, but got {rs_api.status_code}. Response body {rs_api.json()} "
    rs_json = rs_api.json()
    email = rs_json['email']
    
    # Print the current iteration of the loop to inform of where at in the creation process
    print(i)
