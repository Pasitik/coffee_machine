#from models.coffee_maker import Coffee
from models.latte import Latte

if __name__ == "__main__":
    on = True
    while (on):
        coffee_type = input ("do you want a 'latte', a 'espresso' or a 'cappiccino': ")
        if coffee_type == "latte":
            lat = Latte()
            lat.resources()
            lat.make_payments()
            lat.make_latte()

