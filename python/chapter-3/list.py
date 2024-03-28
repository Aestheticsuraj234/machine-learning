mrks1 = 94.4
marks2 = 87.7
marks3 = 95.6
marks4 = 66.89
marks5 = 78.32



marks = [mrks1, marks2, marks3, marks4, marks5]
print(type(marks))

# slicing
print(marks[0:3])
print(marks[1:4])
print(marks[2:])  # from 2nd index to end
print(marks[:3])  # from start to 3rd index
print(marks[-1])  # last element
print(marks[-2])  # second last 

# SOME FUNCTIONS
list = [1, 2, 3, 4, 5]
list.append(4)
print(list)
list.sort(reverse=True)
print(list)