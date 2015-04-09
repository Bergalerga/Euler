def sumPrime():
	currNum = 2
	sum = 2
	for x in range(3, 2000001):
		if isP(x):
			sum += x
			print(x)
	print(sum)
	
def isP(n):

# make sure n is a positive integer
	n = abs(int(n))

	if n < 2:
		return False

	if n == 2:
		return True

	if not n & 1:
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

sumPrime()