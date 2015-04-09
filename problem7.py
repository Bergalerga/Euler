def primes():
	currNumber = 2
	count = 0
	while True:
		if isP(currNumber):
			count += 1
			print(count)
		if count == 10001:
			print(currNumber)
			break;
		currNumber += 1

def isP(n):
	if n == 2:
		return True 
	for x in range(2, n):
		if n % x == 0:
			return False
	return True

primes()