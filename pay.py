def trip_payment():
    print("Welcome to the Trip Payment Portal!")
    trip_type = input("Is this a National or International trip? (Enter 'National' or 'International'): ").strip().lower()
    
    if trip_type not in ["national", "international"]:
        print("Invalid trip type. Please enter 'National' or 'International'.")
        return

    try:
        budget = float(input("Enter your budget amount in USD: "))
        if budget < 0:
            print("Budget cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for the budget.")
        return

    # Example cost setup
    national_trip_cost = 500  # Cost in USD
    international_trip_cost = 1500  # Cost in USD

    if trip_type == "national":
        trip_cost = national_trip_cost
        print(f"The cost of a National trip is ${trip_cost}.")
    else:
        trip_cost = international_trip_cost
        print(f"The cost of an International trip is ${trip_cost}.")

    if budget >= trip_cost:
        print(f"Your budget of ${budget} covers the trip! Proceeding to payment.")
        remaining_budget = budget - trip_cost
        print(f"Remaining budget after payment: ${remaining_budget:.2f}")
    else:
        remaining_amount = trip_cost - budget
        print(f"Your budget of ${budget} is insufficient. You need an additional ${remaining_amount:.2f} to proceed.")
        # Option to pay partially or cancel
        partial_payment = input("Do you want to pay the current budget as a partial payment? (yes/no): ").strip().lower()
        if partial_payment == "yes":
            print(f"You have paid ${budget} as a partial payment. Please arrange the remaining ${remaining_amount:.2f} to complete the booking.")
        else:
            print("Trip booking canceled due to insufficient funds.")

# Call the function
trip_payment()