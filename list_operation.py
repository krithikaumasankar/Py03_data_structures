# Taking input for both lists at the beginning
list1 = input("Enter elements of List 1 separated by space: ").split()
list2 = input("Enter elements of List 2 separated by space: ").split()

while True:
    print("\n--- MENU ---")
    print("1. Add element at specified position (List 1)")
    print("2. Add element at the last (List 1)")
    print("3. Compare two lists")
    print("4. Print id of all elements of List 1")
    print("5. Find first occurrence of an item (List 1)")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        elem = input("Enter element: ")
        pos = int(input("Enter position: "))
        if 0 <= pos <= len(list1):
            list1.insert(pos, elem)
            print("Updated List 1:", list1)
        else:
            print("Invalid position!")

    elif choice == 2:
        elem = input("Enter element: ")
        list1.append(elem)
        print("Updated List 1:", list1)

    elif choice == 3:
        if list1 == list2:
            print("Both lists are equal")
        else:
            print("Lists are not equal")

    elif choice == 4:
        print("IDs of elements in List 1:")
        for i in list1:
            print(i, "->", id(i))

    elif choice == 5:
        item = input("Enter item to find: ")
        if item in list1:
            print("First occurrence at index:", list1.index(item))
        else:
            print("Item not found")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")