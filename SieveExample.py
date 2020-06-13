import MathTools as mtools
y = []
for i in range(1, 100):
    if mtools.factorial(i) % i **2 != 0:
	y.append(i)

sieve = []
for i in range(len(y)):
	if len(mtools.factorize(y[i])) == 2:
		sieve.append(y[i])

print(sieve)
