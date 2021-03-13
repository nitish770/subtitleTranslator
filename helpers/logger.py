import logging
import json


def successful(file, word, pro, mean):
	with open('assets/learned.txt', 'a+') as f:
		f.write(word+'\n')

	with open(file, 'a+') as f:
		
		text = f'''
{word} : ''' + ' {\n\t\t "Pronunciation" :  ' + f'{pro}, '  \
	+ '\n\n\t\t "Meaning" : [\n\t\t\t'

		for i in range(len(mean)):
			text += str(i+1) + ". " + mean[i] + '\n\t\t\t'

		text += '\n\t\t]\n}\n\n'

		f.write(text)
