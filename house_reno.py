# This is the program for the house renovation of the user choice

class House:
    def __init__(self, owner, address, color, num_of_floors, num_rooms, hasSwimmingPool, has_garage):
        self.owner = owner
        self.address = address
        self.color = color
        self.num_of_floors = num_of_floors
        self.num_rooms = num_rooms
        self.hasSwimmingPool = hasSwimmingPool
        self.has_garage = has_garage

    def display_info(self):
        garage_status = "Yes" if self.has_garage else "No"
        pool_status = "Yes" if self.hasSwimmingPool else "No"
        # Printing the first information after the user has input all their house information
        print(f"\n------House Renovation System------")
        print(f"Owner of the house is: {self.owner}")
        print(f"Address: {self.address}")
        print(f"Color of House : {self.color}")
        print(f"Number of Rooms available : {self.num_rooms}")
        print(f"Number of Floors in House : {self.num_of_floors}")
        print(f"Does the House have swimming pool? : {pool_status}")
        print(f"Does the House have Garage? : {garage_status}")
        print("-----------------------------------\n")

    # Defining the functions for the user updated -> renovation

    def change_owner(self):
        new_owner = input("Please enter the new owner of the house:\n")
        self.owner = new_owner
        print("Hence the owner of the house changed sucessfully!!")

    def change_color(self, new_color):
        self.color = new_color

    def change_address(self):
        new_address = input("Please enter the new address of your house: ")
        self.address = new_address
        print(f"Address changed sucesfully to {new_address}")

    def change_floors(self, new_floor):
        self.num_of_floors = new_floor

    def change_rooms(self, new_rooms):
        self.num_rooms = new_rooms


# Main function moved outside the class
def main():
    print("==== CREATE YOUR CUSTOM HOUSE ====")
    owner = input("Please enter the owner of the house: ")
    address = input("Enter address: ")
    color = input("Enter the color of the house: ")
    num_of_floors = int(input("Enter the total number of floors: "))
    num_rooms = int(input("Enter the total number of rooms: "))
    hasSwimmingPool = input(
        "Does your house have swimming pool (yes/no): ").lower() == 'yes'
    has_garage = input(
        "Does your house have a garage in it (yes/no): ").lower() == 'yes'

    # Create a variable name my_house to store the value of all the house
    my_house = House(owner, address, color, num_of_floors,num_rooms, hasSwimmingPool, has_garage)

    print("Initially the House information (without renovation)\n")
    my_house.display_info()

    # Looping for the updation of the house properties
    while True:
        print("==== Renovation Menu ====")
        print("1. Change Owner")
        print("2. Change address")
        print("3. Change color")
        print("4. Change number of rooms")
        print("5. Change number of floors")
        print("6. Show house details")
        print("7. Exit renovation system")

        choice = input(
            "Enter the renovation choice from the above menu (1-6): ")

        if choice == '1':
            my_house.change_owner()

        if choice == '2':
            my_house.change_address()

        elif choice == '2':
            new_color = input("Please enter the new color of the house: ")
            my_house.change_color(new_color)
            print("Color updated successfully!")

        elif choice == '3':
            new_rooms = int(input("Please enter the new number of rooms: "))
            my_house.change_rooms(new_rooms)
            print("Number of rooms updated successfully!")

        elif choice == '4':
            new_floors = int(input("Please enter the new number of floors: "))
            my_house.change_floors(new_floors)
            print("Number of floors updated successfully!")

        elif choice == '5':
            my_house.display_info()

        elif choice == '6':
            print("Exiting renovation system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number between 1-6.")


# Call the main function
if __name__ == '__main__':
    main()
