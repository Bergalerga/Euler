def properdivisors(number):
	sum = 0
	for x in range(1, number/2 + 1):
		if number % x == 0:
			sum += x
	return sum

def amicable():
	total = 0	
	for number in range(1, 10001):
		dividesum = properdivisors(number)
		if number == properdivisors(dividesum) and dividesum != number:
			total += number
	return total

print(amicable())