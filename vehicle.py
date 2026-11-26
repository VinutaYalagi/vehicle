import sys

def calculate_parking_fee(vehicle_type, hours):

    if vehicle_type == "two-wheeler":
        rate = 20

    elif vehicle_type == "four-wheeler":
        rate = 50

    elif vehicle_type == "heavy vehicle":
        rate = 100

    else:
        print("Invalid vehicle type!")
        sys.exit()

    total_fee = rate * hours

    return total_fee


def main():

    print("===== PARKING MANAGEMENT SYSTEM =====")

    vehicle_type = input("Enter vehicle type (Two-wheeler / Four-wheeler / Heavy vehicle): ").lower()

    hours = float(input("Enter parking duration in hours: "))

    if hours <= 0:
        print("Please enter valid parking hours.")
        sys.exit()

    total_fee = calculate_parking_fee(vehicle_type, hours)

    print("\n===== PARKING RECEIPT =====")
    print("Vehicle Type:", vehicle_type)
    print("Parking Duration:", hours, "hours")
    print("Total Parking Fee: Rs.", total_fee)


if __name__ == "__main__":
    main()