class Cup():
    def __init__(self, size, quantity):
        self.quantity = quantity
        quantity = 0
        self.size = size
        print(quantity)

    def fill(self, millimeters):
        if self.quantity + millimeters <= self.size:
            self.quantity += millimeters

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
