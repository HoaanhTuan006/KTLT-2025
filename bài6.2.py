class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def area(self):
        return self.dai * self.rong

hcn = Hinhchunhat(5, 3)
print(hcn.area())
