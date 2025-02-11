import random
import time
username = None
#a login function, check roles
def login():
    global username
    count = 0
    while count < 3:
        user = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        try:
            with open("users.txt", "r") as file:
                for l in file:
                    s_user, s_pass, role = l.strip().split(",")
                    if user == s_user and password == s_pass:
                        username = user
                        print(f"Logged in successfully.\nWelcome {username}\nRole: {role}")
                        print()
                        return role 
        except FileNotFoundError:
            print("User file not found.")
        print("Invalid username or password.")
        count += 1
        if count == 3:
            print("Too many login attempts. Please try again later.")
            break

#function to hire staff
def hire_staff():
    while True:
        user = input("Enter the username for the new staff member: ").strip()
        passs = input("Enter the password for the new staff member:").strip()
        role = input("Enter the role for the new staff member: ").strip()

        try:
            with open("users.txt", "a") as file:
                file.write(f"{user},{passs},{role}\n")
            print(f"{user} is hired as a new {role} successfully.")
        except Exception as e:
            print(f"Error hiring staff: {e}")

        again = input("Do you want to hire more staff? (yes/no): ").strip().lower()
        if again != 'yes':
            return  # Ensure we return to prevent further prompts after logout

#function to fire staff
def fire_staff():
    print("Current staff members:")
    try:
        with open("users.txt", "r") as file:
            print(f"{'Username':<20} {'Role':<15}") 
            for line in file:
                username, password, role = line.strip().split(",")
                print(f"{username:<20} {role:<15}") 
    except FileNotFoundError:
        print("User file not found.")
    while True:
        user = input("Enter the username of the staff member you want to fire: ").strip()
        found = False
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
            with open("users.txt", "w") as file:
                for l in lines:
                    s_users, s_pass, role = l.strip().split(",")
                    if s_users == user:
                        found = True
                        continue #skips writing this line
                    else:  
                        file.write(l) #writing all lines back 
        except FileNotFoundError:
            print("User file not found.")
        if found:
            print(f"Staff member {user} has been fired.")
        else:
            print(f"Staff member {user} not found.")
        again = input("Do you want to fire more staff? (yes/no): ").strip().lower()
        if again!= 'yes':
            return

def edit_staff():
    print("Current staff members:")
    try:
        with open("users.txt", "r") as file:
            print(f"{'Username':<20} {'Role':<15}")  # Header for alignment
            for line in file:
                if role == "administrator":
                    continue
                username, _, role = line.strip().split(",")
                print(f"{username:<20} {role:<15}")  # Even spacing
    except FileNotFoundError:
        print("User file not found.")
    while True:
        u = input("Enter the username of the staff member you want to edit: ").strip()
        found = False
        update = [] #to store changes
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
            for l in lines:
                s_u, s_p, stored_role = l.strip().split(",")
                if s_u == u:
                    found = True
                    print(f"Editing details for {u}:")
                    n_u = input("Enter new username: ").strip()
                    n_p = input("Enter new password: ").strip()
                    n_role = input("Enter new role: ").strip()
                    update.append(f"{n_u},{n_p},{n_role}\n") #changes into the list
                    print(f"Details for {u} have been updated successfully.")
                else:
                    update.append(l) #no changes so old data into list

            if found:
                with open("users.txt", "w") as file:
                    file.writelines(update)
            else:
                print(f"Staff member '{u}' not found.")
        except FileNotFoundError:
            print("User file not found.")
        again = input("Do you want to edit more staff? (yes/no): ").strip().lower()
        if again!= 'yes':
            return

def sales_report():
    while True:  
        print("1. By Month")
        print("2. By Chef")
        print("3. Add Sales")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            sales_by_month()
        elif choice == "2":
            sales_by_chef()
        elif choice == "3":
            add_sales()
        elif choice == "4":
            admin_menu()
        else:
            print("Not a valid option. Please choose a valid option between 1 and 4.")

