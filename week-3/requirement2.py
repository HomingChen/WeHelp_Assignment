import urllib.request as req
import bs4, re

url = "https://www.ptt.cc/bbs/movie/index.html"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"}

def getData(url, pages):
    data, p = [], 0
    while p<pages:
        request = req.Request(url, headers=header)
        with req.urlopen(request) as response:
            htmlRaw = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(htmlRaw,"html.parser")
        titles = root.find_all("div", class_="title")
        for title in titles:
            if title.a != None and re.match("^\[(好|普|負)雷]", title.a.string)!=None:
                data.append(title.a.string)
        nextPageURL = root.find("a", string="‹ 上頁")["href"]
        url = "https://www.ptt.cc" + nextPageURL
        print(p)
        p += 1
    data.sort()
    return data

data = getData(url,10)

with open("movie.txt", mode="w", encoding="utf-8") as file:
    for title in data:
        file.write(title+"\n")