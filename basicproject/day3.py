# class salarynotinrange(Exception):
# 	pass

# salary=int(input("Enter salary"))
# try:
# 	if not 5000 <salary <15000:
# 		raise salarynotinrange("Salary not between 5000 and 15000")

# except salarynotinrange as sn:
# 	print(sn)
# else:
# 	print("salary:",salary)
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
# b=Bird()
# b.whoisThis()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
###########
# class Parrot:
# 	def fly(self):
# 		print("parrot can fly")
# 	def swim(self):
# 		print("parrot cant swim")
# class Penguin:
# 	def fly(self):
# 		print("penguin cant fly")
# 	def swim(self):
# 		print("penguin can swim")

# def flying(bird):
# 	bird.fly()

# b1=Parrot()
# b2=Penguin()
# flying(b1)
# flying(b2)
#############

# num=[1,2,5]
# value=iter(num)
# item1=next(value)
# print(item1)
# item2=next(value)
# print(item2)
# item3=next(value)
# print(item3)
##########
# num=[1,6,3,9]
# val=iter(num)
# while(True):
# 	try:
# 		item=next(val)
# 		print(item)
# 	except StopIteration:
# 		break

# num=[1,5,2,8,4]
# val=iter(num)
# for ele in val:
# 	try:
# 		print(ele)

# 	except StopIteration:
# 		break

# class Even:
# 	def __init__(self,max):
# 		self.n=2
# 		self.max=max

# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		if self.n<=self.max:
# 			res=self.n
# 			self.n=self.n+2
# 			return res
# 		else:
# 			raise StopIteration

# num=Even(9)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))

###########
# class pow:
# 	def __init__(self,max):
# 		self.n=0
# 		self.max=max

# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		if self.n<=self.max:
# 			res=2 ** self.n
# 			self.n=self.n+1
# 			return res
# 		else:
# 			raise StopIteration

# num=pow(4)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
#############
# def evengen(max):
# 	n=0;
# 	while(n<=max):
		
# 		yield n
# 		n=n+2
# num=evengen(5)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
############
# def fibgen(n):
# 	n1=0
# 	n2=1
# 	while (True):
# 		if n1<n:
# 			yield n1
# 			n1,n2=n2,n1+n2


# num=fibgen(10)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
###########
# def rev(str):
# 	s=str[::-1]
# 	yield s

# r=rev("kirthi")
# print(next(r))
###########
# def rev(str):
# 	l=len(str)
# 	for i in range(l -1,-1,-1):
# 		yield str[i]

# for i in rev("kirthi"):
# 	print(i)
###########

# list=[1,2,6,3,9,4]
# lc=[x*x  for x in list]
# gen=(x*x for x in list)

# print(lc)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
##########
# list=[1,2,6,3,9,4]
# gen=sum(x*x for x in list)
# gen1=max(x*x for x in list)

# print(gen)
# print(gen1)
##########
# def pow(max):
# 	n=0;
# 	while n<=max:
# 		res=2** n
# 		n=n+1
# 		yield res
# num=pow(4)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
#########
# def even(max):
# 	n=0;
# 	while n<=max:
# 		yield n
# 		n=n+2
		
# num=even(10)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
##########

# def fibonacci_numbers(nums):					#######doubt
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x+y
#         yield x

# def square(nums):
#     for num in nums:
#         yield num**2

# print(sum(square(fibonacci_numbers(10))))
#############
# def printmsg(msg):				#non local variable in nested function

# 	def printer():
# 		print(msg)
# 	printer()

# printmsg("kirthi")
##########

# def print_msg(msg):

#     def printer():
#         print(msg)
#     return printer()  				# returns the nested function
# another = print_msg("Hello")
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier

# # Multiplier of 3
# times3 = make_multiplier_of(3)
# # Multiplier of 5
# times5 = make_multiplier_of(5)
# # Output: 27
# print(times3(9))
# # Output: 15
# print(times5(3))
# # Output: 30
# print(times5(times3(2)))

