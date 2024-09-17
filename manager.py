#Fruit add function
def add_fruit(stock):
    print("ADD FRUIT IN STOCK:")
    fruit_name = input("Enter fruit name: ")
#creted add_fruit to add fruit into stock dictionary

    
    #qty as quantity of fruit in kg and it will check by isdigit if input contains string or other invalid input will get error
    #return function will get back to ask if user have enterd invalid input
    #not keyword returns boolean as true or false as per condition
    qty = input("Enter quantity (in kg): ")
    if not qty.isdigit():
        print("Invalid input! Quantity must be a number.")
        return  
    #price stores price of fruite and same for isdigit else error
    price = input("Enter price: ")
    if not price.isdigit():
        print("Invalid input! Price must be a number.")
        return 

    qty = int(qty)
    price = int(price)

    
    # updates stock in dictionary if enterd fruite alredy exists, else it will add new fruit entry 
    if fruit_name in stock:
        stock[fruit_name]['qty'] += qty  # update quantity
        stock[fruit_name]['price'] = price  # update price
    else:
        stock[fruit_name] = {'qty': qty, 'price': price}  # add new fruit to stock

    print(f"{fruit_name} added successfully!") #gives success message if enterd fruite is added to the stock

# view stock details function
def view_stock(stock):
    if not stock:
        print("No stock available.")  # Display message if dictionary is empty
    else:
# displays each fruit with its quantity and price if any stock available.
        for fruit, details in stock.items():
            print(f"{fruit}: quantity = {details['qty']}kg, Price = {details['price']} per kg")

#updates fruit entry in the stock 
def update_fruit(stock):
    fruit_name = input("Enter fruit name to update: ")

    # check if the fruit is in the stock or not
    if fruit_name in stock:
        #new quantity and price with same input validation for last qty and price
        qty = input("Enter new quantity (in kg): ")
        if not qty.isdigit():
            print("Invalid input! Quantity must be a number.")
            return  # Exit the function if input is invalid

        price = input("Enter new price (per kg): ")
        if not price.isdigit():
            print("Invalid input! Price must be a number.")
            return  # Exit the function if input is invalid

        qty = int(qty)
        price = int(price)

        # Updates the stock with new quantity and price
        stock[fruit_name] = {'qty': qty, 'price': price}
        print(f"{fruit_name} updated successfully!")
    else:
        print(f"{fruit_name} not found in stock.")  #if the fruit is not in stock

# Manager role
def manager_role(stock):
    while True:
        
        #manager role options if user have selected manager(1)
        print("\n* Fruit Market Manager *")
        print("1) Add Fruit Stock")
        print("2) View Fruit Stock")
        print("3) Update Fruit Stock")
        choice = input("Select an option to perform: ")

        # Execute the corresponding function based on the user's choice
        if choice == '1':
            add_fruit(stock)
        elif choice == '2':
            view_stock(stock)
        elif choice == '3':
            update_fruit(stock)
        else:
            print("Invalid choice! Please try again...")

        #user input will be converted into lower using lower and it will ask if user wants to select another option.
        ask_user = input("Do you want to perform another operation? Press 'y' for yes and 'n' for no: ")
        if ask_user.lower() != 'y':
            break  # break will end the loop if the user doesn't want to continue
