# Taking initial list input
lst = list(map(int, input("Enter elements of the list: ").split()))

while True:
    print("\n--- MENU ---")
    print("1. Find minimum value")
    print("2. Add element at the last")
    print("3. Print id of all elements")
    print("4. Slice the list")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(lst) > 0:
            print("Minimum value:", min(lst))
        else:
            print("List is empty!")

    elif choice == 2:
        elem = int(input("Enter element to add: "))
        lst.append(elem)
        print("Updated list:", lst)

    elif choice == 3:
        print("IDs of elements:")
        for i in lst:
            print(i, "->", id(i))

    elif choice == 4:
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced list:", lst[start:end])

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
