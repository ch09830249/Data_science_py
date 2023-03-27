# Ch 4
# Web scraping
import requests
r = requests.get("https://www.google.com.tw/?hl=zh_TW")
print(r.status_code)
if r.status_code == 200:
    print("success")
else:
    print("fail")

url_params = {'name': '張浩', 'score': 100}
r = requests.get("https://httpbin.org/get", params=url_params)
# print(r.url)
# print(r.text)

r = requests.post("https://httpbin.org/post", data=url_params)
# print(r.url)
# print(r.text)

# https://www.flag.com.tw/
r = requests.get("https://www.flag.com.tw/")
# print(r.text)
# print(r.encoding)

r = requests.get("https://www.flag.com.tw/")
r.encoding = 'big5'
# print(r.text)
# print(r.encoding)

r = requests.get("https://www.flag.com.tw/")
# print(r.text)
# print('-------------------------')
# print(r.content)
# print('-------------------------')
# print(r.raw)

r = requests.get("https://httpbin.org/user-agent")
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
# print(requests.codes.ok)
# print(requests.codes.all_good)

r = requests.get("https://www.flag.com.tw/")
print(r.raise_for_status())

r = requests.get("https://www.google.com.tw/?hl=zh_TW")
print(r.headers['Content-Type'])
# print(r.headers['Content-Length'])
print(r.headers['Date'])
print(r.headers['Server'])

# r = requests.get("https://www.flag.com.tw/")
# fp = open("C:/Users/user/Desktop/Data_science_py/flag.txt", "w", encoding="utf8")
# fp.write(r.text)
# fp.close()

# fp = open("C:/Users/user/Desktop/Data_science_py/flag.txt", "r", encoding="utf8")
# str = fp.read()
# print("File content 1:")
# print(str)
# fp.close()

# with open("C:/Users/user/Desktop/Data_science_py/flag.txt", "r", encoding="utf8") as fp:
#     str = fp.read()
#     print("File content 2:")
#     print(str)
#     fp.close()