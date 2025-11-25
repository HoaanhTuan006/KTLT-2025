class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

a = Circle(2)
print(a.area())
