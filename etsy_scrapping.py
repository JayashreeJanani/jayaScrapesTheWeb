import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import pandas as pd
x = PrettyTable()
x.field_names = ["Product", "Price"]
r = requests.get('https://www.etsy.com/in-en/search?q=jewellery&anchor_listing_id=1370714173&ref=hp_bubbles_in_bau_aug23&mosv=sese&moci=1180702724745&mosi=1162525649074&locationQuery=1269750&ship_to=IN')
print(r.url)#prints url
print(r.status_code)#prints status code
soup = BeautifulSoup(r.content,'html.parser')#here Beautifulsoup is a class
# print(soup.prettify())
s = soup.find_all('h3',class_='wt-text-caption v2-listing-card__title wt-text-truncate')
r = soup.find_all('span',class_='currency-value')
for _ in s:
    print(_.text)
for i in r:
    print(i.text)
data_list = []

for name, price in zip(s, r):
    try:
        product = name.text
        price = price.text
        x.add_row([product, price])
        data_list.append({
            'Product': product,
            'Price': price
        })
    except AttributeError:
        pass
print(x)
print(data_list)
def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("etsy_prod.xlsx")
    df.to_csv("etsy_prod.csv")

export_data(data_list)
print("Excel Created")



