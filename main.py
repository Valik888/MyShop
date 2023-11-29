from shop import Shop, Discount

# a)
store = Shop("Rozetka", "ishop")
store.describe_shop()
store.set_number_of_units(3000000)
print(store.number_of_units)
store.open_shop()

# b)
store2 = Shop("ITbox", "ishop")
store2.describe_shop()
store2.set_number_of_units(20000)
print(store2.number_of_units)

# c)
print(store.number_of_units)
store.increment_number_of_units(1)
print(store.number_of_units)

# d)
store.describe_shop()
store.set_number_of_units(3900000)
print(store.number_of_units)
store.increment_number_of_units(1200)
print(store.number_of_units)

# e)
discount_store = Discount("Rozetka", "ishop")
discount_store.discount_products = ["motherboards", "solid state drives", "monitors"]
discount_store.get_discount_products()