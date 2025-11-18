### Alisha Rhodes
### 11/16/2025
### Module 3 Lab - Case Study: Lists, Functions, and Classes
### AR_SuperClassVehicle.py
### This program defines a superclass Vehicle and a subclass Automobile. 
### It collects user input to create Automobile objects and displays their information.    


# Define Superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass Automobile inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type: {}".format(self.vehicle_type))
        print("Year: {}".format(self.year))
        print("Make: {}".format(self.make))
        print("Model: {}".format(self.model))
        print("Number of doors: {}".format(self.doors))
        print("Type of roof: {}".format(self.roof))


# Main logic with loop
def main():
    while True:
        # Vehicle type is attached to "car"
        vehicle_type = "car"

        # Collect input
        year = input("What year was the car manufactured?: ")
        make = input("What is the make of the car?: ")
        model = input("Enter the model of the car: ")
        doors = input("How many doors does it have? (2 / 4): ")
        roof = input("Enter the type of roof (solid/sun roof): ")

        # Create Automobile object
        car = Automobile(vehicle_type, year, make, model, doors, roof)

        # Output
        print("\nYou Entered the following Information:")
        car.display_info()

        # Ask if user wants to enter another vehicle
        again = input("\nWould you like to enter another vehicle? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break


# Run the app
if __name__ == "__main__":
    main()
