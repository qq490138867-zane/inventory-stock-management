from inventory_manager import InventoryManager

manager = InventoryManager()

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        product = {
            "id": input("Product ID: "),
            "name": input("Product Name: "),
            "category": input("Category: "),
            "price": float(input("Price: ")),
            "quantity": int(input("Quantity: "))
        }

        manager.add_product(product)
        print("✅ Product added successfully!")

    elif choice == "2":
        products = manager.get_all_products()

        if not products:
            print("No products found.")
        else:
            print("\nCurrent Inventory")
            print("-" * 40)

            for product in products:
                print(product)

    elif choice == "3":
        product_id = input("Enter Product ID to delete: ")

        if manager.delete_product(product_id):
            print("✅ Product deleted.")
        else:
            print("❌ Product not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
