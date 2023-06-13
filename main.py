import products
import store
import promotions


def list_products(store_obj):
    """ Prints out a list of the products in stock. """
    print("_____")
    index = 1
    for product in store_obj.get_all_products():
        print(f"{index}. {product.show()}")
        index += 1
    print("_____")


def show_total_amount(store_obj):
    """ Showing total amount of products in stock. """
    total_amount = int(store_obj.get_total_quantity())
    print(f"Total of {total_amount} items in store")


def make_order(store_obj):
    """Asking the user for a shopping list and places the order.
    prints out the total amount of the order.
    if not enough products in stock- it orders only the product that is in stock. """
    list_products(store_obj)
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    while True:
        product_num = input("Which product # do you want? ")
        if product_num == "":
            print("******")
            break
        product_quantity = input("What amount do you want? ")
        if product_quantity == "":
            print("******")
            break
        shopping_list.append((((int(product_num)) - 1), int(product_quantity)))
    total_price = store_obj.order(shopping_list)
    if total_price:
        print(f"Order made! Total payment: ${total_price}")


def quit_program(store_obj):
    """ Exits the program. """
    exit()


# a dictionary of functions.
dispatch_table = {
    "1": list_products,
    "2": show_total_amount,
    "3": make_order,
    "4": quit_program,
}


def start(store_obj):
    while True:
        print("""
   Store Menu
  ____________
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")
        choice = input("Please choose a number: ")
        if choice in dispatch_table:
            dispatch_table[choice](store_obj)
        else:
            print("Invalid choice. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
