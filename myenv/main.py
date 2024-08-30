import requests
from bs4 import BeautifulSoup
import csv
import re

# error handling for HTTP requests in case the website is not accessible when using get. checks request errors. 
response = requests.get('https://www.jumia.co.ke/')
if response.status_code == 200:
    src = response.content
    print(src)
else:
    print('Error accessing the website', response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

top_selling_items = soup.find_all('a', class_='core')

# a function to check if element is available so as to avoid 
# AttributeError: 'NoneType' object has no attribute 'text'
def check_if_element_is_available(e):
    if e:
        return e.text.strip()
    else:
        return None

data = []
for top_selling_item in top_selling_items:
    product_name = check_if_element_is_available(top_selling_item.find('div',class_='name'))
    discounted_price = check_if_element_is_available(top_selling_item.find('div',class_='prc'))
    percent_discount = check_if_element_is_available(top_selling_item.find('div',class_='bdg _dsct'))
    data.append([product_name, discounted_price, percent_discount])

print(data)
# #  # to save data in csv format
with open('top_selling_items.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['product_name','discounted_price','percent_discount'])
    writer.writerows(data)
        
        