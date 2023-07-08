"""
Write a script that will get a list of all users for the website. 
The script should output a csv file with list of all email addresses.

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

# Empty list to store all of the email addresses
email_addresses = []

# Set initial and per_page values to use pagination to retrieve all customers
page = 1
per_page = 100

# Create a while loop to retrieve customers per page, until all customers are retrieved
while True:
    # Variable to call the WC API and retrieve customers per_page
    customers = wcapi.get("customers", params={"page": page, "per_page": per_page}).json()

    # Extract email addresses and append to the list
    for customer in customers:
        email_addresses.append(customer['email'])

    # Break the loop if the current page has fewer customers than the per_page value
    if len(customers) < per_page:
        break

    # Increment the page number for the next iteration
    page += 1

# Create the CSV file
filename = 'customer_emails1.csv'
with open(filename, 'w') as file:
    # Write the a header
    file.write('Email\n')
    
    # Write the email addresses to the CSV file
    for email in email_addresses:
        file.write(email + '\n')

print(f"CSV file '{filename}' has been created successfully.")
