#说明：创建class Student
import datetime

class Student:
    name: str = ""
    age: int = 0
    nationality: str = ""
    gender: str = ""
    math_score: int = 0
    english_score: int = 0

    def __init__(self, name, age, nationality, gender, math_score, english_score):
        print("调用\"__init__\"方法")
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.math_score = math_score
        self.english_score = english_score
        self.creation_time = datetime.datetime.now()
        

    def create(self) -> None:
        print("调用\"create\"方法")
        print( f"Student {self.name} created with time {self.creation_time}")
    

    def list(self) -> None:
        print("调用\"list\"方法")
        print( f"Name: {self.name}, Age: {self.age}, Nationality: {self.nationality}, Gender: {self.gender}, Math Score: {self.math_score}, English Score: {self.english_score}, Creation Time: {self.creation_time}")
    

def main() -> None:
    student = Student(name="Duke", age=19, nationality="China", gender="M", math_score=90, english_score=85)
    student.create()
    student.list()

if __name__ == "__main__":
    main()