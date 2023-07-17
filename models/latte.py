from models.coffee_maker import Coffee

class Latte(Coffee):
    def __init__(self):
        super().__init__()

    def make_payments(self):
        self.__coin = input("Please make payment of 5rs: ")
        print("{} recieved \nmaking latte".format(self.__coin))

    def make_latte(self):
        Coffee.items["__water"] -= 0.2
        Coffee.items["__milk"] -= 0.05
        Coffee.items["__coffee"] -= 1
        Coffee.items["__money"] += 5
        print(Coffee.items)

    



