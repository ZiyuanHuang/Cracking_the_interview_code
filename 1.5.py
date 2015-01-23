#Implement a method to perform basic string compression using the counts of 
#repeated characters. For example, the string aabcccccaaa would become a2blc5a3. 
#If the "compressed" string would not become smaller than the orig- inal string, 
#your method should return the original string.
def compressedStr(string):
	length = len(string)
	if length == 0:
		return ""
	num = 1
	result = ''
	for index in xrange(1, length):
		if string[index] == string[index - 1]:
			num = num + 1
			continue
		result += string[index - 1]
		result += str(num)
		num = 1
	result += string[index - 1]
	result += str(num)
	return result
string = compressedStr( 'aabcccccaaa' )
print( string )


		


