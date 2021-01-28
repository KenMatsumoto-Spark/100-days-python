from bs4 import BeautifulSoup
import lxml

#to see what a site allows to web scrape, root/romot.txt
# -------------------------------------------------------------empire exercise
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, parser="html.parser", features="lxml")

article_titles = soup.find_all(name="h3", class_="title")
titles = [movie.getText() for movie in article_titles]

titles.reverse()
titles[0] = "1) " + titles[0]


with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n")

# -------------------------------------------------------------news icombinator example
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
#
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, parser="html.parser", features="lxml")
# article_texts = []
# article_links = []
#
# articles = soup.find_all(name="a", class_="storylink")
# for article_tag in articles:
#     article_text = article_tag.getText()
#     article_link = article_tag.get("href")
#     article_texts.append(article_text)
#     article_links.append(article_link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# #
# # for i in range(0, len(article_texts)):
# #     print(article_texts[i])
# #     print(article_links[i])
# #     print(article_upvotes[i])
#
# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
#
# print(article_texts[largest_index])
# print(article_links[largest_index])
#

# ------------------------------------------------------- local website

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# # soup = BeautifulSoup(contents, "lxml")
# soup = BeautifulSoup(contents, "html.parser")
# #
# # print(soup.prettify())
#
# # all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# #
# # section_heading = soup.find(name="h3", class_="heading")
#
# company_url = soup.select_one(selector="p a")
# print(company_url)