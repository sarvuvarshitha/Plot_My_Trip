class TripPlanner:
    def __init__(self):
        # Trip packages categorized by type, destination, and category
        self.trips = {
            "national": {
                "beach": [
                    {"destination": "Goa Beach", "price_per_person": 100},
                    {"destination": "Kochi Beach", "price_per_person": 120},
                ],
                "city": [
                    {"destination": "Jaipur City Tour", "price_per_person": 150},
                    {"destination": "Delhi City Tour", "price_per_person": 180},
                ],
                "temple": [
                    {"destination": "Tirupati Temple", "price_per_person": 120},
                    {"destination": "Varanasi Pilgrimage", "price_per_person": 130},
                ],
                "destination_wedding": [
                    {"destination": "Udaipur Royal Wedding", "price_per_person": 500},
                    {"destination": "Goa Beach Wedding", "price_per_person": 450},
                ]
            },
            "international": {
                "beach": [
                    {"destination": "Maldives Beach", "price_per_person": 500},
                    {"destination": "Bora Bora Beach", "price_per_person": 600},
                ],
                "city": [
                    {"destination": "Paris City Tour", "price_per_person": 1000},
                    {"destination": "New York City Tour", "price_per_person": 1200},
                ],
                "temple": [
                    {"destination": "Angkor Wat Temple", "price_per_person": 800},
                    {"destination": "Golden Temple Amritsar", "price_per_person": 700},
                ],
                "destination_wedding": [
                    {"destination": "Paris Destination Wedding", "price_per_person": 1500},
                    {"destination": "Santorini Wedding", "price_per_person": 1700},
                ]
            }
        }
        self.booked_trips = {}  # To store booked trips by username

    def display_trip_types(self):
        print("\nChoose your trip type:")
        print("1. National Trip")
        print("2. International Trip")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            print("\nYou chose a National Trip.")
            return "national"
        elif choice == "2":
            print("\nYou chose an International Trip.")
            return "international"
        else:
            print("Invalid choice. Please choose either 1 or 2.")
            return self.display_trip_types()

    def display_categories(self, trip_type):
        print(f"\nChoose your trip category for {trip_type.capitalize()} trips:")
        categories = self.trips[trip_type]
        for idx, category in enumerate(categories.keys(), start=1):
            print(f"{idx}. {category.capitalize()}")
        choice = input("Enter your choice (1-4): ").strip()

        categories_list = list(categories.keys())
        if choice.isdigit() and 1 <= int(choice) <= len(categories_list):
            print(f"\nYou chose the {categories_list[int(choice) - 1].capitalize()} category.")
            return categories_list[int(choice) - 1]
        else:
            print("Invalid choice. Please choose a valid category.")
            return self.display_categories(trip_type)

    def recommend_trip(self, trip_type, category, budget, num_people):
        print(f"\nPlanning a {trip_type.capitalize()} trip with a budget of ${budget} for {num_people} people...")

        available_trips = self.trips[trip_type][category]
        possible_trips = []

        for package in available_trips:
            total_cost = package["price_per_person"] * num_people
            if total_cost <= budget:
                possible_trips.append((package, total_cost))

        if not possible_trips:
            print("\nNo packages available within your budget and preference.")
        else:
            print("\nRecommended Packages within your budget:")
            for idx, (package, total_cost) in enumerate(possible_trips, start=1):
                print(f"{idx}. {package['destination']} - Total Cost: ${total_cost}")
            choice = input("\nEnter the number of the package you'd like to book (or press Enter to skip): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(possible_trips):
                return possible_trips[int(choice) - 1]
        return None

    def plan_trip(self, username):
        print("\n--- Step 1: Trip Type Selection ---")
        trip_type = self.display_trip_types()

        print("\n--- Step 2: Trip Category Selection ---")
        category = self.display_categories(trip_type)

        print("\n--- Step 3: Budget and Number of People ---")
        budget = float(input(f"\nEnter your budget for the {category} trip: $"))
        num_people = int(input("Enter the number of people: "))

        print("\n--- Step 4: Trip Recommendation ---")
        selected_trip = self.recommend_trip(trip_type, category, budget, num_people)

        if selected_trip:
            package, total_cost = selected_trip
            print(f"\nYou have successfully booked: {package['destination']} - Total Cost: ${total_cost}")
            if username not in self.booked_trips:
                self.booked_trips[username] = []
            self.booked_trips[username].append({"trip": package, "total_cost": total_cost})


def my_trips(username):
    planner = TripPlanner()
    if username in planner.booked_trips:
        trips = planner.booked_trips[username]
        print("\nYour Booked Trips:")
        for idx, trip in enumerate(trips, start=1):
            print(f"{idx}. Destination: {trip['trip']['destination']}, Total Cost: ${trip['total_cost']}")
        print("\nWould you like to update any trip details?")
        print("1. Yes\n2. No")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            trip_idx = int(input("Enter the trip number you'd like to update: ")) - 1
            if 0 <= trip_idx < len(trips):
                print(f"Updating trip to {trips[trip_idx]['trip']['destination']}")
                # Update logic here
                trips[trip_idx]['total_cost'] += 50  # Example: Adding $50 as an update
                print("Trip updated successfully!")
            else:
                print("Invalid trip number.")
    else:
        print("\nYou have no booked trips.")
