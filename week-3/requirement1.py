import urllib.request as req
import json, re, csv

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response:
    dataRaw = json.load(response)["result"]["results"]

colName = ["景點名稱", "區域", "經度", "緯度", "第一張圖檔網址"]
data =[]

for place in dataRaw:
    xpostDate = place["xpostDate"]
    if xpostDate > "2015/01/01":
        stitle, longitude, latitude = place["stitle"], place["longitude"], place["latitude"]
        address = re.search("..區", place["address"]).group(0)
        file_ = re.search("(https).+?(.jpg|.JPG|.png|.PNG)", place["file"]).group(0)
        newList = [stitle, address, longitude, latitude, file_]
        data.append(newList)
    else:
        continue

with open("data.csv", mode="w", encoding="utf-8 sig", newline="") as file:
    write = csv.writer(file)
    write.writerow(colName)
    write.writerows(data)