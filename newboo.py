alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТНФХЦЧШЩЪЭЮЯ'
minalphabet = alphabet.lower()
n = int(input('Введите шаг шифрования: '))
s = ''
string = input('Введите текст: ')
for i in alphabet:
    if i in string:
        k = string.index(i)
        c = alphabet[k + n]
        s += c
for f in minalphabet:
    if f in string:
        k = string.index(f)
        c = alphabet[k + n]
        c = c.lower()
        s += c
for w in string:
    if w == ' ':
        k = string.index(w)
        s
        
print(s)


