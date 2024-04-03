# # class Students:
# #     __acc_password = 23
# #     def  __init__(self , name):
# #         self.name = name;
# #     def __reset_pass(self):
# #         print(self.__acc_password)


# # s1 = Students("Suraj")
# # del s1
# # print(s1.name)

# class Person:
#     __name = "anonymous"


# p1 = Person()
# print(p1.__name)


# Inheritance


class Car:
    color = "#000"

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("Porshe")


print(car1.start())
