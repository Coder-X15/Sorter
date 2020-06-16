from math import factorial
def factorize(x):
    # function to factorise numbers
    u = set([1,int(x)])
    for i in range(1,int(x)):
        if x % i == 0:
            u.add(x/i)
            u.add(i)
    return u
def hcf(*num):
    # highest common factor (or greatest common divisor)
    u = []
    if type(num[0]) == list:
        num = num[0]
    for i in num:
        u.append(factorize(i))
    v = u[0]
    for j in range(1,len(u)):
        v = v.intersection(u[j])
    if len(v) == 2:
        return list(v - {1})[0]
    else:
        y = max(v)
        return y
    
def gcd(*num):
    #for those who love to call gcd rather than hcf :D
    return hcf(list(num))

def lcm(*num):
    # lowest common multiple
    num = list(num)
    backup = tuple(num)
    exit_stat = False
    while exit_stat is False:
        num[num.index(min(num))] += backup[num.index(min(num))]
        if num.count(num[0]) == len(num):
            exit_stat = True
            return num[0] 