def add_sales():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        chef = input("Enter the chef's name: ").strip()
        item = input("Enter the item sold: ").strip()
        quantity = input("Enter the quantity sold: ").strip()
        price = None
        try:
            with open("menu.txt", "r") as file:
                for line in file:
                    category, dish, item_price = line.strip().split(',')
                    if dish.lower() == item.lower():
                        price = float(item_price)
                        break
        except FileNotFoundError:
            print("Menu file not found.")
            return

        if price is None:
            print(f"Item '{item}' not found in the menu.")
            return
        total_amount = float(quantity) * float(price)

        try:
            with open("sales.txt", "a") as file:
                file.write(f"{date},{chef},{item},{quantity},{price},{total_amount}\n")
            print("Sales entry added successfully.")
        except Exception as e:
            print(f"Error adding sales entry: {e}")
        
        a = input("Do you want to add more sales? (yes/no): ").strip().lower()
        if a!= 'yes':
            sales_report()

def sales_by_month():
    dates = set()
    while True:
        try:
            with open("sales.txt", "r") as file:
                for line in file:
                    date, _, _, _, _, _ = line.strip().split(",")
                    y_m = date[:7]  #stores the year and month 
                    dates.add(y_m)
        except FileNotFoundError:
            print("Sales file not found.")
        
        print("Available dates for sales:")
        for date in sorted(dates):
            print(date)

        month = input("Enter the date in this format -> (YYYY-MM): ").strip()
        t_s = 0
        found = False 
        print(f"Sales report for {month}:")
        try:
            with open("sales.txt", "r") as file:
                for l in file:
                    date, chef, item, quantity, price, t_a = l.strip().split(",")
                    if date.startswith(month):
                        found = True  
                        print(f"Date: {date}, Chef: {chef}, Item: {item}, Quantity: {quantity}, Total Amount: {float(t_a)}")
                        t_s += float(t_a)
        except FileNotFoundError:
            print("Sales file not found.")
        if found:
            print(f"Total sales for {month}: ${t_s:.2f}")
        else:
            print(f"No sales during {month}.")
        again = input("Do you want to view sale report of another month?(yes/no): ")
        if again!= 'yes':
            sales_report()
def sales_by_chef():
    # shows all the chef 
    chefs = set()
    try:
        with open("sales.txt", "r") as file:
            for line in file:
                _, chef_name, _, _, _, _ = line.strip().split(",")
                chefs.add(chef_name)
    except FileNotFoundError:
        print("Sales file not found.")
    
    print("Chef List:")
    for chef in sorted(chefs):
        print(chef)

    chef = input("Enter the chef name: ").strip()
    total_sales = 0
    print(f"Sales report for Chef: {chef}")
    try:
        with open("sales.txt", "r") as file:
            for l in file:
                date, chef_name, item, quantity, price, total_amount = l.strip().split(",")
                if chef_name == chef:
                    print(f"Date: {date}, Item: {item}, Quantity: {quantity}, Total Amount: {total_amount}")
                    total_sales += float(total_amount)
    except FileNotFoundError:
        print("Sales file not found.")
    print(f"Total sales for Chef {chef}: ${total_sales:.2f}")
    again = input("Press enter to return: ")
    if again == "":
        sales_report()


def feedback_view():
    try:
        with open("feedback.txt", "r") as file:
            print("Feedback sent by customers:")
            print(file.read())
    except FileNotFoundError:
        print("No feedback file found. No feedback to display.")
    
    # Ask if the user wants to return to the main menu
    input("Press Enter to return to the main menu...")

def updating_profile():
    n_users = input("Enter new username: ")
    n_passes = input("Enter new password: ")
    try:
        with open("users.txt", "r") as file:
            lines = file.readlines()
        updated = False
        with open("users.txt", "w") as file:
            for l in lines:
                s_users, s_passes, role = l.strip().split(",")
                if username in s_users:
                    # Update the username and password
                    file.write(f"{n_users},{n_passes},{role}\n")
                    updated = True
                else:
                    file.write(l)  # No changes, writing all the data back
        if updated:
            print("Successfully updated profile!!!")
        else:
            print("No such user found!")
    except FileNotFoundError:
        print("User file not found.")

#start of manager interface
#to add new customers
def add_customer():
    while True:
        username = input("Enter the username for the new customer: ").strip()
        password = input("Enter the password for the new customer: ").strip()
        try:
            with open("users.txt", "a") as file:
                file.write(f"{username},{password},customer\n")
            print(f"{username} is added as a customer successfully.")
        except Exception as e:
            print(f"Error adding customer: {e}")
        
        again = input("Do you want to add more customers? (yes/no): ").strip().lower()
        if again != "yes":
            break

