n = int(input('Введите че-то: '))
if n <= 9 and n >= 1:
    for i in range(n, 0, -1):
        i = str(i)
        print('A' + i, 'B' + i, 'C' + i, 'D' + i)
else: 
    print('ошибка')