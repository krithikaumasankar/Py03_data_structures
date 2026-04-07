# Create an empty telephone directory
directory = {}

# Number of contacts
n = int(input("Enter number of contacts: "))

# Add contacts
for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    directory[name] = phone

# Display the directory
print("\nTelephone Directory:")
for name, phone in directory.items():		#items() ? gives both key and value
    print(name, ":", phone)