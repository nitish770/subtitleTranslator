import re
import requests
from helpers.logger import *


def changeQuote(words:list):
	# print(word)
	for n in range(len(words)):
		words[n] = words[n].replace("'", '"')
	return words


def getMeaning(word):
	''' get meaning from oxforddictionaries.com '''

	ptrn_pronounce = re.compile(r'(?<="phoneticSpelling":)(.*)')
	ptrn_mean  = re.compile(r'definitions": \[\s*(.*)', re.M)

	# temp api
	keys = [['c7b3ae10', 'c8c2609d9aafa94be8806a440df78784'],
			
			]

	app_id , app_key = keys[0]

	language = 'en-us'

	url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word.lower()
	r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

	if r.status_code == 200:
		count = 1
		pronounce  = ptrn_pronounce.findall(r.text)
		pronounce_ = list(set([i[2:-1] for i in pronounce]))

		print("Pronunciation : ")
		if pronounce:
			for i in pronounce_:
				print('\t', count, i)
				count += 1

		mean = ptrn_mean.findall(r.text)
		mean_ = [i[1:-1] for i in mean]

		count = 1
		print("\nMean : ")
		if mean:
			for i in mean_:
				print('\t', count, i)
				count+=1

		successful(word, pronounce_, mean_)

	else:
		# log into log.log
		unSuccessful(word)
		print('Couldn\'t found ')

	return r.text

