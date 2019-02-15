from bs4 import BeautifulSoup
import requests

url = "http://www.srikanthtechnologies.com/default.aspx"
resp = requests.get(url)
bs = BeautifulSoup(resp.text, 'html.parser')
anchors = bs.find_all("a")
print("No. of images : ", len(anchors))
for a in anchors:
    if 'href' in a.attrs:
        print(a['href'])