class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize a Product object with the given name, price, and quantity.

        Params:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """

        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

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

    def get_promotion(self):
        """Get the current promotion applied to the product."""
        return self.promotion

    def set_promotion(self, promotion):
        """Set the promotion to be applied to the product."""
        self.promotion = promotion

    def show(self) -> str:
        """Returns the details of the product, including the current promotion if exists."""
        if self.promotion:
            promotion_info = f"Promotion: {self.promotion.name}"
        else:
            promotion_info = ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity) -> float:
        """
        Buy a specified quantity of the product.

        Params:
            quantity: The quantity to buy.

        Returns:
            float: The total price for the purchased quantity of the product.
        """
        try:
            if quantity > self.quantity:
                raise ValueError("Quantity is larger than what exists.")
            total_price_for_product = 0
            if self.promotion is not None:
                total_price_for_product = self.promotion.apply_promotion(self, quantity)
            else:
                total_price_for_product = quantity * self.price
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            return float(total_price_for_product)
        except ValueError as error:
            print(f"Error buying product: {error}")
            return 0


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0):
        """
        Initialize a NonStockedProduct object with the given name, price and a set quantity of zero.

        Params:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        super().__init__(name, price, quantity)

    def buy(self, quantity) -> float:
        """ returns the price of a product, after applying promotions. """
        total_price_for_product = 0
        if self.promotion is not None:
            total_price_for_product = self.promotion.apply_promotion(self, quantity)
        else:
            total_price_for_product = quantity * self.price
        return float(total_price_for_product)

    def show(self) -> str:
        """Returns the details of the product, including the current promotion if exists."""
        if self.promotion:
            promotion_info = f"Promotion: {self.promotion.name}"
        else:
            promotion_info = ""
        return f"{self.name}, Price: ${self.price}, {promotion_info}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        """
        Initialize a LimitedProduct object with the given name, price, quantity and a maximum buying limit.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        """Returns the details of the product, including the current promotion if exists."""
        if self.promotion:
            promotion_info = f"Promotion: {self.promotion.name}"
        else:
            promotion_info = ""
        return (f"{self.name}, Price: ${self.price}, Quantity: {self.quantity},"
                f" {promotion_info}, Limited to {self.maximum} per order")

    def buy(self, quantity) -> float:
        """ returns the price of a product, after applying promotions. """
        try:
            if quantity > self.maximum:
                raise ValueError(f"limited to {self.maximum} per order.")
            total_price_for_product = quantity * self.price
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            return float(total_price_for_product)
        except ValueError as error:
            print(f"Error buying product: {error}")
            return 0
