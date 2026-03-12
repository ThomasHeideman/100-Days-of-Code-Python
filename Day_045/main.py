from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_website = response.text
soup = BeautifulSoup(yc_website,"html.parser")

# articles = soup.select(" .titleline a")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.get_text()
#     link = article_tag.get("href")
#     article_texts.append(text)
#     article_links.append(link)
#
#
# article_upvotes = [int(score.get_text().split(" ")[0]) for score in soup.find_all(name="span",class_="score")]
# most_upvoted_index = article_upvotes.index(max(article_upvotes))
#
# print(article_texts[most_upvoted_index],article_links[most_upvoted_index])

all_articles = soup.find_all(name="tr", class_="athing")

combined_articles = []

for article in all_articles:
    title_tag = article.select_one(".titleline a")
    title_text = title_tag.get_text()
    link = title_tag.get("href")

    subtext_row = article.find_next_sibling(name="tr")
    score_tag = subtext_row.select_one(".score")

    if score_tag:
        upvotes = int(score_tag.get_text().split(" ")[0])
    else:
        upvotes = 0

    combined_articles.append({
        "text": title_text,
        "link": link,
        "upvotes": upvotes
    })
highest_voted_article = max(combined_articles, key=lambda x: x['upvotes'])

print(f"{highest_voted_article['text']} - {highest_voted_article['link']}" )


# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents,"html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)

# print(soup.a)
# print(soup.li)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.get_text())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id= "name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# company_url = soup.select_one(selector="p a")
# print(company_url.get_text())
# name = soup.select_one("#name").get_text()
# print(name)
# headings = soup.select(".heading")
# print(headings)