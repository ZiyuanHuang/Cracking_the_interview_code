from collections import Counter
def isSubstring (str1, str2 ):
	if not len(str1) == len(str2):
		print ('not substring')
		return
	if not Counter(str1) == Counter(str2):
		print ('not substring')
		return
	for eachletter in str1:
		index1 = str1.index(eachletter)
		index2 = str2.index(eachletter)
		if index1 == 0:
			str1head = str1[len(str1) - 1]
		else:
			str1head = str1[index1 - 1]
		if index1 == len(str1) - 1:
			str1tail = str1[0]
		else:
			str1tail = str1[index1 + 1]
		if index2 == 0:
			str2head = str2[len(str2) - 1]
		else:
			str2head = str2[index2 - 1]
		if index2 == len(str2) - 1:
			str2tail = str2[0]
		else:
			str2tail = str2[index2 + 1]
		if not str1head == str2head:
			print ('not substring')
			return
		if not str1tail == str2tail:
			print ('not substring')
			return
	print ('is substring')







