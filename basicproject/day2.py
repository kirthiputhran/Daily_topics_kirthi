# import os
# import subprocess

# def listdir(dir):
#   cmd = 'ls -l ' + dir
#   print("Command to run:", cmd)   ## good to debug cmd before actually running it
#   (status, output) = subprocess.getstatusoutput(cmd)
#   if status:    ## Error case, print the command's output to stderr and exit
#     sys.stderr.write(output)
#     sys.exit(status)
#   print (output) 

# def main():
# 	listdir('mysite')

# if __name__ == '__main__':
# 	main()
##############
# def main():
# 	for i in range(1,11):
# 	    print(i)
# 	    if i == 5:
# 	        break

# if __name__ == '__main__':
#  	main()
##############
# website = "apple.com"
# print(website)										# assigning a new value to website
# website = "programiz.com"
# print(website)
############

# a, b, c = 5, 3.2, "Hello"
# print (a)
# print (b)
# print (c)
############

# a=b=c='kirthi'
# print (a)
# print (b)
# print (c)
##########

# a=dict([[1,2],[3,4]])
# print(a)

# b=dict([(3,26),(4,44)])
# print(b)
###########
# x = 5; y = 10
# print('The value of x is {} and y is {}'.format(x,y))
# print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

###########
# n=input("Enter the number:")
# print(n)

##########
# p=eval('2+3')
# print(p)
########

# import math
# print(math.pi)
########
# x=15
# y=4
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y)
#########
# x=15
# y=4
# print(x<y)
# print(x>y)
# print(x==y)
# print(x!=y)
# print(x<=y)
# print(x>=y)
#########
# x=True
# y=False
# print(x and y)
# print(x or y)
# print(not y)
############
# x=10
# y=4
# print(x & y)
# print(x | y)
# print(x ^ y)
# print(-y)
# print(y>>2)
# print(y<<2)
#########

# def printHello():
#     print("Hello")

# a = printHello()
###########
# def outer_function():
#     a = 20

#     def inner_function():
#         a = 30
#         print('a =', a)

#     inner_function()
#     print('a =', a)


# a = 10
# outer_function()
# print('a =', a)

#########
# Program to iterate through a list using indexing

# genre = ['pop', 'rock', 'jazz']
# for i in genre:
#     print("I like", i)

######
# program to display student's marks from record
# student_name = 'Soyuj'
# marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

# for student in marks:
#     if student == student_name:
#         print(marks[student])
#         break
# else:
#     print('No entry with that name found.')
##############

# n=10
# sum=0
# i=1
# for i in range(n+1):
# 	sum=sum+i;
# print(sum)
# ###########
# def greet(name, msg="Good morning!"):
#     print("Hello", name + ', ' + msg)

# greet("Kate")
# greet("Bruce", "How do you do?")
#############
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list)


# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x: x * 2 , my_list))
# print(new_list)
#############

# def foo():
#     y = "local"
#     print(y)
# foo()
###########
# x = "global "
# def foo():
#     global x
#     y = "local"
#     x = x * 5
#     print(x)
#     print(y)

# foo()
##########
# x = 5
# def foo():
#     x = 10
#     print("local x:", x)
# foo()
# print("global x:", x)

#########
# def foo():
#     x = 20

#     def bar():
#         global x
#         x = 25
    
#     print("Before calling bar: ", x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar: ", x)

# foo()
# print("x in main: ", x)
###########

# with open("foo2.txt","w") as f:
# 	f.write("My name is kirthi")
# 	f.write("I love Drawing")
###########
# with open("foo2.txt","a") as f:
# 	f.write(" and painting")
##########
# import os
# cur_dir=os.getcwd()
# print(cur_dir)

########
# num=10
# den=0
# print(num/den) 			#divide by zero

########
# try:
# 	num=int(input("Enter numerator:"))
# 	den=int(input("Enter denominator:"))
# 	result=num/den
# 	print(result)

