import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.encoding = "utf-8"
best_movies_website = response.text
soup = BeautifulSoup(best_movies_website,"html.parser")


movies = soup.find_all(name="h3", class_="title")
movie_titles = []
for movie in movies:
    title = movie.get_text()
    movie_titles.append(title)
movie_titles.reverse()

for title in movie_titles:
    movie = f"{title}\n"
    with open(f"./movies.txt", mode="a", encoding="utf-8") as new_file:
            new_file.write(movie)