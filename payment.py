def make_payment(amount):
    print(f"\n--- Payment ---")
    print(f"Your Total Amount: ${amount}")
    payment_method = input("Enter Payment Method (Card/UPI): ")
    if payment_method.lower() in ["card", "upi"]:
        print("Payment Successful! Thank you.")
    else:
        print("Invalid Payment Method.")
