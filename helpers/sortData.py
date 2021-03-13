import requests
from bs4 import BeautifulSoup as bs 
from urllib import request
from urllib.error import URLError, HTTPError
import re
from typing import List


class AppURLopener(request.FancyURLopener): # else can't scrape oxfordlearnersdictionaries.com
    version = "Mozilla/5.0"


class OxfordScraper:

	def __init__(self):
		self.titles = []
		self.words = []
		self.opener = AppURLopener()


	def driver(self):
		for title in self.getTitle():
			print('working ', title)
			self.scrapeWords(title) # first page

			for page_url in self.getPagesList(title): # pages from 2

				print('working', page_url)
				self.scrapeWords(page_url)

				print(page_url, ' done')
				self.writeInFile(self.words)	# write list text to file
				self.words = []



	def getTitle(self):
		url = 'https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/Oxford3000_A-B/'
		response = self.opener.open(url)
		bs_obj = bs(response, 'lxml')
		res = bs_obj.find_all("ul", {"class" : "hide_phone"})

		if res:
			res = str(res[0])


		self.titles = re.findall(r'href="(.*)"', res)
		self.titles.insert(0, url)

		return sorted(self.titles)


	def getPagesList(self, link:str):
		response = self.opener.open(link)
		bs_obj = bs(response, 'lxml')
		# print(bs_obj)
		results = bs_obj.find_all("div", class_="outer")
		# print(results)
		if results:
			results = re.findall(r'href="(.*)"', str(results[0]))

		# print(results)

		return sorted(set(results))


	def scrapeWords(self, link):
		response = self.opener.open(link)
		bs_obj = bs(response, 'lxml')
		# print(bs_obj)
		results = bs_obj.find_all("ul", class_="wordlist-oxford3000")
		# print(results)

		for i in results[0].find_all('li'):
			# print(i)
			if(i.a):
				self.words.append(i.a.text.strip())

	def writeInFile(self, words:List, file='3000.txt'):
		with open(file, 'a+') as f:
			for i in words:
				f.write(i+'\n')

