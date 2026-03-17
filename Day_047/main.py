import requests
import postman
from bs4 import BeautifulSoup

# url = "https://appbrewery.github.io/instant_pot/"
url ="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "nl,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0",
  }


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

product_title = soup.find(name="span", id="productTitle").get_text()
price = soup.select_one(".a-price .a-offscreen").get_text().strip()
price_float = float(price.split("EUR")[1])
ps = postman.PostMan()
alert_price = 100.00
message = f"Subject:Price Alert!\n\nNew low price detected for {product_title},\nnow only {price}\nBuy here: {url}"

if price_float < alert_price :
    ps.send(message.encode('utf-8'))

