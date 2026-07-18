from file_handler import load_data, save_data


class InventoryManager:
    def __init__(self):
        self.products = load_data()

    def add_product(self, product):
        # Check for duplicate product ID
        if self.find_product(product["id"]) is not None:
            return False

        self.products.append(product)
        save_data(self.products)
        return True

    def get_all_products(self):
        return self.products

    def delete_product(self, product_id):
        for product in self.products:
            if product["id"] == product_id:
                self.products.remove(product)
                save_data(self.products)
                return True
        return False

    def find_product(self, product_id):
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None

    def update_product(self, product_id, updated_product):
        for index, product in enumerate(self.products):
            if product["id"] == product_id:
                self.products[index] = updated_product
                save_data(self.products)
                return True
        return False

    def get_low_stock(self, limit=5):
        """
        Return all products with stock less than or equal to limit.
        """
        return [
            product
            for product in self.products
            if product["quantity"] <= limit
        ]
