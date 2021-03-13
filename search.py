import re
import requests
from helpers.logger import successful

def isBasicWord(word):
	''' check if the word is common or not
	Args:
		word : string
	return:
		0 : true
		1 : false
	'''
	pass



def getMeaning(word):

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
		# print("text \n" + r.text)

		count = 1
		pronounce  = ptrn_pronounce.findall(r.text)
		pronounce_ = [i[2:-1] for i in pronounce]

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

		successful('assets/mean.txt', word, pronounce_, mean_)
		# print(word, mean_)

				
	else:
		print('Couldn\'t found ', word)
