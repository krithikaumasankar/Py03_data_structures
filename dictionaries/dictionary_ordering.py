mydict = {3: "python", 4: "linux", 2: "c", 1: "java"}
ascending = dict(sorted(mydict.items()))
descending = dict(sorted(mydict.items(),reverse=True))
print("Original Dictionary:",mydict)
print("Ascending Order:",ascending)
print("Descending Order:",descending)
