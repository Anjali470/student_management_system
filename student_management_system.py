students = [{'id': 1, 'name': 'John', 'age': 20, 'marks': [85, 90, 78]},
                {'id': 2, 'name': 'Joseph', 'age': 21, 'marks': [90, 100, 70]},
                {'id': 3, 'name': 'Andrew', 'age': 19, 'marks': [80, 70, 75]},
                {'id': 4, 'name': 'James', 'age': 22, 'marks': [95, 65, 90]}]

def add_student(student_id, name, age, marks):
    students.append({'id': student_id, 'name': name, 'age': age, 'marks': marks})

def view_all_students():
    for student in students:
        print(student)

def search_student_by_id(id):
    for student in students:
        if student['id'] == id:
            return student
    return None

def update_student(student_id, name, age, marks):
    student = search_student_by_id(student_id)
    student['name'] = name
    student['age'] = age
    student['marks'] = marks

def delete_student(student_id):
    for i in range(len(students)):
        if students[i]['id'] == student_id:
            students.pop(i)
            return "Student removed successfully"
    return None

def calculate_average(student_id):
    student = search_student_by_id(student_id)
    marks = student['marks']
    return sum(marks)/len(marks)

def calculate_grade(average):
    if 100 >= average > 90:
        return "A"
    elif 90 >= average > 80:
        return "B"
    elif 70 >= average > 60:
        return "C"
    elif 60 >= average > 50:
        return "D"
    elif 50 >= average >= 35:
        return "E"
    else:
        return "F"

def display_top_students(n):
    avg_lst = []
    for student in students:
        avg = calculate_average(student['id'])
        avg_lst.append((avg, student['name']))
    avg_lst.sort(reverse=True)
    n = min(n, len(avg_lst))
    for i in range(n):
        print(f"{i + 1}. {avg_lst[i][1]} with average {avg_lst[i][0]:.2f}")

def display_statistics():
    print("Total number of students: ", len(students))
    avg = 0
    count = 0
    for student in students:
        avg += calculate_average(student['id'])
        count += 1
    print("Class average: ", avg/count)

def main():
    print('MENU\n'
          '1. Add Student\n'
          '2. View All Students\n'
          '3. Search Student\n'
          '4. Update Student\n'
          '5. Delete Student\n'
          '6. View Student Report\n'
          '7. View Top 3 Students\n'
          '8. View Class Statistics\n'
          '9. Exit')
    while True:
        try:
            choice = int(input('Enter your choice(1-9): '))
        except ValueError:
            print("Enter valid choice!!")
            continue
        if choice not in range(1, 10):
            print("Choice should be within 1-9")
            continue
        if choice == 9:
            print("Exiting....")
            break
        elif choice == 1:
            while True:
                try:
                    student_id = int(input('Enter student id: '))
                except ValueError:
                    print("Enter valid id")
                    continue
                if search_student_by_id(student_id) is not None:
                    print("Student already exists!!")
                else:
                    break
            name = input('Enter student name: ')
            while True:
                try:
                    age = int(input('Enter student age: '))
                except ValueError:
                    print("Not a valid age")
                    continue
                if age not in range(3, 100):
                    print("Enter Valid age")
                else:
                    break
            marks = []
            while True:
                try:
                    marks = list(map(int, input('Enter student marks list: ').split(',')))
                except ValueError:
                    print("Not valid marks")
                    continue
                all_valid = True
                for mark in marks:
                    if mark not in range(1, 101):
                        all_valid = False
                        print("Enter valid mark")
                        break
                if all_valid:
                    break
            add_student(student_id, name, age, marks)
            print("Student added successfully!!")
        elif choice == 2:
            view_all_students()
        elif choice == 3:
            while True:
                try:
                    student_id = int(input('Enter student id: '))
                    break
                except ValueError:
                    print("Enter valid id")
                    continue
            student = search_student_by_id(student_id)
            if student:
                print(student)
            else:
                print('ID does not exist!!')
        elif choice == 4:
            while True:
                try:
                    student_id = int(input('Enter student id: '))
                except ValueError:
                    print("Enter valid id")
                    continue
                if search_student_by_id(student_id) is None:
                    print("Student doesn't exist")
                else:
                    break
            name = input('Enter student name: ')
            while True:
                try:
                    age = int(input('Enter student age: '))
                except ValueError:
                    print("Not a valid age")
                    continue
                if age not in range(3, 100):
                    print("Enter Valid age")
                else:
                    break
            marks = []
            while True:
                try:
                    marks = list(map(int, input('Enter student marks list: ').split(',')))
                except ValueError:
                    print("Not valid marks")
                    continue
                all_valid = True
                for mark in marks:
                    if mark not in range(1, 101):
                        all_valid = False
                        print("Enter valid mark")
                        break
                if all_valid:
                    break
            update_student(student_id, name, age, marks)
            print("Student updated successfully")

        elif choice == 5:
            while True:
                try:
                    student_id = int(input('Enter student id: '))
                    break
                except ValueError:
                    print("Enter valid id")
                    continue
            result = delete_student(student_id)
            if result:
                print(result)
            else:
                print('ID does not exist!!')

        elif choice == 6:
            while True:
                try:
                    student_id = int(input('Enter student id: '))
                except ValueError:
                    print("Enter valid id")
                    continue
                if search_student_by_id(student_id) is None:
                    print("Student doesn't exist")
                else:
                    break
            avg = calculate_average(student_id)
            grade = calculate_grade(avg)
            print(f'Student with ID {student_id} has {avg} with grade {grade}')

        elif choice == 7:
            while True:
                try:
                    n = int(input("Enter your number: "))
                    break
                except ValueError:
                    print("Enter valid number")
                    continue
            display_top_students(n)

        elif choice == 8:
            display_statistics()

if __name__ == '__main__':
    main()
