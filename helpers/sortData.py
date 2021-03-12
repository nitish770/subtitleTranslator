
read_file = open('../assets/3000.lst')

st = set(read_file.readlines())
read_file.close()

sorted_set = sorted(st)
count = 0

def binarySort(word, l, h, count=0):
	''' Check if word is in file(lexicograhically sorted)
	return:-
		0 : false
		1 : true
	 '''
	global sorted_set


	searched = set()
	
	mid = (l+h)//2

	if l > h:
		print("Couldn't find it")
		return

	word2 = sorted_set[mid].strip()

	try:
		if word2[count] > word[count]:
			binarySort(word, l, mid, count)

		elif word2[count] < word[count]:
			binarySort(word, mid, h, count)

		else:
			print(l, mid, h, word, word2)

			if word==word2:
				print("Found")
				return

			while word[count]==word2[count] and count < len(word2):
				count += 1

			print(count)

			if word[count-1] == word2[count-1] and count == len(word2):
				# word > word2
				if len(word)>len(word2) and count == len(word2):
					l += 1

				# word < word2
				elif len(word)<len(word2) and count == len(word2):
					h -= 1

				# breakpoint()
			if len(word)>len(word2):
				elif word[count]>word2[count]:
					l = mid
				else:
					print(count, word2)
					h = mid

			binarySort(word, l, h)



	except Exception as e:
		print(e)
		print("coulndn't find it")



def createData():
	with open('../assets/3000.lst', 'w+') as f:
		for word in sorted_set:
			f.write(word)




binarySort('hello', 0, 20000)
# print('m'>'l')