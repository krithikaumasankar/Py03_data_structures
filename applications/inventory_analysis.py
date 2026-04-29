# Step 1: Get number of products
n = int(input("Enter number of products: "))

product_list = []

# Taking input for each product
for i in range(n):
    print(f"\nEnter details of Product {i+1}")
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    
    product_list.append((pid, name, qty, price))

# Convert list to tuple
inventory = tuple(product_list)

# Step 2: Display all product details
print("\n--- All Product Details ---")
for p in inventory:
    print("ID:", p[0], "| Name:", p[1], "| Quantity:", p[2], "| Price:", p[3])

# Step 3: Search product by ID
search_id = int(input("\nEnter Product ID to search: "))
found = False

for p in inventory:
    if p[0] == search_id:
        print("Product Found:", p)
        found = True
        break

if not found:
    print("Product not found")

# Step 4: Find product with highest price
max_product = inventory[0]

for p in inventory:
    if p[3] > max_product[3]:
        max_product = p

print("\nProduct with Highest Price:")
print("ID:", max_product[0], "| Name:", max_product[1],
      "| Quantity:", max_product[2], "| Price:", max_product[3])

# Step 5: Low stock products (qty < 20)
print("\nLow Stock Products (Quantity < 20):")
found = 0
for p in inventory:
    if p[2] < 20:
        found += 1
        print("ID:", p[0], "| Name:", p[1],
              "| Quantity:", p[2], "| Price:", p[3])
if not found:
    print("There is no low stock products..")
