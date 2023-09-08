import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import pandas as pd
x = PrettyTable()
x.field_names = ["Tool name", "Description"]
r = requests.get('http://www.radsan.in/product/')
print(r.url)#prints url
print(r.status_code)#prints status code
soup = BeautifulSoup(r.content,'html.parser')#here Beautifulsoup is a class
# print(soup.prettify())
s = soup.find_all('h4',class_='elementor-heading-title elementor-size-default')
r = soup.find_all('div',class_='elementor-text-editor elementor-clearfix')
data_list = []

for name, description in zip(s, r):
    try:
        tool_name = name.text
        tool_description = description.find('p').text
        x.add_row([tool_name, tool_description])
        data_list.append({
            'Tool name': tool_name,
            'Description': tool_description
        })
    except AttributeError:
        pass
print(x)
print(data_list)
def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("radsan_products.xlsx")
    df.to_csv("radsan_products.csv")

export_data(data_list)
print("Excel Created")



