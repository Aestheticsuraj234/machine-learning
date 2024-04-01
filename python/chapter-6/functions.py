# # make functions in pyton
# def Calc_Sum(a,b):
#     sum = a+b
#     return sum
# print(Calc_Sum(2,3))

# cities = ['delhi' , 'bengaluru' , 'gurgaon' , 'hyedrabad']

# def print_len(city):
#      print(len(city))


# def print_city(city):
#     for item in list:
#         print(item)


n = 5

# for i in range(1 , n+1):
#     fact *= i
# print(fact)


# def cal_fact(n):
#     fact = 1
#     for i in range(1 , n+1):
#         fact *= i
#     return fact


# print(cal_fact(5))


def isOdd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


isOdd()


def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)

show(5)

def calc_sum(n):
    if(n==0):
        return
    print(n)
    calc_sum(n-1) + n
    

calc_sum(5)    


def print_list(list , idx):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list , idx + 1)


print_list([1,2,3,4,5] , 0)    