# Ch 5
from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.flag.com.tw/")
soup = BeautifulSoup(r.text, "lxml")
print(r.text)
tag_a = soup.find("a")
print(tag_a)
print(tag_a.string)

tag_p = soup.find(name="p")
print(tag_p)
tag_a = tag_p.find(name="a")
# print(tag_p.a.string) # None
# print(tag_a.string)

tag_span = soup.find(name="p", attrs={"class": "footer-right"})
print(tag_span)