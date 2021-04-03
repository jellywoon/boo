n = int(input())
strings = []
for i in range(n):
    string = input()
    if string[0] == '%' and string[1] == '%':
        string = string.replace('%%', '')
        strings.append(string)
    elif string[0] != '#' and string[1] != '#' and string[2] != '#' and string[3] != '#':
        strings.append(string)
for k in strings:
    print(k)
print(6)
print(6)
print(6)
print(6)
print(6)
print(6)
print(6)
print(6)

