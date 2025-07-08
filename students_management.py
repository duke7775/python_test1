#功能 学生管理系统
import json
import os
from datetime import datetime

#加载学生数据
def load_students():
    if os.path.exists('students.json'):
        try:
            with open('students.json', 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

#保存学生数据
def save_students(students):
    with open('students.json', 'w') as f:
        json.dump(students, f)

#创建学生信息
def create_student(students):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    nationality = str(input("Enter nationality:"))
    gender = input("Enter gender (M/F):")
    if gender not in ['M', 'F']:
        print("Invalid gender. Please enter M or F.")
        return
    math_score = float(input("Enter math score:"))
    english_score = float(input("Enter English score:"))

    students[name] = {
        'name': name,
        'age': age,
        'nationality': nationality,
        'gender': gender,
        'math_score': math_score,
        'english_score': english_score,
        'created_at': datetime.now().isoformat()
    }
    print("student created successfully")

# 列出学生信息
def list_students(students):
    for student in students.values():
        print(f"Name: {student['name']}, Age: {student['age']}, Nationality: {student['nationality']}, Gender: {student['gender']}, Math Score: {student['math_score']}, English Score: {student['english_score']}, Created At: {student['created_at']}")
    if not students:
        print("No students found.") 
        return

# 删除学生信息
def delete_student(students):
    name = input("Enter the name of the student to delete:")
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully.")
    else:
        print(f"Student {name} not found.")

#按数学分数排序




#主要功能
def main():
    students = load_students()
    while True:
        command = input("Enter command (create/list/delete/order/quit): ")
        if command == "create":
            create_student(students)
        elif command == "list":
            list_students(students)
        elif command == "delete":
            delete_student(students)
        elif command == "quit":
            save_students(students)
            break
        else:
            print("Invalid command.")


if __name__ == "__main__": main()      