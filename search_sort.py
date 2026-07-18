def search_by_name(products, keyword):
    """
    Search products by name.
    """
    keyword = keyword.lower()

    return [
        product
        for product in products
        if keyword in product["name"].lower()
    ]


def sort_by_name(products):
    """
    Sort products by name.
    """
    return sorted(products, key=lambda product: product["name"].lower())


def sort_by_price(products):
    """
    Sort products by price.
    """
    return sorted(products, key=lambda product: product["price"])


def sort_by_quantity(products):
    """
    Sort products by quantity.
    """
    return sorted(products, key=lambda product: product["quantity"])
