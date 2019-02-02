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
        self.price = price  # Name Wrangling
        self.qoh = qoh

    # Methods
    def print_details(self):
        print(f"Name = {self.name}, Price = {self.price}, Qoh = {self.qoh}")

    def net_price(self):
        return self.price + (self.price * Product.tax / 100)

    # Special methods
    def __str__(self):
        return f"{self.name},{self.price},{self.qoh}"

    def __eq__(self, other):
        print('__eq__')
        return self.name == other.name

    def __gt__(self, other):
        return self.__price > other.__price

    @property
    def amount(self):
        return self.price * self.qoh


class DiscountProduct(Product):
    def __init__(self, name, price, qoh=0, disrate=10):
        Product.__init__(self, name, price, qoh)
        self.disrate = disrate

    # Overriding net_price() of Product class
    def net_price(self):
        discount = self.price * self.disrate / 100
        grossprice = self.price - discount
        tax = grossprice * Product.tax / 100
        return grossprice + tax


dp = DiscountProduct("Product 1", 10000, 5, 30)
print(dp.net_price())

# Create object
p1 = Product("iPhone X", 80000, 10)
print(p1.amount)
print(p1.net_price())
Product.set_tax(20)
print(p1.net_price())
