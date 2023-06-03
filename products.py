class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize a Product object with the given name, price, and quantity.

        Params:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        self.active = True
        try:
            if not name:
                raise ValueError("Name cannot be empty.")
            if price < 0:
                raise ValueError("Price cannot be negative.")
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")

            self.name = name
            self.price = price
            self.quantity = quantity

        except ValueError as error:
            print(f"Error initializing product: {error}")

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity):
        """ Set the new quantity of the product. """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """ Check if the product is active. """
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """ Prints and returns the details of the product. """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Buy a specified quantity of the product.
        Params:
            quantity: The quantity to buy.
        Returns:
            float: The total price for the purchased quantity of the product.
        Raises:
            ValueError: If the specified quantity is larger than the available quantity.
        """
        try:
            if quantity > self.quantity:
                raise ValueError("Quantity is larger than what exists.")
            total_price_for_product = quantity * self.price
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            return float(total_price_for_product)
        except ValueError as error:
            print(f"Error buying product: {error}")
            return 0
