class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def myName(self):
        print(self.first_name)

    def myLastName(self):
        print(self.last_name)

    def myFullName(self):
        print(f"{self.first_name} {self.last_name}")


user1 = User("Sonya", "Trubitsina")
