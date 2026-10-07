class Student:

    def __init__(self, name, courseCode, dict_units):
        self.name = name
        self.courseCode = courseCode
        self.dict_units = dict_units


unitInfo = {"KG": "ITD104", "GP":"CAB302", "KG": "ITD201"}

john = Student("Anthony", "IT10", unitInfo)
john.dict_units = unitInfo
jill = Student("Jill", "ET10",unitInfo)


print(f"The student name is {john.name} and is in course {john.courseCode}")
print(f"The student name is {jill.name} and is in course {jill.courseCode}")

for key,value in john.dict_units.items():
    print(f"John in enrolled in {key} at {value}")