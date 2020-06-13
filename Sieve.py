import MathTools as mtools

class PrimeNumSieve:
    def __init__(self, limit):
        self.temp = []
        for i in range(1, limit):
	if mt.factorial(i) % i**2 != 0:
		self.temp.append(i)
    def __call__(self):
        self.output = []
        for j in range(len(self.temp)):
	if len(mt.factorize(self.temp[j])) == 2:
		sieve.append(self.temp[j])
	return self.output
