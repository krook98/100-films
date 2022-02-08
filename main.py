from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
page = response.text

soup = BeautifulSoup(page, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
titles = [movie.getText() for movie in movies]

with open('movies.txt', 'w') as f:
    for title in titles[::-1]:
        f.write(f"{title}\n")



