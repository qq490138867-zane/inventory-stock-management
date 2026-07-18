from inventory_manager import InventoryManager

manager = InventoryManager()

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Low Stock Report")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        product_id = input("Product ID: ")
        name = input("Product Name: ")
        category = input("Category: ")

        while True:
            try:
                price = float(input("Price: "))
                break
            except ValueError:
                print("Please enter a valid price.")

        while True:
            try:
                quantity = int(input("Quantity: "))
                break
            except ValueError:
                print("Please enter a valid quantity.")

        product = {
            "id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }

        if manager.add_product(product):
            print("✅ Product added successfully!")
        else:
            print("❌ Product ID already exists.")

    elif choice == "2":

        products = manager.get_all_products()

        if not products:
            print("No products found.")
        else:
            print("\nCurrent Inventory")
            print("-" * 75)
            print(
                f"{'ID':<10}{'Name':<20}{'Category':<20}{'Price':<10}{'Quantity':<10}"
            )
            print("-" * 75)

            for product in products:
                print(
                    f"{product['id']:<10}"
                    f"{product['name']:<20}"
                    f"{product['category']:<20}"
                    f"£{product['price']:<9.2f}"
                    f"{product['quantity']:<10}"
                )

    elif choice == "3":

        product_id = input("Enter Product ID to search: ")

        product = manager.find_product(product_id)

        if product:
            print("\nProduct Found")
            print("-" * 40)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Category: {product['category']}")
            print(f"Price: £{product['price']}")
            print(f"Quantity: {product['quantity']}")
        else:
            print("❌ Product not found.")

    elif choice == "4":

        product_id = input("Enter Product ID to update: ")

        product = manager.find_product(product_id)

        if product is None:
            print("❌ Product not found.")

        else:

            new_name = input(f"New Name ({product['name']}): ")
            if new_name == "":
                new_name = product["name"]

            new_category = input(f"New Category ({product['category']}): ")
            if new_category == "":
                new_category = product["category"]

            while True:
                try:
                    price_input = input(f"New Price ({product['price']}): ")

                    if price_input == "":
                        new_price = product["price"]
                    else:
                        new_price = float(price_input)

                    break

                except ValueError:
                    print("Please enter a valid price.")

            while True:
                try:
                    quantity_input = input(f"New Quantity ({product['quantity']}): ")

                    if quantity_input == "":
                        new_quantity = product["quantity"]
                    else:
                        new_quantity = int(quantity_input)

                    break

                except ValueError:
                    print("Please enter a valid quantity.")

            updated_product = {
                "id": product["id"],
                "name": new_name,
                "category": new_category,
                "price": new_price,
                "quantity": new_quantity
            }

            manager.update_product(product_id, updated_product)
            print("✅ Product updated successfully!")

    elif choice == "5":

        product_id = input("Enter Product ID to delete: ")

        if manager.delete_product(product_id):
            print("✅ Product deleted.")
        else:
            print("❌ Product not found.")

    elif choice == "6":

        low_stock = manager.get_low_stock()

        if not low_stock:
            print("All products have sufficient stock.")
        else:
            print("\nLow Stock Report")
            print("-" * 50)

            for product in low_stock:
                print(
                    f"{product['id']} | "
                    f"{product['name']} | "
                    f"Quantity: {product['quantity']}"
                )

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
