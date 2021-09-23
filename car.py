from operator import attrgetter

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Minivan(Car):
    def __init__(self, brand, model, year, hasASD):
        super().__init__(brand, model, year)
        self.hasASD = hasASD

m = Minivan('Honda', 'Odyssey', '2021', True)
print(getattr(m, 'brand'),getattr(m, 'model'),getattr(m, 'year'),getattr(m, 'hasASD'))
print(attrgetter('brand', 'model', 'year', 'hasASD')(m))






