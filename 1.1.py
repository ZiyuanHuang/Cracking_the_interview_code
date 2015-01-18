def ifunque( str ):
	length = len(str);
	for index in range(length):
		for eachletter in str:
			if index == str.index(eachletter):
				continue
			if str[index] == eachletter:
				return True
	return False

s = "ap2"
if ifunque(s) == True:
	print("not all unique")
if ifunque(s) == False:
	print("all unique")



