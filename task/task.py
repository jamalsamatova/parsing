# import requests
# from bs4 import BeautifulSoup as BS

# def get_html(url):
#   response = requests.get(url)
# #   print(response.status_code)
#   return response.text

# def get_data(html):
#     soup = BS(html, 'lxml')
#     heading = soup.find('h1')
#     txt = soup.find('p')
#     link = soup.find('a')
#     print(heading)
#     print(txt)
#     print(link)

# def main():
#   url = 'http://www.example.com/'
#   html = get_html(url)
#   data = get_data(html)

# main()



########################################################################

# import requests 
# from bs4 import BeautifulSoup as bs

# def get_html(url):
#   response = requests.get(url)
#   return response.text

# def get_data(html):
#   soup = bs(html, 'lxml')
#   deutch = soup.find('div', class_ = 'central-featured-lang lang4')
#   amount = deutch.find('bdi').text
#   print(amount)


# def main():
#   url = 'https://www.wikipedia.org/'
#   html = get_html(url)
#   data = get_data(html)

# main()


########################################################################

# import requests
# from bs4 import BeautifulSoup as BS

# def check_h1(url):
#   response = requests.get(url)
#   if response.status_code == 200:
#     html = response.text
#     soup = BS(html, 'lxml')
#     try:
#       soup.find('h1').text
#       print('Heading exists')
#     except:
#       print('Heading doesn\'t exist.')

# url = 'http://www.example.com/'
# check_h1(url)

########################################################################

# import requests
# from bs4 import BeautifulSoup as bs

# def get_html(url):
#   response = requests.get(url)
#   return response.text

# def get_content(html):
#   soup = bs(html, 'lxml')
#   cards = soup.find_all('div', class_ = 'feature-cards-card-info-wrapper')
#   for card in cards:
#     name = card.find('a').text
#     print(name)

# def main():
#   url = 'https://makers.kg/'
#   html = get_html(url)
#   get_content(html)

# main()

########################################################################

# import requests
# from bs4 import BeautifulSoup as bs
# import csv

# def get_html(url):
#   response = requests.get(url)
#   return response.text

# def get_content(html):
#   soup = bs(html, 'lxml')
#   cards = soup.find_all('div', class_ = 'feature-cards-card-wrapper')
#   info = {}
#   for card in cards:
#     name = card.find('a').text
#     image = 'https://makers.kg/' + card.find('img').get('src')
#     subtitle = card.find('div', class_ = 'feature-cards-card-info-subtitle').text
#     info = {
#       'name': name, 
#       'description': subtitle, 
#       'image_link': image
#     }
#     write_csv(info)
    

# def write_csv(info):
#   with open('csv_file.csv', 'a') as f:
#     content = csv.writer(f, delimiter = '/')
#     content.writerow(
#       (info['name'],
#       info['description'],
#       info['image_link'])
#     )

# def main():
#   url = 'https://makers.kg/'
#   html = get_html(url)
#   get_content(html)

# main()

########################################################################

# import requests
# from bs4 import BeautifulSoup as bs

# def get_html(url):
#   response = requests.get(url)
#   return response.text

# def get_content(html):
#   soup = bs(html, 'lxml')
#   list_ = []
#   articles = soup.find_all('div', class_ = 'DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf')
#   for article in articles:
#     title = article.find('h3', class_ = 'ipQwMb ekueJc RD0gLb').text
#     list_.append(title)
#   print(list_)
#   return list_

# def article(keyword, headlines):
#   result = list(filter(lambda title: keyword.lower() in title.lower(), headlines))
#   print(result)
      

# def main():
#   url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
#   html = get_html(url)
#   list_ = get_content(html)
#   keyword = input('Enter a keyword: ')
#   article(keyword, list_)

# main()

########################################################################

# import requests
# from bs4 import BeautifulSoup as bs

# def get_html(url):
#   response = requests.get(url)
#   return response.text

# def get_content(html):
#   soup = bs(html, 'lxml')
#   list_of_movies = soup.find_all('td', class_ = "titleColumn")
#   movies = {}
#   for movie in list_of_movies:
#     name = movie.find('a').text
#     link = 'https://www.imdb.com/' + movie.find('a').get('href')
#     movies.update({name: link})
#   return movies
    
# def get_link(name, movies):
#   for movie in movies:
#     if name.lower() in movie.lower():
#       print(movies[movie])

# def main(): 
#   url = 'https://www.imdb.com/chart/top'
#   html = get_html(url)
#   movies = get_content(html)
#   name = input('Enter movie\'s name: ')
#   get_link(name, movies)
  
# main()

########################################################################

# import requests
# from bs4 import BeautifulSoup as bs
# import csv

# def get_html(url):
#   response = requests.get(url)
#   return response.text

# def get_content(html):
#   soup = bs(html, 'lxml')
#   mobiles = soup.find_all('div', class_='item product_listbox oh')
#   for mobile in mobiles:
#     try:
#       title = mobile.find('div', class_='listbox_title oh').find('a').text.strip()
#     except:
#       title = ''
#     try:
#       image = 'https://www.kivano.kg' + mobile.find('a', class_='listbox_img pull-left').find('img').get('src')
#     except:
#       image = 'Image not found :('
#     try:
#       price = mobile.find('div', class_='listbox_price text-center').text.strip()
#     except:
#       price = ''
#     info = {
#       'title': title,
#       'image': image,
#       'price': price,
#     }
#     write_csv(info)

# def write_csv(data):
#   with open('mobiles.csv', 'a') as f:
#     writer = csv.writer(f, delimiter='/')
#     writer.writerow(
#       (
#         data['title'],
#         data['image'],
#         data['price']
#       )
#     )

# def main():
#   for page in range(1, 33):
#     print(f'Парсинг {page} страницы...')
#     url = f'https://www.kivano.kg/mobilnye-telefony/page-{page}'
#     html = get_html(url)
#     get_content(html)

# main()