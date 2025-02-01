import random
import time
#a login function, check roles
def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    file = open("users.txt", "r")
    for l in file:
        s_user,s_pass,role = l.strip().split(",")
        if username == s_user: 
            if password == s_pass:
                print(f"Logged in successfully.\nRole: {role}")
                return role
    file.close()  
    print("Invalid username or password.")

#function to hire staff
def hire_staff():
    user = input("Enter the username for the new staff member: ").strip()
    passs = input("Enter the password for the new staff member:").strip()
    role = input("Enter the role for the new staff member: ").strip()

    file = open ("users.txt", "a")
    file.write(f"{user},{passs},{role}\n")
    file.close()
    print(f"{user} is hired as a new {role} successfully.")

#function to fire staff
def fire_staff():
    user = input("Enter the username of the staff member you want to fire: ").strip()
    file = open("users.txt", "r")
    lines = file.readlines()
    # to check if the staff is registered and trying to remove him/her
    file = open("users.txt", "w")
    for l in lines:
        found = False
        s_users, s_pass, role = l.strip().split(",")
        if s_users == user:
            found = True
            continue  #skips writing this line
        file.write(l) #writing all lines back 
        file.close()  
        if found:
            print(f"Staff member {user} has been fired.")
        else:
            print(f"Staff member {user} not found.")

def edit_staff():
    u = input("Enter the username of the staff member you want to edit: ").strip()
    file= open ( "users.txt", "r" )
    lines = file.readlines()
    found = False
    update = [] #to store changes
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
        file=open("users.txt", "w")
        file.writelines(update)
        file.close()
    else:
        print(f"Staff member '{u}' not found.")

def sales_report():
    print("Choose a criteria to view the sales report:")
    print("1. By Month")
    print("2. By Chef")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        sales_by_month()
    elif choice == "2":
        sales_by_chef()
    else:
        print("choose a valid option!!")

def sales_by_month():
    month = input("Enter the date in this format -> (YYYY-MM): ").strip()
    t_s = 0
    found = False 
    print(f"Sales report for {month}:")
    with open("sales.txt", "r") as file:
        for l in file:
            date, chef, item, quantity, price, t_a = l.strip().split(",")
            if date.startswith(month):
                found = True  
                print(f"Date: {date}, Chef: {chef}, Item: {item}, Quantity: {quantity}, Total Amount: {float(t_a)}")
                t_s += float(t_a)
    if found:
        print(f"Total sales for {month}: ${t_s:.2f}")
    else:
        print(f"No sales during {month}.")

def sales_by_chef():
    chef = input("Enter the chef name: ").strip()
    total_sales = 0
    print(f"Sales report for Chef: {chef}")
    with open("sales.txt", "r") as file:
        for l in file:
            date, chef_name, item, quantity, price, total_amount = l.strip().split(",")
            if chef_name == chef:
                print(f"Date: {date}, Item: {item}, Quantity: {quantity}, Total Amount: {total_amount}")
                total_sales += float(total_amount)
    print(f"Total sales for Chef {chef}: ${total_sales:.2f}")

def feedback_view():
    try:
        file = open("feedback.txt", "r")
        print("Feedback sent by customers:")
        print(file.read())
    except FileNotFoundError:
        print("No feedback file found. No feedback to display.")

def updating_profile():
    file = open("users.txt", "r")
    lines = file.readlines()
    u_users = input("Enter your current username: ")
    n_users = input("Enter new username: ")
    n_passes = input("Enter new password: ")
    updated = False
    file = open("users.txt", "w")
    for l in lines:
        s_users, s_passes, role = l.strip().split(",")
        if s_users == u_users:
        #writing changes into file
            file.write(f"{n_users},{n_passes},{role}\n")
            updated = True
        else:
            file.write(l) #no changes, writing all the data back
        if updated:
            print("successfully updated profile!!!")
        else:
            print("No such user found!")

#start of manager interface
#to add new customers
def add_customer():
    username = input("Enter the username for the new customer: ").strip()
    password = input("Enter the password for the new customer: ").strip()
    file = open("users.txt", "a")
    file.write(f"{username},{password},customer\n")
    print(f"{username} is add as a customer successfully.")

def delete_customer():
    username = input("Enter username: ").strip()
    file = open("users.txt","r")
    lines = file.readlines()
    found = False  #check if the person exits before deleteing 
    file= open("users.txt","w")
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

def edit_customer():
    username = input("Enter the username of the customer you want to edit: ").strip()
    file = open("users.txt", "r")
    lines = file.readlines()
    found = False
    u_l = [] #empty list to store changed data
    for l in lines:
        stored_username, stored_password, stored_role = l.strip().split(",")
        if stored_role =="customer":
            if stored_username == username:
                found = True
                print(f"Editing details for {username}:")
                new_username = input("Enter new username: ").strip()
                new_password = input("Enter new password: ").strip()
                #writing changes in to u_l(list for changes)
                u_l.append(f"{new_username},{new_password},customer\n")
                print(f"Details for {username} have been updated successfully.")
            else:
                #no changes
                u_l.append(l)
    file.close()
    if found:
        file = open("users.txt", "r")
        file.writelines(u_l) #write the changes back to file
        file.close()  
    else:
        print(f"No customer named {username} found.")

