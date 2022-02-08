# sudo apt install python3.8-venv
# python3 -m venv env (создание виртуального пространства)
# nano requirements.txt (файл, в котором хранятся названия библиотек)
# source env/bin/activate  OR . env/bin/activate
# deactivate
# pip3 freeze
# pip3 install -r requirements.txt

import requests
from bs4 import BeautifulSoup as BS
import csv  # как эксель

def get_html(url):
    response = requests.get(url)  # результат запроса
    # print(response.status_code)
    # print(response.text) # shows response content
    return response.text

# 200 - success
# 201 - successfully installed

def get_data(html):
    soup = BS(html, 'lxml')
    # print(soup)
    catalog = soup.find('div', class_ = 'grid-list') # первое попавшееся совпадение (тэг блока, класс блока)
    # print(catalog)
    mobiles = catalog.find_all('div', class_ = 'ty-column4')
    # print(mobiles[0].find('img').get('alt'))
    # print(mobiles[0].find('img').get('data-ssrc')) 
    for mobile in mobiles:
        try:
            title = mobile.find('img').get('alt')
        except:
            title = ''

        try:
            image = mobile.find('img').get('data-ssrc')
        except:
            image = ''
        
        data = {
            'title': title,
            'image': image
        }
        # print(data)
        write_csv(data)

def write_csv(data):
    with open('mobiles.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')

        writer.writerow(
            (data['title'],
            data['image'])
        )


def main():
    for page in range(1,16):
        print(f'Парсим {page} страницу')
        url = f'https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru/page-{page}'
        html = get_html(url)
        data = get_data(html)

main()