def delete_customer():
    while True:
        print("Current customers:")
        try:
            with open("users.txt", "r") as file:
                print(f"{'Username':<20}")  # this will give the header in an aligned form
                for line in file:
                    username, _, role = line.strip().split(",")
                    if role == "customer":
                        print(f"{username:<20}")  # even spacing between words
        except FileNotFoundError:
            print("User file not found.")
        
        username = input("Enter username: ").strip()

        found = False  #check if the person exists before deleting 
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
            with open("users.txt", "w") as file:
                for l in lines:
                    s_username, s_password, s_role = l.strip().split(",")
                    if s_role == "customer":
                        if s_username == username:
                            found = True  
                            continue
                    file.write(l)  

            if found:
                print(f"Customer '{username}' has been deleted successfully.")
            else:
                print(f"Customer '{username}' does not exist.")
        except FileNotFoundError:
            print("User file not found.")
        
        again = input("Do you want to delete more customers? (yes/no): ").strip().lower()
        if again!= "yes":
            return

def edit_customer():
    while True:
        print("Current customers:")
        try:
            with open("users.txt", "r") as file:
                print(f"{'Username':<20}")  # spacing for alignment
                for line in file:
                    username, _, role = line.strip().split(",")
                    if role == "customer":
                        print(f"{username:<20}")  # spacing evenly 
        except FileNotFoundError:
            print("User file not found.")
        
        username = input("Enter the username of the customer you want to edit: ").strip()
        found = False
        u_l = []  #stores the changes
    
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()

            for l in lines:
                stored_username, stored_password, stored_role = l.strip().split(",")
                if stored_role == "customer" and stored_username == username:
                    found = True
                    print(f"Editing details for {username}:")
                    new_username = input("Enter new username: ").strip()
                    new_password = input("Enter new password: ").strip()
                    # appends the changes 
                    u_l.append(f"{new_username},{new_password},customer\n")
                    print(f"Details for {username} have been updated successfully.")
                else:
                    # appends the non changed line if no changes are made
                    u_l.append(l)

            if found:
                with open("users.txt", "w") as file:
                    file.writelines(u_l)  # writing the updated lines in file
            else:
                print(f"No customer named {username} found.")
        except FileNotFoundError:
            print("User file not found.")
        again = input("Do you want to edit more customers? (yes/no): ").strip().lower()
        if again!= "yes":
            return

def view_menu():
    menu = {}
    try:
        with open("menu.txt", "r") as file:
            for l in file:
                category, dish, price = l.strip().split(',')
                if category not in menu:
                    menu[category] = []
                menu[category].append(f"{dish}: {price}")  
    except FileNotFoundError:
        print("Menu file not found.")
        return  # exit if file not gound
    for category, dishes in menu.items():
        print(f"\n{category} Menu:")
        for dish in dishes:
            print(f"  - {dish}")

    input("\nPress Enter to return to the options menu...")  


def add_dishes():
    while True:
        menu = {}  # Dictionary to store menu categories
        try:
            # Read and store the current menu
            with open("menu.txt", "r") as file:
                for l in file:
                    category,dish,price = l.strip().split(',')
                    if category not in menu:
                        menu[category] = []
                    menu[category].append(f"{dish}: {price}")

        except FileNotFoundError:
            print("Menu file not found. A new menu will be created.")
        if menu:
            print("\nCurrent Menu:")
            for category, dishes in menu.items():
                print(f"\n{category} Menu:")
                for dish in dishes:
                    print(f"  - {dish}")

        # Take user input for new dish
        category = input("\nEnter the category of the dish you want to add: ").capitalize()
        dish = input("Enter the name of the dish you want to add: ").capitalize()
        price = input("Enter the price of the dish you want to add: ")

        # Validate price input (ensure it's a positive number)
        if not price.isdigit():
            print("Invalid price! Please enter a valid number.")
            continue

        try:
            # Append the new dish to the file
            with open("menu.txt", "a") as file:
                file.write(f"{category},{dish},{price}\n")
            print(f"Dish '{dish}' added successfully to {category} menu.")
        except Exception as e:
            print(f"Error adding dish: {e}")

        # Ask if the user wants to add another dish
        again = input("\nDo you want to add more dishes? (yes/no): ").strip().lower()
        if again != "yes":
            print("Returning to main menu...")
            return

