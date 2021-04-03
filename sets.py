eng = int(input('Введите колво учеников, изучающих английский: '))
nem = int(input('Введите колво учеников, изучающих немецкий: '))
names = set()
for i in range(eng + nem):
    name = input('Введите фамилию: ')
    if name in names:
        names.remove(name)
    else:
        names.add(name)

print(len(names))
    