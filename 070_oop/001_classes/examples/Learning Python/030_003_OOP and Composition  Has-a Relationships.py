### file: pizzashop.py

from employees import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "orders from", server)

    def pay(self, server):
        print(self.name, "pays for item to", server)


class Oven:
    def bake(self):
        print("oven bakes")


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')         # Embed other objects
        self.chef = PizzaRobot('Bob')     # A robot named bob
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)           # Activate other objects
        customer.order(self.server)         # Customer orders from server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()                     # Make the composite
    print('#' * 23 + ' Simulate Homers order')
    scene.order('Homer')                    # Simulate Homer's order
    print('...')
    print('#' * 23 + ' Simulate Shaggys order')
    scene.order('Shaggy')                   # Simulate Shaggy's order