def delete_dishes():
    while True:
        menu = {}
        try:
            with open("menu.txt", "r") as file:
                for l in file:
                    category, dish, price = l.strip().split(',')
                    if category not in menu:
                        menu[category] = []
                        menu[category].append(f"{dish}: {price}")
        except FileNotFoundError:
            print("Menu file not found.")
        for category, dishes in menu.items():
            print(f"{category} Menu:\t")
            for dish in dishes:
                print(f"{dish}")
        d= input("Enter the name of the dish you want to delete: ").strip().capitalize()
        found = False
        try:
            with open("menu.txt", "r") as file:
                lines = file.readlines()
            with open("menu.txt", "w") as file:
                for l in lines:
                    category, dish, price = l.strip().split(",")
                    if dish == d:
                        found = True
                        print(f"{dish} has been deleted successfully.")
                        continue  
                    file.write(l)
            if not found:
                print(f"The dish '{d}' was not found in the menu.")
        except FileNotFoundError:
            print("Menu file not found.")
        
        again = input("Do you want to delete more dishes? (yes/no): ").strip().lower()
        if again != "yes":
            return

def edit_menu():
    menu = {}
    while True:
        try:
            with open("menu.txt", "r") as file:
                for l in file:
                    category, dish, price = l.strip().split(',')
                    if category not in menu:
                        menu[category] = []
                    menu[category].append(f"{dish}: {price}")
        except FileNotFoundError:
            print("Menu file not found.")
        for category, dishes in menu.items():
            print(f"{category} Menu:\t")
            for dish in dishes:
                print(f"{dish}")
        print()
        d= input("Enter the name of the dish you want to edit: ").strip().capitalize()
        found = False
        updated = [] 
        try:
            with open("menu.txt", "r") as file:
                lines = file.readlines()
            for l in lines:
                category, dishes, price = l.strip().split(",")
                if d == dishes:
                    found = True
                    print(f"Editing details for {d}:")
                    category_name = input("Enter new category: ").strip().capitalize()
                    dish_name = input("Enter new name for the dish: ").strip().capitalize()
                    n_price = input("Enter new price for the dish: ").strip()
                    # adding the new details to the created updated_lines list using append() method
                    updated.append(f"{category_name},{dish_name},{n_price}\n")
                    print(f"Details for {d} has been updated successfully.")
                else:
                    # keep the unchanged data into the new empty list
                    updated.append(l)
            if found:
                with open("menu.txt", "w") as file:
                    file.writelines(updated)  
            else:
                print(f"No dish named {d} found.")
        except FileNotFoundError:
            print("Menu file not found.")
        
        again = input("Do you want to edit more dishes? (yes/no): ").strip().lower()
        if again!= "yes":
            return

#for manager to check what ingredients is needed
def ingredients():
    try:
        with open("ingredients.txt","r") as file:
            lines = file.readlines()
            print("Ingredients:")
            for l in lines:
                ingredient, quantity = l.strip().split(",")
                print(f"{ingredient}: {quantity}")
    except FileNotFoundError:
        print("Ingredients file not found.")
    input("Press Enter to return to the main menu...")

#for chef to see the orders
def view_orders():
    try:
        with open("orders.txt", "r") as file:
            lines = file.readlines()
            print("Orders:")
            for l in lines:
                o_id,c_name,dishes,q,status = l.strip().split(",")
                print(f"Order ID: {o_id}, Customer: {c_name}, Dishes: {dishes}, Quantity: {q}, Status: {status}")        
    except FileNotFoundError:
        print("Orders file not found.")
    input("Press enter to return.")
    print()
#to tell the customer their order is completed or in process
def update_order():
    while True:
        id = input("Enter the order id: ")
        update=[]
        found = False
        try:
            with open("orders.txt", "r") as file:
                lines = file.readlines()
            for l in lines:
                o_id, c_name, dishes, status = l.strip().split(",")
                if o_id == id:
                    found = True
                    n_status = input("Enter the new status: ")
                    update.append(f"{o_id},{c_name},{dishes},{n_status}\n")
                    print("Change successful")
                else:
                    update.append(l)
            if found:
                with open("orders.txt", "w") as file:
                    file.writelines(update)
            else:
                print(f"No order with order id {o_id} found.")
        except FileNotFoundError:
            print("Orders file not found.")
        
        again = input("Do you want to update another order? (yes/no): ").strip().lower()
        if again!= "yes":
            return

