from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []
        self.enrollments = []

                # Using isinstance to check if the professor entered is the correct format or an instance of the professor class from professor.py
        if professor is isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Exception("Invalid Professor...")   # Not sure what he's using here to raise the Exception. Have to look it up later
                            
            self.professors = professor
        else:
            raise Exception("Invalid Professor...")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Exception("Invalid Professor...")

        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Exception("Invalid Enroll...")

        if len(enrollments) == self.max_:
            raise Exception("Cannot enroll if course is full")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) <= self.min_