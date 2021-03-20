class Parking():
    """
        Parking object for each parking.
        Properties:
            size: The total size of the parking.
            slots: The total number of slots with Car object assigned, if parked. None, otherwise.
            closestSlot: The slot available nearest to entry. Infinity in case parking full.
            full: Flag denoting if parking is full.
            info: Dictionary object that contains processed data. Think of it as analytical data useful for quickly querying when information is required.
    """
    def __init__(self, size):
        self.size = int(size)
        self.slots = dict([(i, None) for i in range(1, self.size+1)])
        self.closestSlot = 1
        self.full = False
        self.info = {
            'age_to_slot': {},
            'reg_to_slot': {}
        }

class Car():
    """
        Car object for each driver that enters the building.
        Properties:
            registration: The registration number of the car.
            driver_age: The age of the driver of the car.
    """
    def __init__(self, car_reg, age):
        self.registration = car_reg
        self.driver_age = age

def slot4Car(parking, car_reg):
    """
        Returns slot number for a registration, if exists.
        Otherwise, returns None.
    """
    return parking.info['reg_to_slot'][car_reg] if car_reg in parking.info['reg_to_slot'] else None

def parkNewCar(parking, car_reg, age):
    """
        Creates new car object and assigns a parking slot, if car does not already exists.
        Updates the parking information parameters.
        Prints the result.
        Return allocated slot on success. Otherwise, None is returned.
    """
    if (parking.full):
        print ('Car parking is full')
        return None
    if (slot4Car(parking, car_reg)):
        print ('Car already parked')
        return None
    alloc_slot = parking.closestSlot
    parking.slots[alloc_slot] = Car(car_reg, age)


    parking.info['reg_to_slot'][car_reg] = alloc_slot
    if (age in parking.info['age_to_slot']):
        parking.info['age_to_slot'][age].append(alloc_slot)
    else:
        parking.info['age_to_slot'][age] = [alloc_slot]

    updateParkingInfo(parking)
    print (f'Car {car_reg} parked at {alloc_slot}')
    return alloc_slot

def leaveSlot(parking, slot):
    """
        Empties a parking slot, if filled.
        Updates the parking information parameters.
        Prints the result.
        Returns the car object on success. Otherwise, None is returned.
    """
    slot = int(slot)
    if (parking.slots[slot] == None):
        print (f'Slot {slot} is already empty')
        return None
    car = parking.slots[slot]
    parking.slots[slot] = None
    del parking.info['reg_to_slot'][car.registration]
    parking.info['age_to_slot'][car.driver_age].remove(slot)
    updateParkingInfo(parking, emptied=slot)
    print (f'Slot number {slot} vacated, the car with vehicle registration number "{car.registration}" left the space, the driver of the car was of age {car.driver_age}')
    return car

def updateParkingInfo(parking, emptied=None):
    """
        Processes and updates the parking object's values post arrival or departure, to ensure smooth & quick operations.
    """
    if (emptied != None and emptied < parking.closestSlot):
        parking.closestSlot = emptied
        parking.full = False
        return
    for slot in parking.slots:
        if (parking.slots[slot] == None):
            parking.closestSlot = slot
            parking.full = False
            return
    parking.closestSlot = float('inf')
    parking.full = True
    return

def age_to_reg(parking, age):
    """
        Prints and returns information: The registration numbers of people of x age.
    """
    if (age not in parking.info['age_to_slot']):
        print ('No cars with drivers of this age in parking')
        return
    slots = parking.info['age_to_slot'][age]
    print (','.join(list(parking.slots[slot].registration for slot in slots)))
    return list(parking.slots[slot].registration for slot in slots)

def age_to_slots(parking, age):
    """
        Prints and returns information: The slot numbers of people of x age.
    """
    if (age not in parking.info['age_to_slot']):
        print ('No slots occcupied by drivers of this age in parking')
        return
    print (','.join(list(str(slot) for slot in parking.info['age_to_slot'][age])))
    return parking.info['age_to_slot'][age]
