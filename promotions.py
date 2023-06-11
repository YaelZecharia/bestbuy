from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        """
        Initialize a Promotion object with the given name.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        """
        Initialize a PercentDiscount object with the given name and a discount percent.
        """
        super().__init__(name)
        self.discount_percentage = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        applying the PercentDiscount promotion
        """
        price = product.price * quantity
        discount_amount = price * (self.discount_percentage / 100)
        discounted_price = price - discount_amount
        return discounted_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        """
        Initialize a SecondHalfPrice object with the given name.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """
        applying the SecondHalfPrice promotion
        """
        price = product.price
        half_price = product.price / 2

        full_price_quantity = quantity - (quantity // 2)
        half_price_quantity = quantity // 2

        total_price = (full_price_quantity * price) + (half_price_quantity * half_price)

        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        """
        Initialize a ThirdOneFree object with the given name.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """
        applying the ThirdOneFree promotion
        """
        discounted_price = (quantity // 3) * (2 * product.price) + (quantity % 3) * product.price
        return discounted_price
