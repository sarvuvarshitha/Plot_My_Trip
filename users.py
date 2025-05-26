# Database for storing users (login credentials) and additional user details
users_db = {
    "customers": {"john": "pass123", "alice": "mypassword"},
    "employees": {"admin": "admin123"}
}

user_details_db = {
    "customers": {
        "john": {"full_name": "John Doe", "email": "john@example.com", "phone": "1234567890"},
        "alice": {"full_name": "Alice Smith", "email": "alice@example.com", "phone": "9876543210"}
    },
    "employees": {
        "admin": {"full_name": "Admin User", "email": "admin@example.com", "phone": "1122334455"}
    }
}

def register_user(user_type):
    """Register a new user and ask for additional details."""
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    if username in users_db[user_type]:
        print(f"User {username} already exists in {user_type}.")
    else:
        # Register user and add credentials
        users_db[user_type][username] = password

        # Ask for additional details
        print(f"User {username} registered successfully!")
        full_name = input("Enter your full name: ")
        email = input("Enter your email address: ")
        phone = input("Enter your phone number: ")

        # Store the additional details in the user_details_db
        user_details_db[user_type][username] = {
            "full_name": full_name,
            "email": email,
            "phone": phone
        }
        print(f"Profile details for {username} saved successfully!")

def display_user_details(user_type, username):
    """Display user details."""
    if username in user_details_db[user_type]:
        details = user_details_db[user_type][username]
        print("\n--- User Details ---")
        print(f"Full Name: {details['full_name']}")
        print(f"Email: {details['email']}")
        print(f"Phone: {details['phone']}")
    else:
        print(f"No details found for {username}.")

def login():
    print("\n--- Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Check if the user is a customer or employee
    for user_type, users in users_db.items():
        if username in users:
            if users[username] == password:
                print(f"Login successful! You are logged in as {user_type.capitalize()}.")
                display_user_details(user_type, username)  # Show user details after login
                return user_type, username
            else:
                print("Invalid password! Please try again.")
                return None, None

    # If username is not found, prompt for registration
    print(f"Username {username} not found. Would you like to register?")
    choice = input("Enter 'yes' to register or 'no' to exit: ").lower()
    if choice == 'yes':
        # Ask if the user is a customer or employee for registration
        user_type = input("Are you a customer or employee? ").lower()
        if user_type in users_db:
            register_user(user_type)
        else:
            print("Invalid user type. Please try again.")
    return None, None
