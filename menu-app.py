import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the Firebase Admin SDK
cred = credentials.Certificate("menu-driven-database-app-firebase-adminsdk-1cju4-19588f5284.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://menu-driven-database-app-default-rtdb.firebaseio.com/'
})

# Get a reference to the Firebase Realtime Database
ref = db.reference()

# Create a row in the table.
def create_row(current_table):
    name=input("Name: ")
    age=input('Age: ')
    email=input('Email: ')
    data = {
        'age': int(age),
        'email': email,
        'name': name
            }
    
    current_table_ref = ref.child(current_table)
    current_table_ref.push(data)
    print("Row added successfully.")

# Get the rows from the table
def get_rows(table_name):
    rows = []
    for child in ref.child(table_name).get().items():
        row_id, row_data = child
        rows.append((row_id, row_data))
    return rows

# List out the rows from the database.
def list_rows(table_name):
    rows = get_rows(table_name)
    print(f"{'ID':<25}{'Name':<20}{'Age':<10}{'Email':<30}")
    for row_id, row_data in rows:
        name = row_data.get('name', '')
        age = row_data.get('age', '')
        email = row_data.get('email', '')
        print(f"{row_id:<25}{name:<20}{age:<10}{email:<30}")

# Update a row in the specified table
def update_row(current_table):
    row_id = input("Enter the ID of the row to update: ")
    name = input("New name: ")
    age = input("New age: ")
    email = input("New email: ")
    data = {
        "name": name,
        "age": int(age),
        "email": email
    }
    current_table_ref = ref.child(current_table)
    current_table_ref.child(row_id).update(data)
    print("Row updated successfully.")

# Delete a row from the specified table
def delete_row(current_table):
    row_id = input("Enter the ID of the row to delete: ")
    current_table_ref = ref.child(current_table)
    current_table_ref.child(row_id).delete()
    print("Row deleted successfully.")

# Menu for interacting with the database.
while True:
    current_table="users"
    print("\nMenu:")
    print("\nWhat would you like to do?")
    print("1. Create row")
    print("2. Update row")
    print("3. Delete row")
    print("4. List rows")
    print("0. exit")

    choice = input(">")

    if choice == "1":
        create_row(current_table)
    elif choice == "2":
        update_row(current_table)
    elif choice == "3":
        delete_row(current_table)
    elif choice == "4":
        list_rows(current_table)
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")