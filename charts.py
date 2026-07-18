import matplotlib.pyplot as plt


def show_stock_chart(products):
    """
    Display a bar chart showing product quantities.
    """

    if not products:
        print("No products available.")
        return

    names = [product["name"] for product in products]
    quantities = [product["quantity"] for product in products]

    plt.figure(figsize=(8, 5))
    plt.bar(names, quantities)

    plt.title("Inventory Stock Levels")
    plt.xlabel("Products")
    plt.ylabel("Quantity")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
