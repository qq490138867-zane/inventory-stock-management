from inventory_manager import InventoryManager
from search_sort import (
    search_by_name,
    sort_by_name,
    sort_by_price,
    sort_by_quantity,
)
from charts import show_stock_chart


def display_products(products, title="Products"):
    """
    Display a list of products in a formatted table.
    """

    print(f"\n===== {title} =====")

    if not products:
        print("No products found.")
        return

    print("-" * 78)
    print(
        f"{'ID':<12}"
        f"{'Name':<20}"
        f"{'Category':<18}"
        f"{'Price':<12}"
        f"{'Quantity':<10}"
    )
    print("-" * 78)

    for product in products:
        print(
            f"{str(product['id']):<12}"
            f"{product['name']:<20}"
            f"{product['category']:<18}"
            f"£{product['price']:<11.2f}"
            f"{product['quantity']:<10}"
        )

    print("-" * 78)


def get_valid_price(prompt):
    """
    Ask the user for a valid non-negative price.
    """

    while True:
        try:
            price = float(input(prompt))

            if price < 0:
                print("Price cannot be negative.")
                continue

            return price

        except ValueError:
            print("Please enter a valid number.")


def get_valid_quantity(prompt):
    """
    Ask the user for a valid non-negative quantity.
    """

    while True:
        try:
            quantity = int(input(prompt))

            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            return quantity

        except ValueError:
            print("Please enter a valid whole number.")


def add_product(manager):
    """
    Add a new product to the inventory.
    """

    print("\n===== Add Product =====")

    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    category = input("Category: ").strip()

    if not product_id or not name or not category:
        print("Product ID, name and category cannot be empty.")
        return

    price = get_valid_price("Price: £")
    quantity = get_valid_quantity("Quantity: ")

    added = manager.add_product(
        product_id,
        name,
        category,
        price,
        quantity,
    )

    if added:
        print("Product added successfully.")
    else:
        print("A product with this ID already exists.")


def view_products(manager):
    """
    Display all products.
    """

    products = manager.get_all_products()
    display_products(products, "All Products")


def search_products(manager):
    """
    Search for products by ID or name.
    """

    print("\n===== Search Product =====")
    print("1. Search by Product ID")
    print("2. Search by Product Name")

    search_choice = input("Choose an option: ").strip()

    if search_choice == "1":
        product_id = input("Enter Product ID: ").strip()
        product = manager.find_product(product_id)

        if product:
            display_products([product], "Search Result")
        else:
            print("Product not found.")

    elif search_choice == "2":
        keyword = input("Enter product name: ").strip()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        products = manager.get_all_products()
        results = search_by_name(products, keyword)

        display_products(results, "Search Results")

    else:
        print("Invalid option.")


def update_product(manager):
    """
    Update an existing product.
    """

    print("\n===== Update Product =====")

    product_id = input("Enter Product ID: ").strip()
    product = manager.find_product(product_id)

    if not product:
        print("Product not found.")
        return

    print("Press Enter to keep the current value.")

    name = input(
        f"Product Name [{product['name']}]: "
    ).strip()

    category = input(
        f"Category [{product['category']}]: "
    ).strip()

    price_input = input(
        f"Price [{product['price']:.2f}]: £"
    ).strip()

    quantity_input = input(
        f"Quantity [{product['quantity']}]: "
    ).strip()

    if name == "":
        name = product["name"]

    if category == "":
        category = product["category"]

    if price_input == "":
        price = product["price"]
    else:
        try:
            price = float(price_input)

            if price < 0:
                print("Price cannot be negative.")
                return

        except ValueError:
            print("Invalid price.")
            return

    if quantity_input == "":
        quantity = product["quantity"]
    else:
        try:
            quantity = int(quantity_input)

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

        except ValueError:
            print("Invalid quantity.")
            return

    updated = manager.update_product(
        product_id,
        name,
        category,
        price,
        quantity,
    )

    if updated:
        print("Product updated successfully.")
    else:
        print("Product could not be updated.")


def delete_product(manager):
    """
    Delete a product from the inventory.
    """

    print("\n===== Delete Product =====")

    product_id = input("Enter Product ID: ").strip()
    product = manager.find_product(product_id)

    if not product:
        print("Product not found.")
        return

    display_products([product], "Product to Delete")

    confirmation = input(
        "Are you sure you want to delete this product? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        deleted = manager.delete_product(product_id)

        if deleted:
            print("Product deleted successfully.")
        else:
            print("Product could not be deleted.")
    else:
        print("Deletion cancelled.")


def show_low_stock(manager):
    """
    Display products with low stock.
    """

    print("\n===== Low Stock Report =====")

    limit_input = input(
        "Enter low-stock limit or press Enter to use 5: "
    ).strip()

    if limit_input == "":
        limit = 5
    else:
        try:
            limit = int(limit_input)

            if limit < 0:
                print("Stock limit cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid whole number.")
            return

    products = manager.get_low_stock(limit)
    display_products(products, f"Products With Stock of {limit} or Less")


def sort_products(manager):
    """
    Sort and display products.
    """

    print("\n===== Sort Products =====")
    print("1. Sort by Name")
    print("2. Sort by Price")
    print("3. Sort by Quantity")

    sort_choice = input("Choose an option: ").strip()
    products = manager.get_all_products()

    if not products:
        print("No products available.")
        return

    if sort_choice == "1":
        sorted_products = sort_by_name(products)
        title = "Products Sorted by Name"

    elif sort_choice == "2":
        sorted_products = sort_by_price(products)
        title = "Products Sorted by Price"

    elif sort_choice == "3":
        sorted_products = sort_by_quantity(products)
        title = "Products Sorted by Quantity"

    else:
        print("Invalid option.")
        return

    display_products(sorted_products, title)


def display_stock_chart(manager):
    """
    Display the inventory stock chart.
    """

    products = manager.get_all_products()
    show_stock_chart(products)


def display_menu():
    """
    Display the main menu.
    """

    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Low Stock Report")
    print("7. Sort Products")
    print("8. Stock Chart")
    print("9. Exit")


def main():
    """
    Run the inventory management system.
    """

    manager = InventoryManager()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_product(manager)

        elif choice == "2":
            view_products(manager)

        elif choice == "3":
            search_products(manager)

        elif choice == "4":
            update_product(manager)

        elif choice == "5":
            delete_product(manager)

        elif choice == "6":
            show_low_stock(manager)

        elif choice == "7":
            sort_products(manager)

        elif choice == "8":
            display_stock_chart(manager)

        elif choice == "9":
            print("Thank you for using the Inventory Management System.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 9.")


if __name__ == "__main__":
    main()
