class Product:
    # Class attributes - static variable
    tax = 18
    @staticmethod
    def set_tax(newtax):
        Product.tax = newtax

    # Constructor
    def __init__(self, name, price, qoh=0):
        # Object attributes
        self.name = name
        self.price = price # Name Wrangling
        self.qoh = qoh

    # Methods
    def print_details(self):
        print(f"Name = {self.name}, Price = {self.price}, Qoh = {self.qoh}")

    def net_price(self):
        return self.price + (self.price * Product.tax / 100)

    # Special methods
    def __str__(self):
        return f"{self.name},{self.price},{self.qoh}"

    def __eq__(self,other):
        print('__eq__')
        return self.name == other.name

    def __gt__(self,other):
        return self.__price > other.__price


# Create object
p1 = Product("iPhone X", 80000)
print(p1.net_price())
Product.set_tax(20)
print(p1.net_price())