# 	list=[1,2,3,4,7]
# 	i=int(input("Enter index"))
# 	print(list[i])

# except ZeroDivisionError:
# 	print("denominator cannot be zero")

# except IndexError:
# 	print("Index is greater than the size of list")
# print("Program ends")

#############

# try:
# 	num=1/0
# except:
# 	print("denominator cannot be zero")

# finally:
# 	print("It gets printed always")

# import module sys to get the type of exception
# import sys

# randomList = ['a', 0, 4]

# for entry in randomList:
#     try:
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occurred.")
# print("The reciprocal of", entry, "is", r)
############
# a = int(input("Enter a positive integer: "))
# try:
#     if a <= 0:
#         raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print(ve)  
# else:
# 	print("Number is positive")
########
# num = int(input("Enter a number: "))
# try:
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)

#########

# class Error(Exception):								#Base class for other exceptions
#     pass


# class ValueTooSmallError(Error):					#Raised when the input value is too small
#     pass


# class ValueTooLargeError(Error):					#Raised when the input value is too large
#     pass

# number = 10
# while True:
#     try:
#     	i_num = int(input("Enter a number: "))
#         if (i_num < number):
#         	raise ValueTooSmallError
#         elif (i_num > number):
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError:
#         print("This value is too small, try again!")
#         print()
#     except ValueTooLargeError:
#         print("This value is too large, try again!")
#         print()

# print("Congratulations! You guessed it correctly.")
##############
# class Student:
# 	def check_pass(self):
# 		if self.marks>=40:
# 			return True
# 		else:
# 			return False
# s1=Student();
# s1.name='Kirthi'
# s1.marks=89
# did_pass =s1.check_pass()
# print(did_pass)

# s2=Student();
# s2.name='xysv'
# s2.marks=36

# did_pass =s2.check_pass()
# print(did_pass)
###########
# class Student:
# 	def check_pass(self):
# 		if self.marks>=40:
# 			return True
# 		else:
# 			return False

# 	def __init__(self,name,marks):				#automatically gets called when objects are created
# 		self.name=name
# 		self.marks=marks

# s1=Student("kirthi",89);
# print(s1.name)
# print(s1.marks)
# did_pass =s1.check_pass()
# print(did_pass)
# s2=Student("wsdf",34);
# print(s2.name)
# print(s2.marks)
# did_pass =s2.check_pass()
# print(did_pass)
############

# class complex:
# 	def __init__(self,real,imag):
# 		self.real=real
# 		self.imag=imag
# 	def add(self,num):
# 		real=self.real+num.real
# 		imag=self.imag+num.imag
# 		result=complex(real,imag)
# 		return result

# n1=complex(3,5)
# n2=complex(6,2)
# result=n1.add(n2)
# print(result.real)
# print(result.imag)

#############
# class Parrot:
# 	def __init__(self,name,age):
# 		self.name=name
# 		self.age=age

# 	def details(self,sec):
# 		print("Parrot {} is {} years old".format(self.name,self.age))
# 		print("Parrot {} is {} years old".format(sec.name,sec.age))

# b1=Parrot("poo",10)
# b2=Parrot("bzz",15)
# op=b1.details(b2)
########
# class Parrot:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)

#     def dance(self):
#         return "{} is now dancing".format(self.name)

# blu = Parrot("Blu", 10)
# print(blu.sing("'Happy'"))
# print(blu.dance())
############

# parent class
# class Bird:
    
#     def __init__(self):
#         print("Bird is ready")

#     def whoisThis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# # child class
# class Penguin(Bird):

#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")

#     def whoisThis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")

# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()

# class Computer:

#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Computer()
# c.sell()

# # change the price
# c.__maxprice = 1000
# c.sell()

# # using setter function
# c.setMaxPrice(1000)
# c.sell()
##########
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.no_of_sides = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.no_of_sides)]

#     def dispSides(self):
#         for i in range(self.no_of_sides):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)

#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)
# t=Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()



