from manager import manager_role #importes manager role to perfom add-view-update task.
from customer import customer_role

def main():
    stock = {}  #Dictionary to store the fruit stock data

    while True:
        print("WELCOME TO FRUIT MARKET")#Ask user to select role
        print("1) Manager")
        print("2) Customer")
        role = input("Select role: ")
        
        if not role.isdigit():#not keyword returns boolean as true or false as per condition isdigit check if entered input is number or not
            print("Enter Number")
        elif role == '1': # if role selected as 1 it will give access to manager using manager_role(stock) functtion else customer
            manager_role(stock)
        elif role == '2':
            customer_role()
        else:
            print("Invalid role! Please try again...")#if invalid number it will give error

        ask_role = input("Do you want to select another role? Press 'y' for yes and 'n' for no: ")
        if ask_role.lower() != 'y':#user input will be converted into lower using lower() and it will ask if user wants to change role after completed task.
            break #else break will end the loop

if __name__ == "__main__":
    main() #here the program starts
