books = int(input())

summer = int(input())
library = set()
summerbooks = set()
for i in range(books):
    booksinl = input()
    library.add(booksinl)
for f in range(summer):
    summers = input()
    summerbooks.add(summers)

for k in summerbooks:
    if k in library:
        print('YES')
    else:
        print('NO')