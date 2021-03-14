
mid_ = 0
mutex = 1
file = open('assets/3000.txt', 'r+')


def getLen():
	return h


def binarySort(word, l, h, count=0):
	# breakpoint()

	if len(word)<3:
		return 1

	global mutex

	# run isLearned function only once
	if mutex and isLearned(word):
		mutex = 0
		return 1


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
			if count == len(word) :
				# word < word2
				h = mid

			elif count == len(word2) :
				# word > word2
				l = mid

			elif word[count]<word2[count]:
				h = mid

			else:
				l = mid
			
			return binarySort(word, l, h)
		return 1


	except Exception as e:
		print('Exception' , e)

	finally:
		file.close()


def isLearned(word, file='assets/learned.txt'):
	file1 = open(file, 'r+')
	words = file1.readlines()
	file1.close()

	for wrd in words:
		# print('wrod', wrd)
		if wrd.strip() == word:
			# print(wrd, word)
			return 1
	return 0


def BadWord(word, file='assets/log.log'):
	with open(file, 'r+') as f:
		lines = f.readlines()
		for line in lines:
			if line.strip() == word:
				return 1
	return 0
	

words_data = file.readlines()
h = len(words_data)
# print(binarySort('phonei', 0, getLen()))
