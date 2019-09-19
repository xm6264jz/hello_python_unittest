# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        # raise exception if two employees with same ID are added

        try:
            employee_ids = []
            for current_employee in self.employees:
                employee_ids.append(current_employee.id)

            if employee.id in employee_ids:
                raise PhoneError('Employee is already added')
            else:
                self.employees.append(employee)
        except:
            print('This employee is already in the list.')


    def add_phone(self, phone):
        # raise exception if two phones with same ID are added
        
        try:
            phone_ids = []
            for current_phones in self.phones:
                phone_ids.append(current_phones.id)
            
            if phone.id in phone_ids:
                raise PhoneError('This phone is already in the list')
            else:
                self.phones.append(phone)
        except:
            print('This phone is already in the list')

    def assign(self, phone_id, employee):
        # Find phone in phones list
        # if phone is already assigned to an employee, do not change list, raise exception
        # if employee already has a phone, do not change list, and raise exception
        # if employee already has this phone, don't make any changes. This should NOT raise an exception.
        
        # If the phone is already assigned to an employee raise error
        # Loop through the phone list to get my phone object by matching ID
        print()
        # Find the phone in the phone list that matches the phone ID given
        # if that phone has an employee ID that means it is already assigned - raise error
        for phone in self.phones:
            if phone.id == phone_id:
                if phone.employee_id == employee.id:
                    print('This phone is already assigned to this employee')
                elif phone.employee_id != None:
                    raise PhoneError('This phone is already assigned to an employee')
                else:
                    # Loop through all phones in the phone list and add the employee IDs to a list if they have an assigned employee
                    employee_ids = []
                    for current_phone in self.phones:
                        if current_phone.employee_id == int:
                            employee_ids.append(current_phone.id)
                
                    # If the employee ID is found in the list of employee_ids that means they already have a phone & raise an error
                    if employee.id in employee_ids:
                            raise PhoneError('employee id is already in list')
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(employee.id)
                return


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        #   should return None if the employee does not have a phone
        #   the method should raise an exception if the employee does not exist
        if employee not in self.employees:
            raise PhoneError('Employee does not exist')

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None

class PhoneError(Exception):
    pass
