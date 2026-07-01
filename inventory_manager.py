class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        return self.products
