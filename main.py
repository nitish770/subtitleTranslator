import re
import bs4
import search as srch
import sys
import time
import multiprocessing
import helpers.logger


word_regex = re.compile(r'\[?([a-zA-Z]+)')


def returnWord(line):
	res = word_regex.findall(line)
	return res

def extract(file):
	with open(file, 'r+') as file:
		lines = file.readlines()

		for line in lines:
			res = returnWord(line.strip())
			for word in res:
				print(word)
				# time.sleep(2)
				srch.getMeaning(word)
				

if __name__ == '__main__':
	files = sys.argv[1:]
	for file in files:
		print('\n\n', file, '\n\n')
		extract(file)