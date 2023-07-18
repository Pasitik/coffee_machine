#from models.coffee_maker import Coffee
from models.latte import Latte
from models.espresso import Espresso
from models.cappuccino import Cappuccino



if __name__ == "__main__":
    is_on = True
    
    while (is_on):
        menu = input("select (purchase/report/power_off) : ")
        if menu == "power_off":
            is_on = False
        
        elif menu == "report":
            print("Water = {}ml".format(Latte().items["__water"]))
            print("Milk = {}ml".format(Latte().items["__milk"]))
            print("Coffee = {}g".format(Latte().items["__coffee"]))
            print("Money = {}rs".format(Latte().items["__money"]))




        elif menu == "purchase":
            coffee_type = input ("do you want a 'latte', a 'espresso' or a 'cappiccino': ")
            if menu == "power_off":
                is_on = False

            elif coffee_type == "latte":
                lat = Latte()
                lat.resources()
                lat.make_payments()
                lat.make_latte()

            elif coffee_type == "espresso":
                esp = Espresso()
                esp.resources()
                esp.make_payments()
                esp.make_espresso()

            elif coffee_type == "cappiccino":
                cup = Cappuccino()
                cup.resources()
                cup.make_payments()
                cup.make_cappuccino()