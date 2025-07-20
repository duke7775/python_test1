#说明：创建class Student
import datetime

class Student:
    def __init__(self, name, age, nationality, gender, math_score, english_score):
        print("调用\"__init__\"方法")
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.math_score = math_score
        self.english_score = english_score
        self.creation_time = datetime.datetime.now()
        

    def create_student(self):
        print("调用\"create_student\"方法")
        return f"Student {self.name} created with time {self.creation_time}"
    

    def list_student(self):
        print("调用\"list_student\"方法")
        return f"Name: {self.name}, Age: {self.age}, Nationality: {self.nationality}, Gender: {self.gender}, Math Score: {self.math_score}, English Score: {self.english_score}, Creation Time: {self.creation_time}"
    

    def __del__(self):
        print("调用\"__del__\"方法")
        print(f"Student {self.name} deleted at {datetime.datetime.now()}")
        

if __name__ == "__main__":
        student = Student("Duke", 19, "China", "M", 90, 85)
        print(student.create_student())
        print(student.list_student())