import requests
from bs4 import BeautifulSoup
import pandas as pd

main_list = []

def extract(url):
	# url of what you want to get
	# header you can look up online, i don't think it's necessarily necessary.
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}

	# gets the url through with the header...
	r = requests.get(url, headers=headers)
	# I don't really know what this does
	soup = BeautifulSoup(r.content, "html.parser")

	# finds all the divs with the particular class.
	events = soup.find_all('div', class_ = "date views-row")
	return events

def transform(articles):
	for item in articles:
		# .strip() replaces all of the extra whitespace n the line.
		name = item.find('span', class_ = 'title').text.strip().replace('\n', '')
		date = item.find('var', class_ = 'atc_date_start').text.replace(' 00:00:00', '')
		schoolThing = {
			'date' : date,
			'name' : name
		}
		main_list.append(schoolThing)

def load():
	df = pd.DataFrame(main_list)
	df.to_csv('psuDateEvents.csv', index=False)

if __name__ == "__main__":
	url = "https://www.pdx.edu/registration/academic-calendar"
	data = extract(url)
	transform(data)
	load()
	print('Saved to CSV')
	# for i in range(0, len(main_list)):
	# 	print(main_list[i])