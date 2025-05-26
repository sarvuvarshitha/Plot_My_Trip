
---

# 🌍 Trip Planner – Your Personalized Travel Assistant

## ✈️ Overview

**Trip Planner** is a Python-based travel planning application that allows users to seamlessly plan, budget, and manage trips both **nationally and internationally**. Inspired by real-world platforms like MakeMyTrip, this CLI-based app helps users explore destinations, manage bookings, and simulate payments all within a smart, interactive console interface.

---

## 🔧 Features

* 👥 **User Management**: Login, register, and view personal details (supports both customers and employees).
* 🗺️ **Trip Customization**:

  * Choose between **National** and **International** trips.
  * Select from categories like **Beach**, **City**, **Temple**, or **Destination Wedding**.
* 💰 **Budget Handling**: Enter your budget and get trip suggestions that fit your financial plan.
* 📦 **Package Recommendations**: Displays filtered trip options based on your input (price per person, number of people, etc.).
* 🧾 **Booking System**: Book and save trips with dynamic cost calculations.
* 💳 **Payment Simulation**: Make or simulate full/partial payments using mock UPI/Card methods.
* 🧳 **View & Update Bookings**: See your booked trips and make changes.

---

## 🗂️ Files Breakdown

| File                         | Purpose                                               |
| ---------------------------- | ----------------------------------------------------- |
| `main.py`                    | Entry point for the app – handles menu navigation     |
| `users.py`                   | Manages login, registration, and user profiles        |
| `trips.py`                   | Core logic for planning and recommending trips        |
| `data.py`                    | Contains sample data for flights, buses, and hotels   |
| `pay.py`                     | Budget vs trip cost validation and payment simulation |
| `payment.py` / `payments.py` | Mock payment processor modules                        |
| `utils.py`                   | Helper functions for validation and UI display        |

---

## 💻 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/trip-planner.git
   cd trip-planner
   ```

2. **Run the app**

   ```bash
   python main.py
   ```

---

## 📚 Requirements

This project uses standard Python libraries. It does not require any external dependencies.

---

## 🎯 Future Improvements

* GUI/Frontend using Tkinter or web framework
* Real-time API integration for flight and hotel bookings
* User session persistence and trip history storage
* Email or SMS notifications

---

## 🙌 Acknowledgements

* CLI Design inspired by platforms like **MakeMyTrip**
* Basic mock data used for demo purposes

---

