# number = int(input('Введите количество покупок: '))
# buys = []
# for i in range(number):
#     buy = input('Введите покупку: ')
#     buys.append(buy)
# for n in range(number):
#     if n == (number - 1):
#         print(buys[n])
#     else:
#         print(buys[n], end = ', ')
    

# finds = []
# n = int(input('Введите количество запросов: '))
# for i in range(n):
#     find = input('Введите запрос: ')
#     finds.append(find)
# wtf = input('Введите строку: ')
# for n in finds:
#     if wtf in n:
#         print(n)

n = int(input())
meows = []
for i in range(n):
    meow = int(input())
    meows.append(meow)
for n in range(len(meows) - 1):
    print(meows[n] + meows[n + 1])