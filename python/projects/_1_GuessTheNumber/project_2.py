import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""

#list comprehension
password = "".join(random.choice(charValues) for i in range(pass_len))

# for i in range(pass_len):
#     password += random.choice(charValues)
    

print("Your Random Password is:", password)    