#request an order from the manager
def request_add():
    while True:
        ing = input("Enter the ingredient you want to request: ")
        qua = input("Enter the quantity: ")
        try:
            with open("ingredients.txt","a") as file:
                file.write(f"{ing},{qua}\n")
            print(f"Request submitted successfully.")
        except Exception as e:
            print(f"Error requesting ingredient: {e}")
        
        again = input("Do you want to request another ingredient? (yes/no): ").strip().lower()
        if again!= "yes":
            return

#already received the request then delete it
def request_del():
    try:
        with open("ingredients.txt","r") as file:
            lines = file.readlines()
            print("Ingredients:")
            for l in lines:
                ingredient, quantity = l.strip().split(",")
                print(f"{ingredient}: {quantity}")
    except FileNotFoundError:
        print("Ingredients file not found.")
    while True:
        ing = input("Enter the ingredient you want to delete: ")
        found = False
        try:
            with open("ingredients.txt", "r") as file:
                lines = file.readlines()
            update = []
            for l in lines:
                ingredient, quantity = l.strip().split(",")
                if ingredient != ing:
                    update.append(l)
                else:
                    found = True
                    print(f"{ingredient} has been deleted successfully.")
            if found:
                with open("ingredients.txt", "w") as file:
                    file.writelines(update)
            else:
                print(f"Ingredient '{ing}' not found.")
        except FileNotFoundError:
            print("Ingredients file not found.")
        
        again = input("Do you want to delete another ingredient? (yes/no): ").strip().lower()
        if again!= "yes":
            return

#if chef wants to edit their ingredient request to the manager
def request_edit():
    try:
        with open("ingredients.txt","r") as file:
            lines = file.readlines()
            print("Ingredients:")
            for l in lines:
                ingredient, quantity = l.strip().split(",")
                print(f"{ingredient}: {quantity}")
    except FileNotFoundError:
        print("Ingredients file not found.")
    while True:
        ing = input("Enter the ingredient you want to edit: ")
        found = False
        try:
            with open("ingredients.txt", "r") as file:
                lines = file.readlines()
            updated_lines = []
            for l in lines:
                ingredient, quantity = l.strip().split(",")
                if ingredient == ing:
                    found = True
                    print(f"Editing details for {ingredient}:")
                    new_quantity = input("Enter quantity: ")
                    updated_lines.append(f"{ingredient},{new_quantity}\n")
                    print(f"Details for {ingredient} have been updated successfully.")
                else:
                    updated_lines.append(l)
            if found:
                with open("ingredients.txt", "w") as file:
                    file.writelines(updated_lines)
            else:
                print(f"Ingredient '{ing}' not found.")
        except FileNotFoundError:
            print("Ingredients file not found.")
        
        again = input("Do you want to edit another ingredient request? (yes/no): ").strip().lower()
        if again!= "yes":
            return

#to place an order this function will be used
def a_order():
    while True:
        try:
            with open("orders.txt", "r") as file:
                lines = file.readlines()
                print("Orders:")
                for l in lines:
                    o_id,c_name,dishes,q,status = l.strip().split(",")
                    print(f"Order ID: {o_id}, Customer: {c_name}, Dishes: {dishes}, Quantity: {q}, Status: {status}")        
        except FileNotFoundError:
            print("Orders file not found.")
        print("Order for the above menu:")
        print()
        dishes = input("Enter the dishes you want to order: ")
        o_id = random.randint(1,999)
        q = input("Quantity: ")
        c_name = input("Enter your name: ")
        try:
            with open("orders.txt", "a") as file:
                file.write(f"\n{o_id}, {c_name}, {dishes}, {q}, in process")
            print("Order placed successfully.")
            print(f"Your order ID is: {o_id}")
            print(f"You have ordered {dishes}")
        except Exception as e:
            print(f"Error placing order: {e}")
        
        again = input("Do you want to order more? (yes/no): ").strip().lower()
        if again!= "yes":
            return
        
