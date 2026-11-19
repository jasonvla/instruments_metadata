import requests
from bs4 import BeautifulSoup

# url format: "www.musikwissenschaft.uni-wuerzburg.de/musikinstrumente/bestand/inventarliste/...."

# run on single webpage for now

URL = "https://www.musikwissenschaft.uni-wuerzburg.de/musikinstrumente/bestand/inventarliste/ate1-bode-melochord/"
page = requests.get(URL)

page_str = page.text

soup = BeautifulSoup(page_str, "html.parser")

# print(soup.prettify())
for p in soup.find_all("p"):
    print(p)

# instrument name + id are usually stored within <h> tags.
# issue: not always on the same header-level. sometimes <h1>, <h3>, ...
