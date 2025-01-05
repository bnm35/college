#creating a login interface to know the users' role
def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    try:
        # Open the file and read the data
        with open("credentials.txt", "r") as file:
            for line in file:
                # Split the line into components
                stored_username, stored_password, role = line.strip().split(",")
                
                # Check if the username matches
                if username == stored_username:
                    # If the username matches, check the password
                    if password == stored_password:
                        print(f"Login successful! Role: {role}")
                        return role
                    else:
                        # Password is incorrect, stop further checks
                        print("Incorrect password.")
                        return None

        # If no username matches after checking all lines
        print("Invalid username.")
        return None

    except FileNotFoundError:
        print("The file 'credentials.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


#function to hire staff
def hire_staff():
    print("Enter the username for the new staff member:")
    username = input("Enter username: ").strip()
    print("Enter the password for the new staff member:")
    password = input("Enter password: ").strip()
    print("Enter the role of the new staff: ")
    role = input("Enter role: ").strip()

    with open("credentials.txt", "a") as file:
        file.write(f"{username},{password},{role}\n")
        print(f"{username} is hired as a new {role} successfully.")

#function to fire staff
def fire_staff():
    print("Enter the username of the staff member you want to fire:")
    username = input("Enter username: ").strip()
    # read the data from the present file
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
    # to check if the staff is registered and trying to remove him/her
    with open("credentials.txt", "w") as file:
        staff_found = False
        for line in lines:
            stored_username, stored_password, role = line.strip().split(",")
            if stored_username == username and role == "staff":
                staff_found = True
                continue  # removing the staff
            # writing the other unchanged staff back into the file
            file.write(line)  
        if staff_found:
            print(f"Staff member {username} has been fired.")
        else:
            print(f"Staff member {username} not found.")

def edit_staff():
    username = input("Enter the username of the staff member you want to edit: ").strip()
    # reading data form the given file
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
    staff_found = False
    updated_lines = [] # creating a list to store the new updated data
    # editing the data of the staff you want
    for line in lines:
        stored_username, stored_password, stored_role = line.strip().split(",")
        # checking if the entered username and the username in the file are the same
        if stored_username == username:
            staff_found = True
            print(f"Editing details for {username}:")
            new_username = input("Enter new username: ").strip()
            new_password = input("Enter new password: ").strip()
            new_role = input("Enter new role (e.g., manager, chef): ").strip()
            # adding the new details to the created updated_lines list using append() method
            updated_lines.append(f"{new_username},{new_password},{new_role}\n")
            print(f"Details for {username} have been updated successfully.")
        else:
            # keeping the line as it is in the updated_lines list
            updated_lines.append(line)

    # updating the file when the staff is found
    if staff_found:
        with open("credentials.txt", "w") as file:
            file.writelines(updated_lines)  # storing the new updated data into the file 
    else:
        print(f"Staff member '{username}' not found.")
    if not staff_found:
        print(f"Staff member '{username}' not found.")

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
        print("Invalid choice. Please enter a valid option.")

def sales_by_month():
    month = input("Enter the month (YYYY-MM): ").strip()
    total_sales = 0
    print(f"Sales report for {month}:")
    with open("sales.txt", "r") as file:
        for line in file:
            date, chef, item, quantity, price, total_amount = line.strip().split(",")
            if date.startswith(month):
                print(f"Date: {date}, Chef: {chef}, Item: {item}, Quantity: {quantity}, Total Amount: {total_amount}")
                total_sales += float(total_amount)
    print(f"Total sales for {month}: ${total_sales:.2f}")

def sales_by_chef():
    chef = input("Enter the chef name: ").strip()
    total_sales = 0
    print(f"Sales report for Chef: {chef}")
    with open("sales.txt", "r") as file:
        for line in file:
            date, chef_name, item, quantity, price, total_amount = line.strip().split(",")
            if chef_name == chef:
                print(f"Date: {date}, Item: {item}, Quantity: {quantity}, Total Amount: {total_amount}")
                total_sales += float(total_amount)
    print(f"Total sales for Chef {chef}: ${total_sales:.2f}")

def feedback_view():
    try:
        with open("feedback.txt", "r") as file:
            print("Feedback sent by customers:")
            print(file.read())
    except FileNotFoundError:
        print("No feedback file found. No feedback to display.")

# def updating_profile():


#starting of manager interface
#adding new customer into the credentials file
def add_customer():
    username = input("Enter the username for the new customer: ").strip()
    password = input("Enter the password for the new customer: ").strip()
    
    with open("credentials.txt", "a") as file:
        file.write(f"{username},{password},'customer'\n")
        print(f"{username} is add as a customer successfully.")

def delete_customer():
    username = input("Enter username: ").strip()
    # reading the data from the current file
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
    user_found = False  # checking if the user exists 
    # writing data back  into the file
    with open("credentials.txt", "w") as file:
        for line in lines:
            stored_username, stored_password, stored_role = line.strip().split(",")
            if stored_username == username:
                # the user found and skiped writting it back into the file
                user_found = True  
                continue
            # writing the other data which were not skipped into the file again
            file.write(line)  

    if user_found:
        print(f"Customer '{username}' has been deleted successfully.")
    else:
        print(f"Customer '{username}' does not exist.")

def edit_customer():
    username = input("Enter the username of the staff member you want to edit: ").strip()
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
    staff_found = False
    # creating a list to store the new updated data
    updated_lines = [] 
    for line in lines:
        stored_username, stored_password, stored_role = line.strip().split(",")
        # checking if the entered username and the username in the file are the same
        if stored_username == username:
            staff_found = True
            print(f"Editing details for {username}:")
            new_username = input("Enter new username: ").strip()
            new_password = input("Enter new password: ").strip()
            # adding the new details to the created updated_lines list using append() method
            updated_lines.append(f"{new_username},{new_password},'customer'\n")
            print(f"Details for {username} have been updated successfully.")
        else:
            # keeping the line as it is in the updated_lines list
            updated_lines.append(line)
    # updating the file when the staff is found
    if staff_found:
        with open("credentials.txt", "w") as file:
            # storing the new updated data into the file 
            file.writelines(updated_lines)  
    else:
        print(f"Staff member '{username}' not found.")
    if not staff_found:
        print(f"Staff member '{username}' not found.")

def view_menu():
    with open ("menu.txt", "r") as file:
        lines = file.readlines()
        stored_menu, _ = lines[0].strip().split(",")
        print("Menu:")
        for line in lines:
            item, price = line.strip().split(",")
            print(f"  - {item}: ${price}")
        return

# a function that displays the ingredients for managers
def ingredients():
    with open("ingredients.txt", "r") as file:
        lines = file.readlines()
        stored_ingredients, quantity = lines[0].strip().split(",")
        print("Ingredients list:")
        for line in lines:
            ingredient, quantity = line.strip().split(",")
            print(f"  - {ingredient}: {quantity}")
        return

# a function to access the privileges of an admin
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
        print("Logging out")
    else:
        print("Invalid choice. Try again.")

# a function to access the privileges of a manager
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
        print("Invalid choice. Try again.")

def manage_menu():
    print("1.Do you want to view the menu:")
    print("2. Do you want to add a cuisine dishes and price:")
    print("3. Do you want to add a new dishes:")
    print("4. Do you want to delete a dishes:")
    print("5. Do you want to edit the menu:")
    choice = input("Enter a choice form 1 to 5: ")
    if choice == "1":
        view_menu()
    elif choice == "2":
        add_menu_item()
    elif choice == "3":
        add_dishes()
    elif choice == "4":
        delete_dishes()
    elif choice == "5":
        edit_menu()
    else: print("Invalid choice. Please enter a valid option")

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
        print("Invalid option. Please enter 'hire', 'fire' or 'edit'.")

# a function to access functions that manage customers
def manage_customer():
    print("Do you want to add, delete, or edit a customer?")
    choice = input()
    if choice == "add":
        add_customer()
    elif choice == "delete":
        delete_customer()
    else: edit_customer()

# the main program that controls the flow of the whole system
role = login()
if role == "administration":
    admin_menu()
elif role == "manager":
    manager_menu()
else: print("Invalid entry.")

