from order import Order

class TaxableOrder(Order):
    def __init__(self, item, price, tax):
        self.name = item
        self.cost = float(price) + float(price)*float(tax)


order1 = TaxableOrder("Someitem", 88.0, 0.05)
expected = 92.4
actual = order1.price()
print(f"Expected: {expected}\nActual: {actual}")
assert actual == expected
expected = "Item: Someitem, price: 92.4"
actual = str(order1)
print(f"Expected: {expected}\nActual: {actual}")
assert actual == expected