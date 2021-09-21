#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-21/09/2021&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')



flights=[] # a list to flights

table = soup.find('div', attrs = {'id':'listing-id'})

for row in table.findAll('div',
						attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
	quote = {}
	quote['theme'] = row.h5.text
	quote['url'] = row.a['href']
	quote['img'] = row.img['src']
	quote['lines'] = row.img['alt'].split(" #")[0]
	quote['author'] = row.img['alt'].split(" #")[1]
	quotes.append(quote)

filename = 'flights.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['theme','url','img','lines','author'])
	w.writeheader()
	for quote in quotes:
		w.writerow(quote)
