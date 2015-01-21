def ifunique1( str ):
	length = len(str)
	for index in range(length):
		for eachletter in str:
			if index == str.index(eachletter):
				continue
			if str[index] == eachletter:
				return True
	return False

s = "ap2"
if ifunique1(s) == True:
	print("not all unique")
if ifunique1(s) == False:
	print("all unique")

def ifunique2(  str ):
	char = [1] * 256
	length = len(str)
	if length > 256:
		return False
	for eachletter in str:
		num = ord(eachletter)
		if char[num] == 0:
			return False
		char[num] = 1
	return True
l = "app"
if ifunique2(s) == True:
	print("2 not all unique")
if ifunique2(s) == False:
	print("2 all unique")






