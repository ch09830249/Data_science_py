# Ch 4
from bs4 import BeautifulSoup
html_str = "<p>Hello World</p>"
soup = BeautifulSoup(html_str, "lxml")
# print(soup)
# print("-----------------------")
# print(soup.prettify())
# print("-----------------------")
# print(soup)

html_str = "<div id='msg' class='body strikeout'>Hello World</div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div
# print(type(tag))
# print(tag.name)
# print(tag['id'])
# print(tag['class'])
# print(tag.attrs)
# print(tag.string)
# print(type(tag.string))

html_str = "<div id='msg' class='body strikeout'>Hello World <p>Final Test</p></div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div
# print(tag.string)
# print(tag.text)
# print(type(tag.text))
# print(tag.get_text())
# print(tag.get_text("-"))
# print(tag.get_text("-", strip=True))

html_str = "<div id='msg'>Hello World</div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div
# print(soup.name)
# print(type(soup.name))

html_str = "<p><!-- 註解的文字 --></p>"
soup = BeautifulSoup(html_str, "lxml")
comment = soup.p.string
print(comment)
print(type(comment))