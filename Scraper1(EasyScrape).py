import urllib2
import requests
import os
from bs4 import BeautifulSoup

ack = raw_input("\n Welcome to the SciOly Python web scraper. This version scrapes from \"https://scioly.org/tests/\", and was written in January 2018. This scraper will download all files into a folder named DUMP, or create on if it does not exist in the directory of the this \".py\" file Please check that the webpage has not changed from its January 2018 version to ensure that the webscraper will scrape sucessfully. \n\n This program requires the libraries: urllib2, requests, os and BeautifulSoup. \n\n Continue? (y/n): ")
if ack is "y":
	linkedURL = ""
	urlToQuote = "https://scioly.org/tests/"
	pageQuote = urllib2.urlopen(urlToQuote)
	rawHTML = BeautifulSoup(pageQuote, 'html.parser')
	# print rawHTML
	tds = rawHTML.find_all('td', attrs={'id' : 'type'})
	# print tds
	if not os.path.exists("DUMP"):
		os.makedirs("DUMP")
	for td in tds:
		# print td
		# print("\n")
		for anchors in td.find_all('a'):
			# print anchors
			linkedURL = anchors.get('href')
			print linkedURL
			r = requests.get(linkedURL, allow_redirects=True)
			open(linkedURL[linkedURL.rfind("/")+1:], 'wb').write(r.content)
			os.rename(linkedURL[linkedURL.rfind("/")+1:], ("DUMP\\" + linkedURL[linkedURL.rfind("/")+1:]))	
	exit = raw_input("\n Press any key to exit: ")
else:
	exit = raw_input("\n Press any key to exit: ")
