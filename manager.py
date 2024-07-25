# Manager Role

class FruitMarket:
    def __init__ (self):    
        self.stock = {}     #stores fruit data

    def add_fruit(self):    #Adding fruits in stock function
        print("ADD FRUIT IN STOCK: ")
        fruit_name = input("Enter fruit Name: ")
        qty = int(input("Enter qty (in kg): "))
        price = int(input("Enter price: "))

        if fruit_name in self.stock:
            self.stock[fruit_name]['qty'] += qty
            self.stock[fruit_name]['price'] = price
        else:
            self.stock[fruit_name] = {'qty': qty, 'price' : price}
        print(f"{fruit_name} Added successfully!")

    def view_stock(self):   #Stok view function     
        if not self.stock: 
            print("No stock available.")
        else:
            for fruit, details in self.stock.items():
                print(f"{fruit}: quantity = {details['qty']}kg, Price = {details['price']} per kg")

    def update_fruit(self): #Fruit update function
        fruit_name = input("Enter fruit name to update: ")
        if fruit_name in self.stock:
            qty = int(input("Enter qty for update(in kg): "))
            price = int(input("Enter new price (per kg): "))
            self.stock[fruit_name] = {'qty':qty,'price': price}
            print(f"{fruit_name} Updated succesfully!!!")
        else:
            print(f"{fruit_name} Not found in stock.")

    def manager_role(self): #Manager Functionality
        while True:
            print("\n* Fruit Market Manager *")
            
            print("1) Add Fruit Stock")
            print("2) View Fruit Stock")
            print("3) Update Fruit Stock")
            choice = input("Select option to perform: ")

            if choice == '1':
                self.add_fruit()
            elif choice == '2':
                self.view_stock()
            elif choice == '3':
                self.update_fruit()
            else:
                print("Invalid choice!!! Please try again.")

            ask_user = input("Do you want to perform more operation: Y for yes and N for no: ")
            if "Y" or "y" in ask_user != True:
                break
                

    