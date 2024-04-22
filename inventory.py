class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.item[item_name]

    def __str__(self):
        return "\n".join([f"{name}: {quantity}" for name, quantity in self.items.items()])