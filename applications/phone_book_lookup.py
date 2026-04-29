# Create dictionary
phone_book = {}
n = int(input("Enter number of entries: "))
# Adding entries
for i in range(n):
    mobile = input("Enter mobile number: ")
    name = input("Enter person name: ")
    phone_book[mobile] = name

# Display dictionary
print("\nPhone Book:", phone_book)

# Search operation
search = input("\nEnter mobile number to search: ")

if search in phone_book:
    print("Name:", phone_book[search])
else:
    print("Mobile number not found")
