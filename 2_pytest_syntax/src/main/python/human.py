class Human:
    def __init__(self, name, yob):
        self.name = name
        if yob > 2020:
            raise ValueError("This is impossible")
        self.yob = yob

    def age(self):
        return 2020 - self.yob

    def describe(self):
        return f"{self.name} is {self.age()} years old."
