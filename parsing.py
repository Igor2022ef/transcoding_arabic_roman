import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
URL_TEMPLATE = "https://www.exist.ru/Price/?pid=5D30248D"
r = requests.get(URL_TEMPLATE)
#print(r.status_code)
#print(r.text)
soup = bs(r.text, "html.parser")
list(soup.children)
print([type(item) for item in list(soup.children)])
device_names = soup.find_all('script')
tuple_1 = []
n = 0
for name in device_names:
    var = soup.get_text('Bosch 0 242 235 666')
    n += 1
    tuple_1.append(name)
#print(var)
print('len(tuple_1)')
#print(f'Количество элементов : {n}')
print(tuple_1)
#print(device_names)








#if __name__ == '__main__':