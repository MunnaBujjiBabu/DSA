import operator
l1 = [1,2,3]
l2 = [4,6,7]

#concatenation
l3 = l1 + l2
print(l3)


l4 = [x / y for x, y in zip(l1, l2)]
print(l4)


l5 = list(map(operator.add, l1, l2))
print(l5)

sum = []
for x, y in zip(l1, l2):
    result = x + y
    sum.append(result)

print(sum)


l6 = list(zip(l1, l2))
print(l6)

s1 = {1,2,3}
s2 = {4, 5, 6}
s3 = set(zip(s1, s2))
print(s3)