#if a customer doesn't want to eat the dish now this function deletes that order
def d_order():
    see_status()
    while True:
        id = input("Enter the order ID you want to delete: ")
        found = False
        try:
            with open("orders.txt", "r") as file:
                update = []
                lines = file.readlines()
                for l in lines:
                    o_id, c_name, dishes, q, status = l.strip().split(",")
                    if o_id == id:
                        found = True
                        print(f"Order ID {id} has been deleted successfully.")
                        continue
                    else:
                        update.append(l)
            if found:
                with open("orders.txt", "w") as file:
                    file.writelines(update)
            else:
                print(f"No order with order ID {id} found.")
        except FileNotFoundError:
            print("Orders file not found.")
        
        again = input("Do you want to delete another order? (yes/no): ").strip().lower()
        if again!= "yes":
            return

#this function is for customer to edit their placed orders
def e_order():
    see_status()
    while True:
        o_id = input("Enter the order ID you want to edit: ")
        n_q = input("Quantity: ")
        found = False
        try:
            with open("orders.txt", "r") as file:
                lines = file.readlines()
                update = []
                for l in lines:
                    order_id, c_name, dishes, q, status = l.strip().split(",")
                    if order_id == o_id:
                        found = True
                        print(f"Quantity changed")
                        update.append(f"{order_id},{c_name},{dishes},{n_q},{status}\n")
                        print(f"Order ID {o_id} has been updated successfully.")
                    else:
                        update.append(l)
            if found:
                with open("orders.txt", "w") as file:
                    file.writelines(update)
        except FileNotFoundError:
            print("Orders file not found.")
        
        again = input("Do you want to edit another order? (yes/no): ").strip().lower()
        if again!= "yes":
            return

#this function is for the customer to see the status of their order
def see_status():
    o_name = input("Enter your username: ")
    found = False
    try:
        with open("orders.txt", "r") as file:
            lines = file.readlines()
            for l in lines:
                order_id, c_name, dishes, q, status = l.strip().split(",")
                if username in c_name:
                    found = True
                    print(f"Order ID: {order_id}, Customer: {c_name}, Dishes: {dishes}, Quantity: {q}, Status: {status}")
        if not found:
            print(f"No order for {o_name} found.")
    except FileNotFoundError:
        print("Orders file not found.")
    input("Press enter to view main menu...")
def give_feedback():
    while True:
        feedback = input("Enter your feedback: ")
        found = False
        
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
                for l in lines:
                    s_user, s_pass, role = l.strip().split(",")
                    if role == "customer":
                        found = True
                        # Append feedback to the feedback.txt file
                        with open("feedback.txt", "a") as feedback_file:
                            feedback_file.write(f"{username}: {feedback}\n")
                        print(f"Feedback for {username} has been saved successfully!")
                        break  # Exit the loop once feedback is saved
                if not found:
                    print(f"User {username} not found. Please check your username.")
        except FileNotFoundError:
            print("Users file not found.")
        
        again = input("Do you want to give another feedback? (yes/no): ").strip().lower()
        if again != "yes":
            return 

# access to administration's options
def admin_menu():
    while True:
        print("Admin privileges:")
        print("Choose an option: ")
        print("1. Manage staff")
        print("2. View sales report based on month or by chef")
        print("3. View feedback sent by customers")
        print("4. Update profile")
        print("5. Logout\n")
        choice = input("Choose an option from 1-5: ")
        print()
        if choice == "1":
            manage_staff()
        elif choice == "2":
            sales_report()
        elif choice == "3":
            feedback_view()
        elif choice == "4":
            updating_profile()
        elif choice == "5":
            print("Logging out.....")
            time.sleep(1)
            print("Logged out!!!")
            print()
            break
        else:
            print("not in option")
            break

# access manager's options
def manager_menu():
    while True:
        print("Manager privileges:")
        print("1. Manage Customer")
        print("2. Manage menu categories and pricing")
        print("3. View ingredients list request by chef")
        print("4. Update own profile")
        print("5. Logout")
        choice = input("Choose and option form 1-5: ")
        print()
        if choice == "1":
            manage_customer()
        elif choice == "2":
            manage_menu()
        elif choice == "3":
            ingredients()
        elif choice == "4":
            updating_profile()
        elif choice == "5":
            print("Logging out.....")
            time.sleep(1)
            print("Logged out!!!")
            break
        else:
            print("Error 401!!!")
            

