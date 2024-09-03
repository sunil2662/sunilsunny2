# def my_function():
#     print("hi")
# my_function()
#
# def my_function(a,b):
#     print(a+b)
#     print(a*b)
# my_function(10,2)
#
# def function(name):
#     print("my name is " + name)
# function("sunil")

# food={1:"idly",2:"dosa",3:"bonda",4:"puri"}
# print(food)
# a=int(input("enter the least like food:"))
# if a in food:
#     food.pop(a)
# print(food)
#
# colors=["red","white","black","pink","porpule","brown","yellow","green","orange","blue"]
# print(colors)
# a=int(input("enter the num(0-4):"))
# b=int(input("enter the num(5-9):"))
# c=colors[a:b]
# print(c)
#
# num=[111,222,333,444]
# for x in num:
#     print(x)
# a=int(input("enter a num :"))
# if a in num:
#     c=num.index(a)
#     print(c)
# else:
#     print("that is not in the list")

# nums=[]
# for i in range(3):
#     a=int(input("enter a num:"))
#     nums.append(a)
#     print(nums)
# b=str(input("if you want add the last num?(yes/no):"))
# if b == "no":
#     nums.pop()
# print(nums)

# a=str(input("enter your name:"))
# b=str(input("enter your surname:"))
# print(f"hello {a} {b}")

# name=str(input("enter your name:"))
# age=int(input("enter your age:"))
# b=age+1
# print(f"{name} next birthday you will be {b} ")
#
# ask=int(input("enter total price:"))
# diners=int(input("enter how many diners:"))
# a = ask / diners
# print(f"each persoin must pay {a}")

# a=int(input("enter a num:"))
# b=int(input("enter a num:"))
# if a > b:
#     print(b,a)
# else:
#     print(a,b)
#
# a=int(input("enter a num (0-19):"))
# if a >= 20:
#     print("too high")
# else:
#     print("thank you")

# a=int(input("enter a num between(10-20):"))
# if a > 10 and a < 20:
#     print("thank you")
# else:
#     print("incorrect")

# a=str(input("if it is raining?(yes/no):"))
# if a == "yes":
#     b=str(input("if it is windy?(yes/no):"))
#     if b == "yes":
#         print("it is too windy for an umbrella")
#     elif b == "no":
#         print("take an umbrella")
# else:
#     print("enjoy your day")

# name=str(input("enter your name:"))
# print(len(name))

# def my_function(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
# my_function(5,2)

# def my_function():
#     print("hello")
# my_function()

# def my_function(name):
#     print("my name is "+name)
# my_function("sunil")

# def my_function(name="sravan"):
#     print("my name is "+name)
# my_function("sunil")
# my_function()
#
# def my_function(*name):
#     print("my name is "+name[1])
# my_function("sunil","sravan","sai")

# def my_function(**name):
#     print("my fname is "+name["lname"])
# my_function(fname="sunil",lname="naikoti")

# def myfun(a,b):
#     print(a+b)
#     if a<b:
#         print("thank you")
#     else:
#         print("nice")
# myfun(2,5)

# def myfun(a):
#     print(a)
#     if a < 20:
#         print("hello")
#     else:
#         print("hiii")
# myfun(a=int(input("enter  num:")))
#
# def myfunc(a):
#     for i in a:
#         print(i)
# myfunc(str(input("enter a name:")))
# myfunc(str(input("enter a name:")))

# def myfun(a):
#     for i in range(a):
#         print(i)
# myfun(10)
#
# def myfunc(a):
#     i=0
#     while i < a:
#         i += 1
#         print(i)
# myfunc(5)


# def myfunc(name):
#     print("my name is ",name)
# myfunc("sunil")

# def my(name="sravan"):
#     print("my name is ",name)
# my("sunil")
# my()

