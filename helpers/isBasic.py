
mid_ = 0
mutex = 1

def getLen():
	return h


def binarySort(word, l, h, count=0):
	# breakpoint()

	if len(word)<3:
		return 1

	global mutex

	if mutex and isLearned(word):
		mutex = 0
		return 1

	# if mutex:


	global mid_
	mid = (l+h)//2

	# to get out of Infinite loop
	if mid_== mid:
		# print(word, 'Infinite Loop')
		return 0 

	mid_ = mid


	# checking for valid word
	 


	if word == '' or word == ' ':
		# print('"', word, '" not valid word')
		return 0

	if l >= h:
		# print(word, "Not Found")
		return 0

	word2 = words_data[mid].strip()
	# print(l, h, word2)

	try:
		if word2[count] > word[count]:
			return binarySort(word, l, mid-1, count)
		elif word2[count] < word[count]:
			return binarySort(word, mid+1, h, count)
		else:
			if word==word2:
				# print(word, "Found")
				return 1

			mx = len(word) if len(word)<len(word2) else len(word2)

			while count < mx and word[count]==word2[count]:
				count += 1


			# check if one of words is exhausted
			if count == len(word):
				# word < word2
				h = mid

			elif count == len(word2):
				# word > word2
				l = mid
			
			elif word[count]>word2[count]:
				l = mid

			else:
				h = mid

			return binarySort(word, l, h)
		return 1


	except Exception as e:
		print('Exception' , e)

	finally:
		file.close()


def isLearned(word):
	# print('word in learned', word)
	words = file1.readlines()
	print(words)
	if word+'\n' in words:
		print(word)
		return 1
	return 0


if __name__ == '__main__':
	file = open('../assets/3000.txt', 'r+')
	file1 = open('../assets/learned.txt', 'r+')
else:
	file = open('assets/3000.txt', 'r+') # it'll be open from main.py so curdir = ../
	file1 = open('assets/learned.txt', 'r+')



words_data = file.readlines()
h = len(words_data)

