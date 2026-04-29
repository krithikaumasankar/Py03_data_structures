l = eval(input("Enter the list: "))

while True: 	#it repeat the program continuously until a break statement stops it.
    print("\n****** MENU ******\n")
    print("1.To find the maximum value")
    print("2.To find the minimum value")
    print("3.To slice")
    print("4.To count the number of occurrences of any item")
    print("5.To find the first occurence of the item")
    print("6.Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 6:
        print("Exiting...")
        break

    if choice == 1:
        print("maximum ==> ",max(l))
    elif choice == 2:
        print("minimum ==> ",min(l))
    elif choice == 3:
        start = int(input("Enter starting index: "))
        end = int(input("Enter ending index: "))
        print("Sliced list ==> ", l[start:end])
    elif choice == 4:
        item = eval(input("Enter the item to count: "))
        if item in l:
            print("'",item,"' occurs '",l.count(item),"' times")
        else:
            print(item," is not found..")
    elif choice == 5:
        item = eval(input("Enter the item to find its first oocurence: "))
        if item in l:
            print("First occurence of '",item,"' is in the index '",l.index(item),"'")
        else:
            print(item," is not found in the list..")
    else: 
        print("Invalid choice...")
