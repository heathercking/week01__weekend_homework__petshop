# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(dictionary):
    pet_shop_name = dictionary["name"]
    return pet_shop_name

def get_total_cash(dictionary):
    total_cash = dictionary["admin"]["total_cash"]
    print(total_cash)
    return total_cash