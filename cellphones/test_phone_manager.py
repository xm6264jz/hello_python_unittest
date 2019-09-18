import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        #  add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        #  you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Al')
        employee2 = Employee(2, 'Beatrice')
        employee3 = Employee(3, 'Carl')
        employee4 = Employee(4, 'Darlene')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_employee(employee2)
        test_PhoneAssignments.add_employee(employee3)
        test_PhoneAssignments.add_employee(employee4)

        self.assertIn(employee1, test_PhoneAssignments.employees)
        self.assertIn(employee2, test_PhoneAssignments.employees)
        self.assertIn(employee3, test_PhoneAssignments.employees)
        self.assertIn(employee4, test_PhoneAssignments.employees)
                        
    def test_create_and_add_employee_with_duplicate_id(self):
        # write this test and then remove the self.fail() statement
        # you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Al')
        employee2 = Employee(1, 'Beatrice')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_employee(employee2)

        self.assertIn(employee1, test_PhoneAssignments.employees)
        self.assertNotIn(employee2, test_PhoneAssignments.employees)

    def test_assign_phone_to_employee(self):
        # write this test and remove the self.fail() statement
        # you'll need to fix the assign method in PhoneAssignments

        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Alice')
        phone1 = Phone(1, 'Samsung', 'Galaxy Note 15')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_phone(phone1)

        test_PhoneAssignments.assign(phone1.id, employee1)
        self.assertTrue(phone1.employee_id == 1)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.

        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bob')
        phone1 = Phone(1, 'Samsung', 'Galaxy Note 15')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_employee(employee2)
        test_PhoneAssignments.add_phone(phone1)

        test_PhoneAssignments.assign(phone1.id, employee1)
        with self.assertRaises(PhoneError):    
            test_PhoneAssignments.assign(phone1.id, employee2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Alice')
        phone1 = Phone(1, 'Samsung', 'Galaxy Note 15')
        phone2 = Phone(2, 'Samsung', 'Ultra HD')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_phone(phone1)
        test_PhoneAssignments.add_phone(phone2)

        test_PhoneAssignments.assign(phone1.id, employee1)
        with self.assertRaises(PhoneError):    
            test_PhoneAssignments.assign(phone2.id, employee1)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Alice')
        phone1 = Phone(1, 'Samsung', 'Galaxy Note 15')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_phone(phone1)

        test_PhoneAssignments.assign(phone1.id, employee1)
        test_PhoneAssignments.assign(phone1.id, employee1)


    def test_un_assign_phone(self):
        # write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Alice')
        phone1 = Phone(1, 'Samsung', 'Galaxy Note 15')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_phone(phone1)

        test_PhoneAssignments.assign(phone1.id, employee1)
        test_PhoneAssignments.un_assign(phone1.id)
        self.assertIsNone(phone1.employee_id)


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist

        test_PhoneAssignments = PhoneAssignments()
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bob')
        employee3 = Employee(3, 'Caitie')
        employee4 = Employee(4, 'Dan')
        phone1 = Phone(1, 'Samsung', 'Galaxy Note 15')
        phone2 = Phone(2, 'Samsung', 'Ultra HD')

        test_PhoneAssignments.add_employee(employee1)
        test_PhoneAssignments.add_employee(employee2)
        test_PhoneAssignments.add_employee(employee3)
        test_PhoneAssignments.add_phone(phone1)
        test_PhoneAssignments.add_phone(phone2)

        test_PhoneAssignments.assign(phone1.id, employee1)
        test_PhoneAssignments.assign(phone2.id, employee2)

        print(test_PhoneAssignments.phone_info(employee1))
        print(test_PhoneAssignments.phone_info(employee2))

        self.assertIsNone(test_PhoneAssignments.phone_info(employee3))

        with self.assertRaises(PhoneError):    
            test_PhoneAssignments.phone_info(employee4)
