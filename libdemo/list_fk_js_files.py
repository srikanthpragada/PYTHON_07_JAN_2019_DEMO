
import requests
from bs4 import BeautifulSoup
URL = "http://www.srikanthtechnologies.com"
resp = requests.get(URL)
bs = BeautifulSoup(resp.text,"html.parser")

scripts = bs.find_all("script")
for s in scripts:
    if 'src' in s.attrs:
        src = s['src']
        if src.endswith(".js"):
            print(src)




