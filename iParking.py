import sys

import logic as park

parking = None

def main():
    if len(sys.argv) < 2:
        sys.exit("(Sample) Usage: python iParking.py data/test.csv")
    commands = load_data(sys.argv[1])
    runCommands(commands)

def runCommands(commands):
    """
        Takes a list of valid commands as parameter. Runs them in order.
        Prints the results.
        Raises KeyError if invalid command is passed.
    """
    for item in commands:
        command = item[0]
        args = item[1]
        if (command == 'Create_parking_lot'):
            parking = park.Parking(*args)
            print (f'Created parking of {args[0]} slots')
        elif (command == 'Park'):
            result = park.parkNewCar(parking, *args)
            if (result != None):
                print (f'Car with vehicle registration number "{args[0]}" has been parked at slot number {result}')
            else:
                print ('Car exists') if result == None else print ('Car parking is full')
        elif (command == 'Leave'):
            result = park.leaveSlot(parking, *args)
            if (result == None):
                print (f'Slot {slot} is already empty')
            else:
                print (f'Slot number {args[0]} vacated, the car with vehicle registration number "{result.registration}" left the space, the driver of the car was of age {result.driver_age}')
        elif (command == 'Slot_numbers_for_driver_of_age'):
            result = park.age_to_slots(parking, *args)
            print (','.join(list(str(slot) for slot in result))) if result != None or len(result) > 0 else print ('No slots occcupied by drivers of this age in parking')
        elif (command == 'Vehicle_registration_number_for_driver_of_age'):
            result = park.age_to_reg(parking, *args)
            print (','.join(result)) if result != None or len(result) > 0 else print ('No cars with drivers of this age in parking')
        elif (command == 'Slot_number_for_car_with_number'):
            slot = park.slot4Car(parking, *args)
            print (f'{slot}')
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