def view_menu():
    menu = {}
    file = open("menu.txt", "r")
    for l in file:
        category, dish, price = l.strip().split(',')
        if category not in menu:
            menu[category] = []
        menu[category].append(f"{dish}: {price}")
    file.close()
    for category, dishes in menu.items():
        print(f"{category} Menu:\t")
        for dish in dishes:
            print(f"{dish}")
    return

def add_dishes():
    category = input("Enter the category of the dish you want to add: ")
    dish = input("Enter the name of the dish you want to add: ")
    price = input("Enter the price of the dish you want to add: ")
    file = open("menu.txt", "a")
    file.write(f"{category},{dish},{price}\n")
    print(f"Dish added successfully to the menu.")
    file.close()
    return 

def delete_dishes():
    d= input("Enter the name of the dish you want to delete: ").strip()
    found = False
    file = open("menu.txt", "r")
    lines = file.readlines()
    file= open("menu.txt", "w")
    for l in lines:
        category, dish, price = l.strip().split(",")
        if dish == d:
            found = True
            print(f"{dish} has been deleted successfully.")
            continue  
        file.write(l)
    if not found:
        print(f"The dish '{d}' was not found in the menu.")

def edit_menu():
    d= input("Enter the name of the dish you want to edit: ").strip()
    found = False
    file = open("menu.txt", "r")
    lines = file.readlines()
    updated = [] 
    for l in lines:
        category, dishes, price = l.strip().split(",")
        if d == dishes:
            found = True
            print(f"Editing details for {d}:")
            category_name = input("Enter new category: ").strip()
            dish_name = input("Enter new name for the dish: ").strip()
            n_price = input("Enter new price for the dish: ").strip()
            # adding the new details to the created updated_lines list using append() method
            updated.append(f"{category_name},{dish_name},{n_price}\n")
            print(f"Details for {d} has been updated successfully.")
        else:
            # keep the unchanged data into the new empty list
            updated.append(l)
    file.close()
    # updates when the entered dish found
    if found:
        file = open("menu.txt", "r")
        # new data stored
        file.writelines(updated)
        file.close()  
    else:
        print(f"No dish named {d} found.")


#for manager to check what ingredients is needed
def ingredients():
    file = open("ingredients.txt","r")
    lines = file.readlines()
    stored_ingredients, quantity = lines[0].strip().split(",")
    print("Ingredients:")
    for l in lines:
        ingredient, quantity = l.strip().split(",")
        print(f"{ingredient}: {quantity}")
    return

#for chef to see the orders
def view_orders():
    file = open("orders.txt", "r")
    lines = file.readlines()
    print("Orders:")
    for l in lines:
        o_id, c_name, dishes,status= l.strip().split(",")
        print(f"Order ID: {o_id}, Customer: {c_name}, Dishes: {dishes}, Status: {status}")        

#to tell the customer their order is completed or in process
def update_order():
    id = input("Enter the order id: ")
    update=[]
    found = False
    file = open("orders.txt", "r")
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
        file = open("orders.txt", "w")
        file.writelines(update)
        file.close()  
    else:
        print(f"No order with order id {o_id} found.")

#request an order form the manager
def request_add():
    ing = input("Enter the ingredient you want to request: ")
    qua = input("Enter the quantity: ")
    file = open("ingredients.txt","a")
    file.write(f"{ing},{qua}\n")
    print(f"Request submitted successfully.")
    file.close()
    return 

#already received the request then delete it
def request_del():
    ing = input("Enter the ingredient you want to delete: ")
    found = False
    file = open("ingredients.txt", "r")
    lines = file.readlines()
    update = []
    for l in lines:
        ingredient, quantity = l.strip().split(",")
        if ingredient!= ing:
            update.append(l)
        else:
            found = True
            print(f"{ingredient} has been deleted successfully.")
    file.close()
    if found:
        file = open("ingredients.txt", "w")
        file.writelines(update)
        file.close()
    else:
        print(f"Ingredient '{ing}' not found.")

#if chef wants to edit their ingredient request to the manager
def request_edit():
    ing = input("Enter the ingredient you want to edit: ")
    found = False
    file = open("ingredients.txt", "r")
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
    file.close()
    if found:
        file = open("ingredients.txt", "w")
        file.writelines(updated_lines)
        file.close()
    else:
        print(f"Ingredient '{ing}' not found.")

#to place an order this function will be used
def a_order():
    view_menu()
    dishes = input("Enter the dishes you want to order: ")
    o_id = random.randint(1,999)
    q = input("Quantity: ")
    c_name = input("Enter your name: ")
    file = open("orders.txt", "a")
    file.write(f"\n{o_id}, {c_name}, {dishes}, {q}, in process")
    print("Order placed successfully.")
    print(f"Your order ID is: {o_id}")
    print(f"You have ordered {dishes}")

