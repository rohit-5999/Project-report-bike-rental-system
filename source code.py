class Bike:
    def __init__(self, bike_id, model):
        self.id = bike_id
        self.model = model
        self.available = True  # Track bike availability


class User:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.rentals = []  # Keep track of user rentals


class Rental:
    def __init__(self, user, bike, rental_duration):
        self.user = user
        self.bike = bike
        self.duration = rental_duration
        self.rental_cost = self.calculate_cost(rental_duration)

    @staticmethod
    def calculate_cost(duration):
        if duration <= 1:
            return 399  # Hourly rate
        elif duration <= 24:
            return 2499  # Daily rate
        else:
            return 9999  # Weekly rate


# Inventory of bikes (list of Bike objects)
bikes = [
    Bike(1, "Mountain Bike"),
    Bike(2, "Road Bike"),
    Bike(3, "Hybrid Bike"),
]

# User registry
users = []

# Function to display available bikes
def show_available_bikes():
    print("\nAvailable Bikes:")
    available = False
    for bike in bikes:
        if bike.available:
            print(f"- Bike ID: {bike.id}, Model: {bike.model}")
            available = True
    if not available:
        print("No bikes are currently available.")


def register_user():
    user_id = len(users) + 1
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    new_user = User(user_id, name, email, password)
    users.append(new_user)
    print(f"User {name} registered successfully!")


def authenticate_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user.email == email and user.password == password:
            print(f"Welcome, {user.name}!")
            return user
    print("Invalid email or password.")
    return None


def rent_bike(user):
    show_available_bikes()
    try:
        bike_id = int(input("Enter bike ID to rent (or 0 to exit): "))
        if bike_id == 0:
            return

        found_bike = None
        for bike in bikes:
            if bike.id == bike_id and bike.available:
                found_bike = bike
                break

        if found_bike:
            rental_duration = int(input("Enter rental duration (hours): "))
            new_rental = Rental(user, found_bike, rental_duration)
            user.rentals.append(new_rental)
            found_bike.available = False  # Mark bike as rented
            print(f"Bike (ID: {found_bike.id}) rented successfully!")
            print(f"Estimated cost: Rs{new_rental.rental_cost}")
        else:
            print(f"Bike (ID: {bike_id}) is unavailable.")
    except ValueError:
        print("Invalid input. Please enter a valid bike ID and rental duration.")


def main():
    while True:
        print("\nBike Rental System")
        print("1. Register User")
        print("2. Login")
        print("3. View Available Bikes")
        print("4. Rent a Bike")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                register_user()
            elif choice == 2:
                user = authenticate_user()
                if user:
                    while True:
                        print("\nUser Menu")
                        print("1. View Available Bikes")
                        print("2. Rent a Bike")
                        print("0. Logout")

                        user_choice = int(input("Enter your choice: "))
                        if user_choice == 1:
                            show_available_bikes()
                        elif user_choice == 2:
                            rent_bike(user)
                        elif user_choice == 0:
                            print("successfully logout.")
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == 3:
                show_available_bikes()
            elif choice == 4:
                print("Please log in to rent a bike.")
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
