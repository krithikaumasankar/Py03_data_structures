print("MATRIX 1")
r1 = int(input("Enter the number of rows: "))
c1 = int(input("Enter the number of columns: "))
#r1,c1 = map(int,input(“Enter no. of rows and columns: ”).split())
a = []
print("Enter the elements: ")
for i in range(r1):
    r = []
    for j in range(c1):
        value = int(input())
        r.append(value)
    a.append(r)

print("MATRIX 2")
r2 = int(input("Enter the number of rows: "))
c2 = int(input("Enter the number of columns: "))

if c1 != r2:
    print("Matrix multiplication failed...")
else:
    b = []
    print("Enter the elements: ")
    for i in range(r2):
        r = []
        for j in range(c2):
            value = int(input())
            r.append(value)
        b.append(r)
    res = []
    for i in range(r1):
        r = []
        for j in range(c2):
            s = 0
            for k in range(c1):
                s = s + a[i][k] * b[k][j]
            r.append(s)
        res.append(r)

    for i in range(r1):
        for j in range(c2):
            print(res[i][j], end=' ')
        print()