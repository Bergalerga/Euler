def readfile(file):
	with open(file, "r") as f:
		namelist = f.read().split(",")
	namelist.sort()
	return namelist
	
def sumOfNames():
	totalsum = 0
	currentNumberInList = 1
	namelist = readfile("p022_names.txt")
	for name in namelist:
		sumOfName = 0
		for character in name:
			if character != '"':
				sumOfName += ord(character) - 64
		sumOfName *= currentNumberInList
		totalsum += sumOfName
		currentNumberInList += 1
	return totalsum

print(sumOfNames())
				
		