import re
import bs4
import search as srch
import sys
import time
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
			# print(words)
			# return 
			for word in words:
				word = word.lower().strip()
				# print(word)
				learned = basic.isLearned(word)
				bad_word = basic.BadWord(word)
				# print(learned)
				if (not learned) and (not bad_word):
					# print(word)
					common = basic.binarySort(word, 0, basic.getLen())
					if not common:
						print('\n\nsearching', word)
						srch.getMeaning(word)
				

if __name__ == '__main__':
	files = sys.argv[1:]
	for file in files:
		print('\n\n', file, '\n\n')
		extract(file)