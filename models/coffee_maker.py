import json
class Coffee():

    items = None

    def __init__(self):
        with open("resources.json", "r") as f:
            Coffee.items = json.load(f)

            #print(Coffee.items)

        self.water = Coffee.items["__water"]
        self.milk = Coffee.items["__milk"]
        self.coffee = Coffee.items["__coffee"]
        self.money = Coffee.items["__money"]

    def make_payments(self):
        coin = input("Please make payment of 5rs: ")
        self.items["__coin"] = int(coin)
        if self.items["__coin"] > 5:
            balance = self.items["__coin"] - 5
            print("here is your change of {}".format(balance))
        elif self.items["__coin"] < 5:
            print("Sorry that's not enough, here is your refund of {}".format(self.items["__coin"]))
            return
        name = type(self).__name__
        print("{} recieved \nmaking {}".format(self.items["__coin"], name))

    def resources(self):
        assert self.water > 0, "Sorry, there isnt enough water"
        assert self.milk > 0, "Sorry, there isnt enough water"
        assert self.coffee > 0, "Sorry, there isnt enough coffee"
        print("enough resources")

    

    
    
