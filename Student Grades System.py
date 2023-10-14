student_names = []
student_grades = {}
while True:
    print("_____Student Grades System_____")
    print("")
    print("1.Add a Student")
    print("2.View Student Grades")
    print("3.Calculate Average Grade")
    print("4.Exit")
    
    choice = input("Enter your choice (1) (2) (3) (4): ")
    
    if choice == "1":
        student_name = input("Enter student's name:")
        ENGLISH_grade = float(input("Enter ENGLISH grade:"))
        SCIENCE_grade = float(input("Enter SCIENCE grade:"))
        MATH_grade = float(input("Enter MATH grade:"))
        
        student_names.append(student_name)
        student_grades[student_name] = {
            'ENGLISH': ENGLISH_grade,
            'SCIENCE': SCIENCE_grade,
            'MATH': MATH_grade
        }
    
    elif choice == "2":
        student_name = input("Enter student's name: ")
        if student_name in student_names:
            print("Grades for "+student_name + ":")
            for subject, grade in student_grades[student_name].items():
                print(subject + ": " + str(grade))
        else:
            print("Student not found.")
    
    elif choice == "3":
        student_name = input("Enter student's name: ")
        if student_name in student_names:
            grades = student_grades[student_name]
            average_grade = sum(grades.values()) / len(grades)
            print("Average grade for " + student_name + ": " + "%.2f" % average_grade)

        else:
            print("Student not found.")
    
    elif choice == "4":
        print("Exit Program.")
        break
    
    else:
        print("Invalid. Please enter a valid option (1) (2) (3) (4).")
