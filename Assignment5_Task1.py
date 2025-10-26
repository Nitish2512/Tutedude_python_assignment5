student_dict = {"Alice": 95, "John" : 86, "Bob" : 85, "Smith" : 87, "Mona" : 90}
print(student_dict)

input_name = input("Enter the student name: ").strip().lower()

student_dict_lower = {name.lower(): marks for name, marks in student_dict.items()}
if input_name in student_dict_lower:
    print(f"{input_name.title()}'s marks: {student_dict_lower[input_name]}")
else:
    print("Student not found")