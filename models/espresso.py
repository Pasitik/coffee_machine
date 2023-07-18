from models.coffee_maker import Coffee
import json

class Espresso(Coffee):
    def __init__(self):
        super().__init__()

    def make_espresso(self):
        Coffee.items["__water"] -= 250
        Coffee.items["__milk"] -= 5
        Coffee.items["__coffee"] -= 4
        Coffee.items["__money"] += 5
        with open("resources.json", "w") as f:
            json.dump(Coffee.items, f, indent=4)
        print(Coffee.items)

    



