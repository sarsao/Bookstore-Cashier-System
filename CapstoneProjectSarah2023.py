from tabulate import tabulate
import datetime

# Data Dummy Customer
allcustomers = [
    {'Customer_ID': 1001, 'name': 'John Smith', 'email': 'johns@gmail.com', 'total_amount': 50000, 'registered_date':'2021-05-27'},
    {'Customer_ID': 1002, 'name': 'Alice Johnson', 'email': 'alice23@gmail.com', 'total_amount': 80000, 'registered_date' :'2022-03-01'},
    {'Customer_ID': 1003, 'name': 'Bob Williams', 'email': 'bobiwil@gmail.com', 'total_amount': 39990, 'registered_date' :'2019-05-05'},
    {'Customer_ID': 1004, 'name': 'Eva Davis', 'email': 'evadaves123@gmail.com', 'total_amount': 45000, 'registered_date' :'2020-03-21'},
    {'Customer_ID': 1005, 'name': 'Mike Brown', 'email': 'mikesbrownm@gmail.com', 'total_amount': 129000, 'registered_date' :'2022-10-14'},
    {'Customer_ID': 1006, 'name': 'Asuka Kazama', 'email': 'asoeka@gmail.com', 'total_amount': 50000, 'registered_date' :'2022-08-23'},
    {'Customer_ID': 1007, 'name': 'Bobby Tabuti', 'email': 'bob01@gmail.com', 'total_amount': 834500, 'registered_date' :'2019-05-24'},
    {'Customer_ID': 1008, 'name': 'Hworang', 'email': 'hworang34@gmail.com', 'total_amount': 234191, 'registered_date' :'2022-10-10'},
    {'Customer_ID': 1009, 'name': 'Anna Antuma', 'email': 'annaantuman@gmail.com', 'total_amount': 162791, 'registered_date' :'2021-08-20'},
    {'Customer_ID': 1010, 'name': 'Suwarno', 'email': 'soewarno_id@gmail.com', 'total_amount': 545678, 'registered_date' :'2021-09-19'},
    {'Customer_ID': 1011, 'name': 'Subroto Agus', 'email': 'agussubroto98@gmail.com', 'total_amount': 5728190, 'registered_date' :'2022-04-03'},
    {'Customer_ID': 1012, 'name': 'Purnomo Koncosworo', 'email': 'punromokonco.sw@gmail.com', 'total_amount': 3400000, 'registered_date' :'2022-02-12'},
    {'Customer_ID': 1013, 'name': 'Doddy Surdajat', 'email': 'doddy.s@gmail.com', 'total_amount': 5000000, 'registered_date' :'2022-05-04'},
    {'Customer_ID': 1014, 'name': 'Mya Lopez', 'email': 'myamyamya@gmail.com', 'total_amount': 624500, 'registered_date' :'2022-12-12'},
    {'Customer_ID': 1015, 'name': 'Rifqi Fadhila', 'email': 'rifqifad@gmail.com', 'total_amount': 900000, 'registered_date' :'2023-06-19'},
    {'Customer_ID': 1016, 'name': 'Wilya Putri', 'email': 'wilyayahya@gmail.com', 'total_amount': 670100, 'registered_date' :'2023-05-21'},
    {'Customer_ID': 1017, 'name': 'Alisia Johnson', 'email': 'johnson.alice@gmail.com', 'total_amount': 850000, 'registered_date' :'2023-07-10'},
    {'Customer_ID': 1018, 'name': 'Aca Williams', 'email': 'willacawill@gmail.com', 'total_amount': 33400, 'registered_date' :'2023-01-18'},
    {'Customer_ID': 1019, 'name': 'Asilia Dinda', 'email': 'asiliadinda@gmail.com', 'total_amount': 450000, 'registered_date' :'2022-04-22'},
    {'Customer_ID': 1020, 'name': 'Muliono Suratno', 'email': 'soeratno@gmail.com', 'total_amount': 56000, 'registered_date' :'2023-05-16'},
    {'Customer_ID': 1021, 'name': 'Kaswara Montez', 'email': 'montezkaz@gmail.com', 'total_amount': 350300, 'registered_date' :'2023-08-01'},
    {'Customer_ID': 1022, 'name': 'Cindy Johnson', 'email': 'johnsonevans@gmail.com', 'total_amount': 240000, 'registered_date' :'2021-07-18'},
    {'Customer_ID': 1023, 'name': 'Kaila Rahayu', 'email': 'kailarahayu@gmail.com', 'total_amount': 9050600, 'registered_date' :'2023-04-21'},
    {'Customer_ID': 1024, 'name': 'Emily Davis', 'email': 'emilydavist@gmail.com', 'total_amount': 60000, 'registered_date' :'2023-03-29'},
    {'Customer_ID': 1025, 'name': 'Triputra Bagus', 'email': 'triputracbagus@gmail.com', 'total_amount': 8178900, 'registered_date' :'2023-09-30'}
]

# Main Menu Options
menu_options = (
    "View Customer Data",
    "Create New Customer",
    "Update Existing Customer",
    "Delete Customer Data",
    "Show Data Analytics (Top 5 Buyers)",
    "Exit"
)

# Function to see all customer data
def view_customer_data():
    table_data = []

    for customer in allcustomers:
        row = [customer['Customer_ID'], customer['name'], customer['email'], customer['total_amount'], customer['registered_date']]
        table_data.append(row)

    data_headers = ["Customer ID", "Name", "Email", "Total Amount", "Registered Date"]
    print(tabulate(table_data, headers=data_headers, tablefmt="grid"))

