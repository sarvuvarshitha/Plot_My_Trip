from users import login
from trips import TripPlanner, my_trips

def main():
    print("Welcome to MakeMyTrip!")
    planner = TripPlanner()
    user_type, username = None, None  # Initialize session state

    while True:
        print("\n1. Login\n2. Plan a Trip\n3. View My Trips\n4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_type, username = login()  # Log in and update session state
        elif choice == "2":
            if user_type == "customers" and username:
                planner.plan_trip(username)  
            else:
                print("Please login as a customer to plan trips.")
        elif choice == "3":
            if user_type == "customers" and username:
                my_trips(username)  
            else:
                print("Please login as a customer to view your trips.")
        elif choice == "4":
            print("Thank you for using MakeMyTrip!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


