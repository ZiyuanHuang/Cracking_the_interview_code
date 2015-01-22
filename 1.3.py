#Given two strings, write a method to decide 
#if one is a permutation of the other
def buildict(str):
	dict = {}
	for eachletter in str:
		key = ord(eachletter)
		# dict[letter] = 1
		if dict.has_key(key) == False:
			dict[key] = 1
		if dict.has_key(key) == True:
			times = dict[key]
			dict[key] = times + 1
	return dict

def ifpermutation(str1, str2):
	length1 = len(str1)
	length2 = len(str2)
	if length1 != length2:
		print("Not permutation")
		return
	dict1 = buildict(str1)
	dict2 = buildict(str2)
	if cmp(dict1, dict2) == 0:
		print("permutation")
	else:
		print("Not permutation")
def main():
	str1 = "I love You"
	str2 = "you love I"
	ifpermutation(str1,str2)

main()