#if a customer doesnt want to eat the dish now this function deletes that order
def d_order():
    id = input("Enter the order ID you want to delete: ")
    found = False
    file = open("orders.txt", "r")
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
    file.close()
    if found:
        file = open("orders.txt", "w")
        file.writelines(update)
        file.close()
    else:
        print(f"No order with order ID {id} found.")

#this function is for customer to edit their placed orders
def e_order():
    o_id = input("Enter the order ID you want to edit: ")
    n_q = input("Quantity: ")
    found = False
    file = open("orders.txt", "r")
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
    file.close()
    if found:
        file = open("orders.txt", "w")
        file.writelines(update)
        file.close()

#this function is for the customer to see the status of their order
def see_status():
    o_id = input("Enter the order ID: ")
    found = False
    file = open("orders.txt", "r")
    lines = file.readlines()
    for l in lines:
        order_id, c_name, dishes, q, status = l.strip().split(",")
        if order_id == o_id:
            found = True
            print(f"Order ID: {order_id}, Customer: {c_name}, Dishes: {dishes}, Quantity: {q}, Status: {status}")
            break
    if not found:
        print(f"No order with order ID {o_id} found.")

def give_feedback():
    o_id = input("Enter the order ID: ")
    feedback = input("Enter your feedback: ")
    found = False
    file = open("orders.txt", "r")
    lines = file.readlines()
    for l in lines:
        order_id, c_name, dishes, q, status = l.strip().split(",")
        if order_id == o_id:
            found = True
            file = open("feedback.txt", "w")
            file.write(f"{o_id}: {feedback}")

# access to administration's options
def admin_menu():
    print("Admin privileges:")
    print("Choose an option:")
    print("1. Manage staff")
    print("2. View sales report based on month or by chef")
    print("3. View feedback sent by customers")
    print("4. Update profile")
    print("5. Logout")

    choice = input("Enter your choice: ")
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
        time.sleep(3)
        print("Logged out!!!")
    else:
        print("not in option")

# access manager's options
def manager_menu():
    print("Manager privileges:")
    print("1. Manage Customer")
    print("2. Manage menu categories and pricing")
    print("3. View ingredients list request by chef")
    print("4. Update own profile")
    choice = input("Enter your choice: ")
    if choice == "1":
        manage_customer()
    elif choice == "2":
        manage_menu()
    elif choice == "3":
        ingredients()
    elif choice == "4":
        updating_profile()
    else:
        print("Error 401!!!")

def manage_menu():
    print("1. Do you want to view the menu:")
    print("2. Do you want to add a cuisine dishes and price:")
    print("3. Do you want to delete a dishe:")
    print("4. Do you want to edit the menu:")
    choice = input("Enter a choice form 1 to 4: ")
    if choice == "1":
        view_menu()
    elif choice == "2":
        add_dishes()
    elif choice == "3":
        delete_dishes()
    elif choice == "4":
        edit_menu()
    else: print("not a valid choice!!")

# a function to access functions that manage staffs
def manage_staff():
    choice = input("Do you want to hire ,fire or edit staff?: ").lower()
    if choice == "hire":
            hire_staff()
    elif choice == "fire":
        fire_staff()
    elif choice == "edit":
            edit_staff()
    else:
        print("Something is wrong. Please use 'hire', 'fire' or 'edit'.")

# a function to access functions that manage customers
def manage_customer():
    print("Do you want to add, delete, or edit a customer?")
    choice = input()
    if choice == "add":
        add_customer()
    elif choice == "delete":
        delete_customer()
    else: edit_customer()

def request_ing():
    choice = input("Do you want to add, delete, or edit: ")
    if choice == "add":
        request_add()
    elif choice == "delete":
        request_del()
    elif choice == "edit":
        request_edit()
    else: print("There is something wrong. Please check your entry again")

def chef_menu():
    print("Chef privileges:")
    print("1. View orders ")
    print("2. Update orders as 'In process' or 'Completed'")
    print("3. Request ingredients (Add, Edit, Delete).")
    print("4. Update own profile")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_orders()
    elif choice == "2":
        update_order()
    elif choice == "3":
        request_ing()
    elif choice == "4":
        updating_profile()  
    else:
        print("Not in option")

def put_order():
    choice = input("Do you want to add, delete or edit your order: ")
    if choice == "add":
        a_order()
    elif choice == "delete":
        d_order()
    elif choice == "edit":
        e_order()
    else : print("Thats not correct!!!")

def customer_menu():
    print("Customer privileges:")
    print("1. View & order food (Add, Edit, Delete) and pay to confirm.")
    print("2. View order status")
    print("3. Send feedback to administrator")
    print("4. Update own profile")
    choice = input("Enter your choice: ")
    if choice == "1":
        put_order()
    elif choice == "2":
        see_status()
    elif choice == "3":
            give_feedback()
    elif choice == "4":
        updating_profile()
    else:
            print("Wrong choice !!!")

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
else: print("Wrong entery!!!")