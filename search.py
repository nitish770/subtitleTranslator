import re
import requests
from helpers.logger import *
import random
from configparser import ConfigParser


def getToken(file="config.py"):
	from config import keys
	return random.choices(keys)



def randomColor():
	colors = {
		'BLUE': '\x1b[34m', 'CYAN': '\x1b[36m',
		'GREEN': '\x1b[32m', 'LIGHTBLACK_EX': '\x1b[90m', 'LIGHTBLUE_EX': '\x1b[94m',
		'LIGHTCYAN_EX': '\x1b[96m', 'LIGHTGREEN_EX': '\x1b[92m', 'LIGHTMAGENTA_EX': '\x1b[95m',
		'LIGHTWHITE_EX': '\x1b[97m', 'LIGHTYELLOW_EX': '\x1b[93m',
		'MAGENTA': '\x1b[35m', 'RED': '\x1b[31m', 'RESET': '\x1b[39m', 'WHITE': '\x1b[37m',
		'YELLOW': '\x1b[33m'
		}

	return colors[random.choices([i for i in colors.keys()])[0]]


def resetColor():
	print('\x1b[97m')


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
	key = getToken()

	app_id , app_key = key[0]

	language = 'en-us'

	url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word.lower()
	r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

	if r.status_code == 200:
		count = 1
		pronounce  = ptrn_pronounce.findall(r.text)
		pronounce_ = list(set([i[2:-1] for i in pronounce]))

		print("\x1b[91mPronunciation : \x1b[97m")
		resetColor()

		if pronounce:
			for i in pronounce_:
				print('\t', count, randomColor() + i)
				resetColor()
				count += 1

		mean = ptrn_mean.findall(r.text)
		mean_ = [i[1:-1] for i in mean]

		count = 1
		print("\n\x1b[91mMean : \x1b[97m")
		if mean:
			for i in mean_:
				print('\t', count, randomColor() + i)
				resetColor()
				count+=1

		successful(word, pronounce_, mean_)

	else:
		# log into log.log
		unSuccessful(word)
		print('Couldn\'t found ')

	return r.text

