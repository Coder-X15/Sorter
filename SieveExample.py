import MathTools as mtools
# the variable below ('y') is used to store the values obtained from the first phase of filtering
y = []
for i in range(1, 100): # 100 is taken here as a sample range
    if mtools.factorial(i) % i **2 != 0: #the expression n!/n^2 used to filter out primes (alongside 4)
	y.append(i)

sieve = [] #actual sieving output is stored here
for i in range(len(y)):
	if len(mtools.factorize(y[i])) == 2:
		sieve.append(y[i])

print(sieve)
