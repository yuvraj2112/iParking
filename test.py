import unittest2 as unittest

import logic as park
import iParking as interface


class TestSum(unittest.TestCase):
    def test_park_car(self):
        """
        Test that it can park a car
        """
        parking = park.Parking(2)
        result = park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        self.assertEqual(result, 1)

    def test_leave_car(self):
        """
        Test that it can empty a slot
        """
        parking = park.Parking(2)
        park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        result = park.leaveSlot(parking, 1)
        self.assertIsInstance(result, park.Car)

    def test_slot4Car(self):
        """
        Test that it can return slot where a car is parked
        """
        parking = park.Parking(2)
        park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        result = park.slot4Car(parking, 'KA-01-HH-1234')
        self.assertEqual(result, 1)

    def test_slot4Car_neg(self):
        """
        Test that it can return None where an invalid car is passed
        """
        parking = park.Parking(2)
        park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        result = park.slot4Car(parking, 'KA-01-HH-1235')
        self.assertIsNone(result)

    def test_slots_for_age(self):
        """
        Test that it can return list of slots for age
        """
        parking = park.Parking(2)
        park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        park.parkNewCar(parking, 'KA-01-HH-1235', 21)
        result = park.age_to_slots(parking, 21)
        self.expected = [1, 2]
        self.assertListEqual(result, self.expected)

    def test_regs_for_age(self):
        """
        Test that it can return list of registrations for age
        """
        parking = park.Parking(2)
        park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        park.parkNewCar(parking, 'KA-01-HH-1235', 21)
        result = park.age_to_reg(parking, 21)
        self.expected = ['KA-01-HH-1234', 'KA-01-HH-1235']
        self.assertListEqual(result, self.expected)

    def test_parking_full_scenario(self):
        """
        Test that it can return None when we try to park a car after parking has become full
        """
        parking = park.Parking(2)
        result = park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        self.assertEqual(result, 1)
        result = park.parkNewCar(parking, 'KA-01-HH-1235', 21)
        self.assertEqual(result, 2)
        result = park.parkNewCar(parking, 'KA-01-HH-1236', 21)
        self.assertFalse(result)

    def test_car_exists_scenario(self):
        """
        Test that it can return None when we try to park a car after parking has become full
        """
        parking = park.Parking(2)
        result = park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        self.assertEqual(result, 1)
        result = park.parkNewCar(parking, 'KA-01-HH-1235', 21)
        self.assertEqual(result, 2)
        result = park.parkNewCar(parking, 'KA-01-HH-1235', 21)
        self.assertIsNone(result)

    def test_closest_parking_scenario(self):
        """
        Test that it can always park in the spot closest to the entrance
        """
        parking = park.Parking(3)
        park.parkNewCar(parking, 'KA-01-HH-1234', 21)
        park.parkNewCar(parking, 'KA-01-HH-1235', 21)
        park.leaveSlot(parking, 1)
        result = park.parkNewCar(parking, 'KA-01-HH-1236', 21)
        self.assertEqual(result, 1)

    def test_interface_command(self):
        """
        Test that the interface runs correctly with the right commands
        """
        result = interface.runCommands([
            ('Create_parking_lot', ['3']),
            ('Park', ['KA-01-HH-1234', '21']),
            ('Park', ['KA-01-HH-1324', '21']),
            ('Slot_numbers_for_driver_of_age', ['21'])
        ])
        self.assertTrue(result)

    def test_interface_command_neg(self):
        """
        Test that the interface raises correct exception when unsuppoted command is passed
        """
        self.assertRaises(KeyError, interface.runCommands, [
            ('Create_parking_lot', ['3']),
            ('Park', ['KA-01-HH-1234', '21']),
            ('Park', ['KA-01-HH-1324', '21']),
            ('Wrong_command', ['21'])
        ])

if __name__ == '__main__':
    unittest.main()
