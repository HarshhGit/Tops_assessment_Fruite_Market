# FruitMarket Main File

from manager import FruitMarket
from customer import customer_role


def main():
    while True:
        print(" WELCOM TO FRUIT MARKET")

        print("1) Manager ")
        print("2) Customer ")
        role = input("Select role: ")

        if role == '1':
            market = FruitMarket()
            market.manager_role()
        elif role == '2':
            customer_role()
        else:
            print("Invalid role!!! Please try again.")