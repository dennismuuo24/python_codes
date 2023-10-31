class Person:
    def __init__(self, age, first_name, last_name):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def display_info(self):
        print("Age:", self.age)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)


class Student(Person):
    def __init__(self, age, first_name, last_name, reg_no, department, hostel, mean_score):
        super().__init__(age, first_name, last_name)
        self.reg_no = input("Enter Reg No:= ")
        self.department = input("Enter Department := ")
        self.hostel = input("Enter Hostel := ")
        self.mean_score = mean_score

    def display_info(self):
        super().display_info()
        print("Registration Number:", self.reg_no)
        print("Department:", self.department)
        print("Hostel:", self.hostel)
        print("Mean Score:", self.mean_score)


# Create an instance of the Student class
student1 = Student(20, "John", "Doe", "12345", "Computer Science", "Smith Hostel", 85.5)

# Display student information
student1.display_info()