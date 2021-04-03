n = int(input())
dishesin = set()
disheveryday = set()

for i in range(n):
    dish = input()
    dishesin.add(dish)
    
days = int(input())

for k in range(days):
    day = int(input())
    for f in range(day):
        dishday = input()
        disheveryday.add(dishday)

nondishes = dishesin.difference(disheveryday)

for o in nondishes:
    print(o)


