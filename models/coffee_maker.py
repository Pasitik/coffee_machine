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
        coin = input("Please make payment (accepted coins are: 50rs, 150rs or 200rs): ")
        self.items["__coin"] = int(coin)
        if Coffee.items["__coin"] in Coffee.items["valid_coins"]:
            name = type(self).__name__
            print("{}rs recieved for a cup of {}".format(self.items["__coin"], name))

            if self.items["__coin"] > 5:
                balance = self.items["__coin"] - 5
                print("here is your change of {}rs".format(balance))

            elif self.items["__coin"] < 5:
                print("Sorry that's not enough, here is your refund of {}rs".format(self.items["__coin"]))
                return
            name = type(self).__name__
            print("making {}...".format(name))
            print("Enjoy...")
        else:
            print("Sorry, your coin has been rejected. Please try again(5rs/150rs/200rs)")
            return


    def resources(self):
        assert self.water > 0, "Sorry, there isnt enough water"
        assert self.milk > 0, "Sorry, there isnt enough water"
        assert self.coffee > 0, "Sorry, there isnt enough coffee"
        #print("enough resources")

    

    
    
