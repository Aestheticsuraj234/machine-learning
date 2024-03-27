# age = 9
# if age == 9:
#     print("age is 9")
# elif age < 9:
#     print("age is less than 9")
# else:
#     print("age is not 9")


marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
else:
    print("Fail")
