class Product:
    # Constructor
    def __init__(self, name, price, qoh=0):
        # Object attributes
        self.name = name
        self.__price = price
        self.qoh = qoh

    # Methods
    def print_details(self):
        print(f"Name = {self.name}, Price = {self.__price}, Qoh = {self.qoh}")

    # Special methods
    def __str__(self):
        return f"{self.name},{self.__price},{self.qoh}"

    def __eq__(self,other):
        print('__eq__')
        return self.name == other.name

    def __gt__(self,other):
        return self.__price > other.__price


# Create object
p1 = Product("iPhone X", 80000)
p2 = Product("iPhone X", 70000)

print( getattr(p1,'qoh',10))

print(p1)  # str(p1)
print(p1 == p2)
print(p1 != p2)
print(p1 > p2)



