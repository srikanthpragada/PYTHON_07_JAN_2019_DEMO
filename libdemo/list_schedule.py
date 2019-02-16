
import requests
from bs4 import BeautifulSoup
URL = "http://www.srikanthtechnologies.com/schedule.xml"
resp = requests.get(URL)
bs = BeautifulSoup(resp.text,"xml")

batches = bs.find_all("batch")
for b in batches:
     print( b['subject'])




