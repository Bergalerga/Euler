from math import factorial
def factorialSum(number):
	number = str(factorial(number))
	sum = 0
	for digit in number:
		sum += int(digit)
	return sum
		
print(factorialSum(100))
	
		