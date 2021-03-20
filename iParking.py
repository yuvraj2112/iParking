import sys

import logic as park

parking = None

def main():
    if len(sys.argv) < 2:
        sys.exit("(Sample) Usage: python iParking.py data/test.csv")
    commands = load_data(sys.argv[1])
    runCommands(commands)

def runCommands(commands):
    for item in commands:
        command = item[0]
        args = item[1]
        if (command == 'Create_parking_lot'):
            parking = park.Parking(*args)
            print (f'Created parking of {args[0]} slots')
        elif (command == 'Park'):
            park.parkNewCar(parking, *args)
        elif (command == 'Leave'):
            park.leaveSlot(parking, *args)
        elif (command == 'Slot_numbers_for_driver_of_age'):
            park.age_to_slots(parking, *args)
        elif (command == 'Vehicle_registration_number_for_driver_of_age'):
            park.age_to_reg(parking, *args)
        elif (command == 'Slot_number_for_car_with_number'):
            slot = park.slot4Car(parking, *args)
            print (f'The car {args[0]} is parked at {slot}')
        else:
            raise KeyError
    return True


def load_data(filename):
    """
        Loads and returns insruction data as a list of tuples of command and arguements.
    """
    data = list()
    with open(filename) as f:
        reader = f.readlines()
        for row in reader:
            elems = row.strip().split(' ')
            data.append((elems[0], list(arg for idx, arg in enumerate(elems) if ((idx + 1) % 2) == 0)))
    return data

if __name__ == "__main__":
    main()
