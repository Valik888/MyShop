class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop name: {self.shop_name}")
        print(f"Store type: {self.store_type}")

    def open_shop(self):
        print("The online shop is now open.")

    def set_number_of_units(self, num_units):
        self.number_of_units = num_units

    def increment_number_of_units(self, increment):
        self.number_of_units += increment


class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discount_products(self):
        print("Products with discounts:")
        for product in self.discount_products:
            print(product)

