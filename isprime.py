n = 200
def isPrime(n):
	count = 2
	while (count<n):
		if (n%count == 0):
			return False
		else:
			count = count+1
		if (count == n):
			return True
g = 0
list = [0,1]
while (g<n):
	if (isPrime(g)):
		list.append(g)
	g=g+1
print list