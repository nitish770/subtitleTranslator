import re
import bs4
import search as srch
import sys
import time
import multiprocessing
import helpers.logger
import helpers.isBasic as basic


word_regex = re.compile(r'\[?([a-zA-Z]+)')


def returnWord(line):
	res = word_regex.findall(line)
	return res


def extract(file):
	with open(file, 'r+') as file:
		lines = file.readlines()

		for line in lines:
			words = returnWord(line.strip())
			for word in words:  
				# print(word)
				res = basic.binarySort(word.lower(), 0, basic.getLen())
				# print(res)
				if not res:
					print('\n\nsearching', word)
					srch.getMeaning(word)
					# print(word)
				

if __name__ == '__main__':
	files = sys.argv[1:]
	for file in files:
		print('\n\n', file, '\n\n')
		extract(file)