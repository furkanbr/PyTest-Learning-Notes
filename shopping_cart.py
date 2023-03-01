
class ShoppingCart:
    def __init__(self, maxsize=5):
        self.items = []
        self.maxsize = maxsize

    def add(self, item):
        if len(self.items) == self.maxsize:
            raise OverflowError
        self.items.append(item)

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def get_total_price(self, priceMap):
        total_price = 0
        for item in self.items:
            total_price += priceMap.get(item)

        return total_price