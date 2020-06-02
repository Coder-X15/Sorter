def factorize(x):
    # function for factorisation (not prime factorisation)
    u = set([1,int(x)]) # a set of factors (initially, 1 and the number itself)
    for i in range(1,int(x)):
	# in this loop, we try to find two numbers that can be used to express the number to be factorised
        if x % i == 0: # since factors leave 0 remainder
            u.add(x/i) # the factor no.1
            u.add(i) # the factor no.2
    return u # set of factors return 
def HCF(*num):
    # HCF (highest common factor) = GCD(greatest common divisor)
    u = []
    for i in num:
        u.append(factorize(i)) # set of factors of each number appended to list
    v = u[0]
    for j in range(1,len(u)):
        v = v.intersection(u[j]) # filtering out common factors culminatively
    if len(v) == 2:
        return list(v - {1})[0] # 1 is removed, since it is a factor of every number 
    else:
        y = max(v) # returns the highest factor in the set
        return y


def LCM(*num):
	num = list(num) 
	u = []
	logic = [] # logic list: to find if a number appears as a multiple in the list of multiples of other numbers
	for n in num:
		u.append(list(n * i for  i in range(1, 101)))
	for j in u[0]:
		logic = []
		for k in range(1, len(u)):
			if j in u[k]: # checks if j (in the multiples of the first number in the 'num' argument) appears as a multiple among the multiples of other numbers in the tuple
				logic.append(True)
		if logic.count(True) == len(u) - 1:
			break
	return j # returns the common number
# please do modify it if bugs are found...
