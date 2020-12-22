class Order:
    def __init__(self, item, price):
        self.name = str(item)
        self.cost = float(price)
    
    def __index__(self):
        return self.value

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.cost > other.cost:
            return True
        else:
            return False

    def __add__(self, other):
        item = self.name + '+' + other.name
        price = self.cost + other.cost
        return Order(item, price)

    def item(self):
        return self.name
    
    def price(self):
        return self.cost
    
    def __str__(self):
        return f'Item: {self.name}, price: {self.cost}'