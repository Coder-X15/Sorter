def factorize(x):
    u = set([1,int(x)])
    for i in range(1,int(x)):
        if x % i == 0:
            u.add(x/i)
            u.add(i)
    return u
def HCF(*num):
    u = []
    for i in num:
        u.append(factorize(i))
    v = u[0]
    for j in range(1,len(u)):
        v = v.intersection(u[j])
    if len(v) == 2:
        return v - {1}
    else:
        y = max(v)
        return y


def LCM(*num):
	num = list(num)
	u = []
	logic = []
	for n in num:
		u.append(list(n * i for  i in range(1, 101)))
	for j in u[0]:
		logic = []
		for k in range(1, len(u)):
			if j in u[k]:
				logic.append(True)
		if logic.count(True) == len(u) - 1:
			break
	return j