def print_customer_details_table(customer):
    table_data = [
        ["Customer ID", customer['Customer_ID']],
        ["Name", customer['name']],
        ["Email", customer['email']],
        ["Total Amount", customer['total_amount']],
        ["Registered Date", customer['registered_date']],
    ]

    headers = []
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Function to find customer in allcustomer data
def find_and_print_customer(allcustomers, find_customer_id):
    found = False

    for customer in allcustomers:
        if customer['Customer_ID'] == find_customer_id:
            print_customer_details_table(customer)
            found = True
            break

    return found

def find_customer():
    find_customer_id = int(input("Enter Customer ID to find: "))
    found = find_and_print_customer(allcustomers, find_customer_id)

    if not found:
        print("Customer not found.")
        backmenu = input("Do You Want To Go Back? (yes/no): ").lower()
        if backmenu != "yes":
            print("Exiting the program.")

# Function to ask the user if they want to go back to the main menu or not
def goback_menu():
    user_input = input("Do you want to go back to the main menu? (yes/no): ").lower()
    if user_input != "yes":
        confirm_exit = input("Are you sure you don't want to go back to the main menu? (yes/no): ").lower()
        while confirm_exit != "yes" and confirm_exit != "no":
            print("Invalid input. Please enter 'yes' or 'no'.")
            confirm_exit = input("Are you sure you don't want to go back to the main menu? (yes/no): ").lower()

        if confirm_exit == "yes":
            print("Exiting the program.")
            exit()  
        else:
            print("Back to Main Menu.")

# Function to make a submenu for view and find customer data
def menu_view():
    while True:
        print("1. View All Customer Data")
        print("2. Find Customer Data")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            view_customer_data()
        elif choice == '2':
            find_customer()  
        elif choice == '3':
            goback_menu()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


# Empty customer list to append / add more customer data
customers = []

# Function to generate new customer ID / Unique ID
def customer_counter(counter):
    customer_id = counter
    counter += 1
    return customer_id, counter

# Customer ID / Unique ID starts continue number from the last unique ID data dummy 
customer_counter_value = 1026

# Function to create a new customer
def create_new_customer():
    global customer_counter_value
    customer_id, customer_counter_value = customer_counter(customer_counter_value)  # Generate a unique customer ID
    name = input("Enter Customer Name: ")
    email = input("Enter Customer Email: ")
    total_amount = int(input("Enter Total Amount: "))
    registered_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Add a timestamp

    allcustomers.append({
        'Customer_ID': customer_id,
        'name': name,
        'email': email,
        'total_amount': total_amount,
        'registered_date': registered_date
    })

    print("New customer created successfully.")

# Function to make a submenu for action to create a new customer
def third_view():
    while True:
        print("1. Create New Customer Data")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            create_new_customer()
        elif choice == '2':
            goback_menu()  
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

# Function to update existing customer data
def update_existing_customer():
    customer_id = input("Enter the Customer ID to update: ")
    for customer in allcustomers:
        if str(customer['Customer_ID']) == customer_id:
            # Update customer information
            customer['name'] = input("Enter the new name: ")
            customer['email'] = input("Enter the new email: ")
            customer['total_amount'] = int(input("Enter the new total amount: "))
            
            # Input the registration date as a string and convert it to the desired format
            new_registered_date = input("Enter the Year-Month-Date of the registration date (YYYY-MM-DD): ")
            customer['registered_date'] = datetime.datetime.strptime(new_registered_date, "%Y-%m-%d").strftime("%Y-%m-%d")
            
            print("Customer data updated successfully.")
            return
    print("Customer not found.")

# Function to make a submenu for action to update customer data
def fourth_view():
    while True:
        print("1. Update New Customer Data")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            update_existing_customer()
        elif choice == '2':
            goback_menu() 
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

# Function to delete existing customer data
def delete_customer_data():
    customer_id = input("Enter the Customer ID to delete: ")
    for customer in allcustomers.copy():
        if str(customer['Customer_ID']) == customer_id:
            allcustomers.remove(customer)
            print("Customer data deleted successfully.")
            return
    print("Customer not found.")

def fifth_view():
    while True:
        print("1. Delete Customer Data")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            delete_customer_data()
        elif choice == '2':
            goback_menu() 
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

# Function to show top 5 customer 
def show_data_analytics():
    sorted_customers = sorted(allcustomers, key=lambda x: x['total_amount'], reverse=True)[:5]

    table_data = []
    for customer in sorted_customers:
        row = [customer['Customer_ID'], customer['name'], customer['email'], customer['total_amount'], customer['registered_date']]
        table_data.append(row)

    data_headers = ["Customer ID", "Name", "Email", "Total Amount", "Registered Date"]
    print(tabulate(table_data, headers=data_headers, tablefmt="grid"))

# Function to make a submenu for action to show analytics (top 5 buyers)
def sixth_view():
    while True:
        print("1. Show Data Analytics (Top 5 Buyers)")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            show_data_analytics()
        elif choice == '2':
            goback_menu()  
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")


# Loop function
while True:
    print("\nMain Menu:")
    for i, option in enumerate(menu_options, start=1):
        print(f"{i}. {option}")

    # User input interaction  
    while True:
        choice = input("Please enter the number corresponding to your choice (1-6): ")
        if choice.isdigit() and 1 <= int(choice) <= 6:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

    if choice == "1":
        menu_view()  
    elif choice == "2":
        third_view()
    elif choice == "3":
        fourth_view()
    elif choice == "4":
        fifth_view()
    elif choice == "5":
        sixth_view()  
    elif choice == "6":
        print("Exiting the program.")
        break  
    
    if choice == "6":
        break