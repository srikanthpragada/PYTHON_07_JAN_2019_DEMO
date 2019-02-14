import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    sys.exit(0)

cl = resp.json()  # Convert JSON array to List of Dict
sorted_cl = sorted(cl, key=lambda d: d['population'], reverse=True)

for c in sorted_cl[:20]:
    print(f"{c['name']:40s} {c['region']:15s}  {c['population']:12d}")
