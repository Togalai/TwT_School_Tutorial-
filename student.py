from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, first, last, dob, phone, address, international=False):
        super().__init__(self, first, last, dob, phone, address) # Using super brings in the Exception checking for Address that was put into the Person Class
        self.international = international # Adding on the International flag as needed to this constructor? Need to look up and learn constructors again.
        self.enrolled = [] # a student is created but is not enrolled in anything yet so the list is blank

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Exception("Invalid Enroll...")

        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) < 3
