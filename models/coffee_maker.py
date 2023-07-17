import json
class Coffee():
    # items = {
    #     "__water": 200, #ml
    #     "__milk": 50, #ml
    #     "__coffee": 75, #g
    #     "__coin": 0,#rs
    #     "__money": 0 #rs
    # }

    items = None

    def __init__(self):
        with open("resources.json", "r") as f:
            Coffee.items = json.load(f)

            print(Coffee.items)

        self.water = Coffee.items["__water"]
        self.milk = Coffee.items["__milk"]
        self.coffee = Coffee.items["__coffee"]
        self.money = Coffee.items["__money"]

    def resources(self):
        assert self.water > 0, "Sorry, there isnt enough water"
        assert self.milk > 0, "Sorry, there isnt enough water"
        assert self.coffee > 0, "Sorry, there isnt enough coffee"
        print("enough resources")
    
