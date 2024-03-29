info = {
    "name": "apna",
}

print(info["name"])  # Output: apna
info["name"] = "apna college"
info["age"] = 20

print(info)  # Output: {'name': 'apna college', 'age': 20}


student = {
    "name": "Rahul",
    "subjects": ["Maths", "Science", "English"],
    "marks": {"Maths": 70, "Science": 80, "English": 90},
    "is_passed": True,
    "is_failed": False,
}

print(student)  # Output: {'name': 'Rahul', 'subjects': ['Maths', 'Science', 'English'], 'marks': {'Maths': 70, 'Science': 80, 'English': 90}, 'is_passed': True, 'is_failed': False}

print(student["name"])  # Output: Rahul
print(student["marks"]["Maths"])  # Output: Rahul


print(student.keys())



