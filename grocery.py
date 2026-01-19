class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __str__(self):
        return f"Item(name={self.name}, price={self.price:.2f})"

class Expires(Item):
    def __init__(self, name: str, price: float, expiration_date: str):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def get_expiration_date(self):
        return self.expiration_date

class Meat(Expires):
    def __init__(self, name: str, price_per_pound: float, expiration_date: str, weight: float):
        super().__init__(name, price_per_pound, expiration_date)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_price(self):
        return self.price * self.weight  # price per pound * weight


def main():
    # Unit tests
    apple = Item("Apple", 0.5)
    print(apple)
    print(f"Name: {apple.get_name()}, Price: {apple.get_price()}")

    milk = Expires("Milk", 2.5, "2024-12-20")
    print(milk)
    print(f"Name: {milk.get_name()}, Expiration Date: {milk.get_expiration_date()}")

    steak = Meat("Steak", 10.0, "2024-12-15", 2.5)
    print(steak)
    print(f"Name: {steak.get_name()}, Price: {steak.get_price()}, Weight: {steak.get_weight()}")

    print("All tests passed!")


if __name__ == "__main__":
    main()