# #############
# def inc(x):
# 	return x+1
# def dec(x):
# 	return x-1

# def operate(fun,x):
# 	res=fun(x)
# 	return res

# a=operate(inc,6)
# print(a)
# a=operate(dec,6)
# print(a)
##########
# def printmsg(msg):				#non local variable in nested function
# 	greet="Hello"
# 	def printer():
# 		print(greet,msg)
# 	printer()
# printmsg("kirthi")
###########
# def printer():
# 	print("Hello World")
# def decfun(func):
# 	def inner():
# 		print("Starting "+func.__name__+" function")
# 		func()
# 		print("End of function")
# 	return inner

# a=decfun(printer)
# a()
#########
# def decfun(func):
# 	def inner():
# 		print("Starting "+func.__name__+" function")
# 		func()
# 		print("End of function")
# 	return inner
# @decfun														#@decorater function  near the function which we want to pass as arguement
# def printer():
# 	print("Hello World")
# printer()
#############
# def smartdiv(func):
# 	def inner(a,b):
# 		if b==0:
# 			print("divideby zero error")
# 		else:
# 			res= func(a,b)
# 			return res
# 	return inner

# @smartdiv
# def divide(a,b):
# 	return a/b
# d=divide(6,2)
# print(d)
# d=divide(5,5)
# print(d)
# d=divide(34,0)
#########

# def smartdiv(func):
# 	def inner(a,b):
# 		try:
# 			res= func(a,b)
# 			return res	
# 		except ZeroDivisionError:
# 			print("Divide by zero is not allowed")
			

# 	return inner

# @smartdiv
# def divide(a,b):
# 	return a/b
# d=divide(6,2)
# print(d)
# d=divide(5,5)
# print(d)
# d=divide(34,0)
##########
# def star(func):
# 	def inner(arg):
# 		print("*"*30)
# 		func(arg)
# 		print("*"*30)
# 	return inner
# def percent(func):
# 	def inner(arg):
# 		print("%"*30)
# 		func(arg)
# 		print("%"*30)
# 	return inner

# @star
# @percent
# def msg_fun(msg):
# 	print(msg)

# msg_fun("Hi How are you")

# class celcius:
# 	def __init__(self,temp):
# 		self.temp=temp
# 	def faranheit(self):
# 		res=(self.temp*1.8)+32
# 		return res

# human=celcius(37)
# f=human.faranheit()
# print(f)
############
# import re
# pattern = '^a..s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	
############

import datetime

# datetime_object = datetime.datetime.now()			#current date and time
# print(datetime_object)

# date_object = datetime.date.today()				#current date
# print(date_object)

# d = datetime.date(2019, 4, 13)						#create date
# print(d)

# today = datetime.date.today() 						
# print("Current year:", today.year)					#current year
# print("Current month:", today.month)					#current month
# print("Current day:", today.day)						#current date


# b =datetime.time(11, 34, 56) 							#create time 
# print("b =", b)

# d = datetime.time(11, 34, 56, 234566)
# print("d =", d)

# a = datetime.time(11, 34, 56)
# print("hour =", a.hour)
# print("minute =", a.minute)
# print("second =", a.second)
# print("microsecond =", a.microsecond)

# a = datetime.datetime(2018, 11, 28)
# print(a)

# b = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
# print(b)

# t1 = datetime.date(year = 2018, month = 7, day = 12)
# t2 = datetime.date(year = 2017, month = 12, day = 23)
# t3 = t1 - t2
# print("t3 =", t3)

# t4 = datetime.datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime.datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)

# t1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
# t3 = t1 - t2
# print("t3 =", t3)

# local = datetime.datetime.now()
# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# date_string = "21 June, 2018"
# print("date_string =", date_string)
# date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)

list=[]
n=int(input())

for i in range(n):
	print("Enter index",i)
	item=int(input())
	list.append(item)
print(list)














