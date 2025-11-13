def get_rent():
    while True:
        try:
            rent = int(
                input("Please enter the amount of stay rent to be paid: "))
            if rent < 0:
                print(f"{rent} cannot be less than 0. Not considered a rent amount.")
            elif rent > 0:
                print(f"Total amount of rent to be paid is {rent}")
                return rent  # ✅ Return value
            else:
                print("There is no rent to be paid for the user.")
                return 0     # ✅ Return 0 if rent is 0
        except ValueError:
            print("Invalid rent amount. Please try again.")


def get_food_cost():
    while True:
        try:
            food = float(input("Please enter the amount of food to be paid: "))
            if food < 0:
                print("Food cost cannot be less than zero.")
            elif food > 0:
                print(f"Total amount of food rent to be paid: {food}")
                return food  # ✅ Return value
            else:
                print("Rent amount cannot be zero.")
                return 0
        except ValueError:
            print("Invalid choice! Please enter a number.")


def get_electricity_bill():
    while True:
        try:
            units = float(
                input("Please enter the number of electricity units consumed: "))
            charge_per_unit = float(
                input("Please enter the charge per unit: "))
            if units < 0 or charge_per_unit < 0:
                print("Values cannot be negative.")
            else:
                total_bill = units * charge_per_unit
                print(f"Electricity bill to be paid: {total_bill}")
                return total_bill  # ✅ Return computed value
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def calc_total():
    rent = get_rent()
    food = get_food_cost()
    electricity = get_electricity_bill()

    total = rent + food + electricity  # ✅ all are numbers now
    # Here we receive the total amount of rents in int hence the total will also return in int
    print("\n*** Summary ***")
    print(f"Rent to be paid: {rent}")
    print(f"Food amount to be paid: {food}")
    print(f"Electricity bills to be paid: {electricity}")
    print("----------------------------")
    print(f"Total amount to be paid: {total}")


calc_total()
