
class Book:
    def __init__(self, id, name, price, availability=1):
        self.id = id
        self.name = name
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"{self.id},{self.name},{self.price},{self.availability}"
