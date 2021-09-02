from functools import reduce
import math
numbers = []
factors = [[],[],[],[],[]]
for i in range(0,5):
    element = int(input("Enter "  + str(5-i) + " natural numbers: "))
    numbers.append(element)
def primeFactors(n):
    while n%2 == 0:
        n = n/2
        factors[numbers.index(element)].append(2)
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            n = n/i
            factors[numbers.index(element)].append(i)
    if n>2:
        factors[numbers.index(element)].append(n)
for element in numbers:
    primeFactors(element)
print(factors)
def convert(factors):
    result = dict()
    for factor in factors:
        if factor in result:
            result[factor] += 1
        else:
            result[factor] = 1
    return result
def dictGCF(dict1,dict2):
    result = dict()
    commonKeys = set(dict1.keys()).intersection(set(dict2.keys()))
    for key in commonKeys:
        result[key] = min(dict1[key],dict2[key])
    return result
grandUnification = (reduce(dictGCF,map(convert,factors)))
print(math.prod(key**value for key, value in grandUnification.items()))

