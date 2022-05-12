from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/gp/product/B07PCMG75T/ref=ox_sc_saved_title_9?smid=A2CMPBTY7QNIZA&th=1"
# web = "<span aria-hidden=\"true\">$89.97</span>"
header ={ "Accept-Language": "en-US,en;q=0.9,ar;q=0.8,ms;q=0.7",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
}
website = requests.get(url, headers=header)
web = website.text
soup = BeautifulSoup(web, "html.parser")
# print(soup)

prices = soup.find_all("span", class_="a-offscreen") #attrs={"aria-hidden":"true"})
price = float((prices[0].getText().split("$"))[1])
print(price)