# def myfunc(a):
#     for i in range(a):
#         print(i)
# myfunc(5)
#
# FUNCTION TASK--1:
#
# def check_balance():
#     print(f"your balance is {balance:.2f}:")
# def deposit():
#     amount=float(input("enter your amount:"))
#     if amount < 0:
#         print("amount will be greater than 0")
#         return 0
#     else:
#         return amount
#
# def withdraw():
#     amount=float(input("enter the amount:"))
#     if amount < 0:
#         print("amount will be greater than 0")
#         return 0
#     elif amount > balance:
#         print("insufficient balance")
#         return 0
#     else:
#         return amount
#
# balance = 0
# is_running = True
# while is_running:
#     print("WELL COME TO HDFC")
#     print("1.check_balance")
#     print("2.deposit")
#     print("3.withdraw")
#     print("4.exit")
#     a=int(input("enter a num:"))
#     if a == 1:
#         check_balance()
#     elif a == 2:
#         balance+=deposit()
#     elif a == 3:
#         balance-=withdraw()
#     elif a == 4:
#         is_running=False
#     else:
#         print("invalid operation")
# print("visit again")

# FUNCTION TASK--2:

# def addition():
#     a=int(input("enter a num:"))
#     b=int(input("enter a num:"))
#     c=a+b
#     print(f"the addition is: {c}")
# def subtraction():
#     a = int(input("enter a num:"))
#     b = int(input("enter a num:"))
#     d=a-b
#     print("the subtraction is",d)
# def multi():
#     a = int(input("enter a num:"))
#     b = int(input("enter a num:"))
#     e = a*b
#     print("the multiplication of 2 num is ",e)
# def division():
#     a = int(input("enter a num:"))
#     b = int(input("enter a num:"))
#     f = a/b
#     print("the division is ",f)
#
# is_running = True
# while is_running:
#     print("WELL COME TO THE MATHS CLASS")
#     print("1.addition")
#     print("2.subtraction")
#     print("3.multi")
#     print("4.division")
#     print("5.exit")
#     choice=int(input("enter any operation:"))
#     if choice == 1:
#         addition()
#     elif choice == 2:
#         subtraction()
#     elif choice == 3:
#         multi()
#     elif choice == 4:
#         division()
#     else:
#         print("malli raku osthe chasthav")

# def myfunc():
#     a=int(input("enter a factorial num:"))
#     fact = 1
#     if a < 0:
#         print("a must be greater than 0")
#     else:
#         for i in range(1,a+1):
#             fact=fact*i
#             print(fact)
# myfunc()
#
# def myfunc():
#     a=int(input("enter any num:"))
#     x = a
#     r=0
#     while a > 0:
#         c=a%10
#         r=r+c*c*c
#         a=a//10
#     if x == r:
#         print(r,"it is armstrong num")
#     else:
#         print(r,"it is not a armstrong num")
# myfunc()

# def myfunc():
#     name=str(input("enter any name:"))
#     for i in name:
#         print(i)
# myfunc()
#
# def myfun():
#     name=str(input("enter any name:"))
#     len(name)
#     if len(name)%2 == 0:
#         print("hello")
#     else:
#         a=len(name)//2
#         print(name[a])
# myfun()
#
# def myfun():
#     a=int(input("enter the num:"))
#     print("even num")
#     for i in range(a):
#         if i%2 == 0:
#             print(i)
#         else:
#             pass
# myfun()
#
# def myfun(*name):
#     print(list(name))
#     for i in name:
#         # print(i)
#         y=name.index(i)
#         print(i,y)
# myfun("sunil","sravan","dileep")

# def myfunc(*num):
#     e=len(num)
#     if e%2 == 0:
#         x=(num[e//2-1]+num[e//2])/2
#         print(x)
#     else:
#         a=num[e//2]
#         print(a)
# myfunc(1,5,5,8,6,8,5,8,5,6)


#
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(self):
#     print("Hello my name is " , self.name)
#     print("my age is ",self.age)
#
# p1 = Person("sunil", 22)
# p1.myfunc()

# class man:
#     x=5
# a=man()
# print(a.x)





