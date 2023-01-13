import pyfiglet

result = pyfiglet.figlet_format("ZDork 1.0", font = "big")
print("\033[91m" + result + "\033[0m")

import requests
import random
from bs4 import BeautifulSoup

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4469.69 Safari/536.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4557.102 Safari/537.36"
]

headers = {
    "User-Agent": random.choice(user_agents)
}

query = input("Enter your search query (or type 'CAMS' to search for online cameras.): ")

if query.upper() == "CAMS":
    query = "inurl:viewer/live/index.html"
    

    
url = f"https://www.google.com/search?q={query}"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("div", class_="g")

print("Results:")
for result in results:
    title = result.find("h3").text
    link = result.find("a")["href"]
    print(title)
    print(link)
    print()