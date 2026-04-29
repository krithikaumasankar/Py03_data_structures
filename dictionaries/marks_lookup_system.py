x = int(input("Enter the number: "))
d = {}
for i in range(x):
    n = input("Enter the name: ")
    m = input("Enter the marks: ")
    d[n] = m
while True:
    n = input("Enter name for find marks: ")
    m = d.get(n,-1)	#d.get(key,default_value)
    if m == -1:
        print("Information not found...")
    else:
        print(n,"==>",m)
    opt = input("Do you want to find another information [Yes|No]")
    if opt.lower() == "no":
        break
print("Thank you...")
