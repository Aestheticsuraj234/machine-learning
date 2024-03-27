# str1 = "this is a string \n this is a new line"
# str2='ApnaCollege'
# str3='''This is a multiline string'''

# # basic operations on strings

# # concatenation
# print(str1 + str2)

# # length of string
# print(len(str1))




# indexing
# str = "SIGMA_DEVELOPER"  # 0(S) 1(I) 2(G) 3(M) 4(A) 5(_) 6(D) 7(E) 8(V) 9(E) 10(L) 11(O) 12(P) 13(E) 14(R)


# slicing
# print(str[0:5])  # SIGMA
# print(str[6:])   # DEVELOPER
# print(str[:5])   # SIGMA
# print(str[:])    # SIGMA_DEVELOPER
# print(str[-1])   # R
# print(str[-3:])  # PER
# print(str[:-3])  # SIGMA_DEVELOP


STR_1 = "i am a developer and I am learning python"
# print(STR_1.endswith("on"))  # True
print(STR_1.capitalize())  # I am a developer and i am learning python
print(STR_1.replace("am", "was"))  # i was a developer and I was learning python
print(STR_1.find("am"))  # 2
print(STR_1.count("i"))


first_name = input("Enter your first name: ")
print(len(first_name))