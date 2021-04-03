# name = set()
# animal = {'cat', 'fox', 'dog'}

# print(animal)
# for i in animal:
#     print(i)

# if 'dog' in animal:
#     print('element in set')
# else:
#     print('no')
# boo = 'bobo'
# animal.add(boo)
# print(animal)

# myset = set()
# myset.add('a')
# myset.add('b')
# myset.add('c')
# print(myset)

# myset.remove('a')
# print(myset)
# myset.discard('a')
# print(myset)
myset1 = {1, 4, 9, 3}
myset2 = {8, 2, 0, 1}
giffer = myset1.difference(myset2)
bobo = myset1 - myset2
print(giffer)
print(bobo)

sim = myset1.symmetric_difference(myset2)
print(sim)