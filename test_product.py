import pytest
from products import Product


def test_create_normal_product():
    product = Product("product1", 10.0, 100)
    assert product.name == "product1"
    assert product.price == 10.0
    assert product.quantity == 100
    assert product.active == True


def test_create_product_with_invalid_name():
    with pytest.raises(Exception):
        Product("", 20.0, 100)


def test_create_product_with_invalid_price():
    with pytest.raises(Exception):
        Product("product1", -20.0, 100)


def test_create_product_with_invalid_quantity():
    with pytest.raises(Exception):
        Product("product1", 20.0, -5)


def test_deactivate_product_when_quantity_zero():
    product = Product("Product3", 10.0, 3)
    product.set_quantity(0)
    assert product.active == False


def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("Product4", 10.0, 5)
    quantity_before_purchase = product.quantity
    product.buy(3)
    assert product.quantity == quantity_before_purchase - 3


def test_buying_larger_quantity_than_exists_does_not_raise_exception():
    product = Product("Product5", 10.0, 5)
    product.buy(7)



pytest.main()
