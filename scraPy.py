import requests
from bs4 import BeautifulSoup

# url of what you want to get
# header you can look up online, i don't think it's necessarily necessary.
url = "https://www.pdx.edu/registration/academic-calendar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}

# gets the url through with the header...
r = requests.get(url, headers=headers)
# I don't really know what this does
soup = BeautifulSoup(r.content, "html.parser")

# finds all the spans with the particular class.
events = soup.find_all('span', class_ = 'title')
mesDates = soup.find_all('var', class_ = "atc_date_start")
names, dates = [], []

for item in events:
	# .strip() replaces all of the extra whitespace n the line.
	names.append(item.text.strip().replace("\n", ""))
for date in mesDates:
	dates.append(date.text.replace(" 00:00:00", ""))


for i in range(0, len(dates)):
	print(dates[i], " ", names[i])

# print(events[:10])
# print(names[:10])
# print(dates[:10])

# def main():
# 	print("Hello World")

# if __name__ == "__main__":
# 	main()