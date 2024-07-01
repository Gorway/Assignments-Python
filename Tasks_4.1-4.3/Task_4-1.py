students_grades = {
    "Ani": 90,
    "Hayk": 85,
    "Tigran": 98,
    "Artak": 80
}


def update_grade(students, student_name, new_grade):
    if student_name in students:
        students[student_name] = new_grade
        print(f"Student grade {student_name} changed to {new_grade}.")
    else:
        print(f"Student with name {student_name} not found.")

def delete_student(students, student_name):
    if student_name in students:
        del students[student_name]
        print(f"Student {student_name} deleted.")
    else:
        print(f"Student with name {student_name} not found.")


print("Students grades:")
for student, grade in students_grades.items():
    print(f"{student}: {grade}")

update_grade(students_grades, "Artak", 95)

delete_student(students_grades, "Hayk")

print("Updated stuents grades:")
for student, grade in students_grades.items():
    print(f"{student}: {grade}")
