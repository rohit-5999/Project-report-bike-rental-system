Classes:
Bike: Represents a bicycle with attributes like ID, model, and a flag indicating availability (rented or not).
User: Represents a user with ID, name, email, password, and a list to keep track of their rentals.
Rental: Represents a rental instance with a user, bike, rental duration (hours), and calculated cost based on the duration.

Functions:
show_available_bikes(): Displays a list of currently available bikes.
register_user(): Creates a new user account with details like name, email, and password.
authenticate_user(): Validates user login credentials (email and password).
rent_bike(user): Allows logged-in users to rent a bike. It displays available options, takes the desired bike ID and rental duration as input, and updates the bike's availability and user's rental history.
main(): The main function that drives the program. It presents a menu with options for registration, login, viewing available bikes, renting a bike, and exiting. It calls the appropriate functions based on user choices.

Overall Functionality:
This code provides a basic framework for a bike rental system. Users can register, log in, view available bikes, rent bikes, and see the estimated cost based on the rental duration. The system keeps track of user information, bike availability, and rental history.

Potential Enhancements:
Persistence: Currently, data is lost when the program exits. Storing data in files or a database can enable saving and loading information between sessions.
Payment Processing: The code currently only estimates the cost. A payment processing system could be integrated for actual payments.
Advanced Features: Additional features could be implemented, such as different bike types with varying rates, returning bikes, viewing rental history, and managing user accounts.
Error Handling: More robust error handling could be implemented to handle invalid user input and potential exceptions.# Project-report-bike-rental-system
