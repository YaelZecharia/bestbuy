
class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        """ Adding a product to the store. """
        self.list_of_products.append(product)

    def remove_product(self, product):
        """ Removing a product from the store (if exists). """
        try:
            self.list_of_products.remove(product)
        except ValueError:
            print(f"Product not found in store")

    def get_total_quantity(self) -> int:
        """ Return a total of the products quantity. """
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """ Returns a list of all the products. """
        list_of_active_products = []
        for product in self.list_of_products:
            if product.is_active():
                list_of_active_products.append(product)
        return list_of_active_products

    def order(self, shopping_list) -> float:
        """ Takes an order and returns the total price of the order. """
        total_price = 0
        try:
            for item in shopping_list:
                product_index, product_quantity = item
                product = self.list_of_products[product_index]
                total_price += product.buy(product_quantity)
        except TypeError:
            pass
        except IndexError:
            print("no such product in stock")
        return total_price
