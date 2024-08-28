import requests
from bs4 import BeautifulSoup
import csv
import re

result = requests.get('https://www.jumia.co.ke/')
# print(result.status_code)

src = result.content
# print(src)

soup = BeautifulSoup(result.content, 'html.parser')


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
    price_after_discnt = check_if_element_is_available(top_selling_item.find('div',class_='prc'))
    percent_discnt = check_if_element_is_available(top_selling_item.find('div',class_='bdg _dsct'))
    data.append([product_name, price_after_discnt,percent_discnt])

print(data)
# #  # to save data in csv format
with open('top_selling_items.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['product_name','price_after_discnt','percent_discnt'])
    writer.writerows(data)
        