def manage_menu():
    while True:
        print("1. Do you want to view the menu:")
        print("2. Do you want to add a cuisine dishes and price:")
        print("3. Do you want to delete a dish:")
        print("4. Do you want to edit the menu:")
        print("5. Back\n")
        choice = input("Choose and option from 1-5: ")
        print()
        if choice == "1":
            view_menu()
        elif choice == "2":
            add_dishes()
        elif choice == "3":
            delete_dishes()
        elif choice == "4":
            edit_menu()
        elif choice == "5":
            print("Exiting manage menu...")
            time.sleep(1)
            break
        else: 
            print("not a valid choice!!")

# a function to access functions that manage staffs
def manage_staff():
    while True:
        print("Manage staff menu:- ")
        print("1. Do you want to hire a new staff member?")
        print("2. Do you want to fire a staff member?")
        print("3. Do you want to edit staff information?")
        print("4. Exit")
        choice = input("Choose an option from 1-4: ").lower()
        print()
        if choice == "1":
            hire_staff()
        elif choice == "2":
            fire_staff()
        elif choice == "3":
            edit_staff()
        elif choice == "4":
            print()
            break
        else:
            print("Something is wrong in your selection")
            print()

# a function to access functions that manage customers
def manage_customer():
    while True:
        print("Manage customer menu:- ")
        print("1. Do you want to add a customer?")
        print("2. Do you want to delete a customer?")
        print("3. Do you want to edit a customer info?")
        print("4. Exit")
        choice = input("Choose an option form 1-4: ")
        print()
        if choice == "1":
            add_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            edit_customer()
        elif choice == "4":
            print()
            break
        else: 
            print("Invalid choice!!!")
            print()

def request_ing():
    while True:
        print("Ingredient Request Menu:")
        print("1. Request ingredients")
        print("2. Delete ingredient request")
        print("3. Edit ingredient request")
        print("4. Exit")
        choice = input("Choose an option from 1-4: ")
        print()
        if choice == "1":
            request_add()
        elif choice == "2":
            request_del()
        elif choice == "3":
            request_edit()
        elif choice == "4":
            print()
            break
        else: 
            print("There is something wrong. Please check your entry again")
            print()

def chef_menu():
    while True:
        print("Chef privileges:")
        print("1. View orders ")
        print("2. Update orders as 'In process' or 'Completed'")
        print("3. Request ingredients (Add, Edit, Delete).")
        print("4. Update own profile")
        print("5. Logout")
        choice = input("Choose and option form 1-5: ")
        print()
        if choice == "1":
            view_orders()
        elif choice == "2":
            update_order()
        elif choice == "3":
            request_ing()
        elif choice == "4":
            updating_profile()  
        elif choice == "5":
            print("Logging out.....")
            time.sleep(1)
            print("Logged out!!!")
            print()
            break
        else:
            print("Not in option")
            print()

def put_order():
    while True:
        print("Order Menu:")
        print("1. Add an order")
        print("2. Delete an order")
        print("3. Edit an order")
        print("4. Exit")
        choice = input("Choose an option form 1-5: ")
        print("Choose an option form 1-4: ")
        if choice == "1":
            a_order()
        elif choice == "2":
            d_order()
        elif choice == "3":
            e_order()
        elif choice == "4":
            print()
            break
        else: 
            print("That's not correct!!!")
            print()

def customer_menu():
    while True:
        print("Customer privileges:")
        print("1. View & order food (Add, Edit, Delete) and pay to confirm.")
        print("2. View order status")
        print("3. Write  feedback to administrator")
        print("4. Update own profile")
        print("5. Logout")
        choice = input("Choose an option form 1-4: ")
        print()
        if choice == "1":
            put_order()
        elif choice == "2":
            see_status()
        elif choice == "3":
            give_feedback()
        elif choice == "4":
            updating_profile()
        elif choice == "5":
            print("Logging out.....")
            time.sleep(1)
            print("Logged out!!!")
            print()
            break
        else:
            print("Wrong choice !!!")
            print()

# this is the main block that controls flow of this program
role = login()
if role == "administrator":
    admin_menu()
elif role == "manager":
    manager_menu()
elif role == "chef":
    chef_menu()
elif role == "customer":
    customer_menu()
else: 
    print("Wrong entry!!!")