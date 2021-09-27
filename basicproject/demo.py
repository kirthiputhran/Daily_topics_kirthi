# a = 10
# print(a).    #print integer 10

##########
# a = 'HI'
# print(a).    #print string hi

##########
# a = 'Hello'
# print(len(a))   #length of string 5

###########
# a = 'Hello'
# print(a +' '+ str(len(a))) 	# print hello 5,(convert len to string to concatinate)

###########
# a = 'Hello'
# print(a +' '+ str(9))		#print hello 9

############
# def main():						# it need not be main ,can be anything eg:add
# 	print ("Hello Kirthi")		#main function it prints hello kirthi

# if __name__ == '__main__':		#boilerplate function that calls main function
# 	main()						#incase add give add instead of main

###########
# import sys						# os interpret type like coomand line arguements

# def main():						
# 	print (sys.argv)				#argv used for command line arguements

# if __name__ == '__main__':																	
# 	main()	

#############
# from math import sqrt

# a=sqrt(25)
# print(a)						# print 5 i.e sqroot of 25 

###########
 #import sys				
# dir(sys)						#Defines quick list of its defined symbols or attributes(terminal)
#help(len)  					# for help give q to exit
# help(sys)
# help(sys.exit)

##########	

# def repeat(s,exclaim):
											
# 	result=s + s 										

# 	if exclaim:
# 		result = result + '!!!'
# 	return result
# def main():
# 	print repeat('kirthi',True)
# 	print repeat('neshma',False)


# if __name__ == '__main__':
# 	main()

##############

# import sys
# def Hello(name):
# 	if name =='kirthi' or name =='neshma':
# 		name= name + "!!!"
# 	else:
# 		name= name
# 	print ("HELLO",name)

# def main():
# 	Hello(sys.argv[1])

# if __name__ == '__main__':
# 	main()
#################

# a="I \"love\"this exercise"    	#backslash to remove special meaning
# print (a)
#################
# a=" Hello World"
# b=['kir','thi']
# print(a.lower())					#lowercase
# print(a.upper())					#Uppercase
# print(a.find('e'))					#returns index of that character
# print(a[5])							#returns char of that index
# print(a[1])
# print(a.strip())					#removes whiespace from start and end
# print(a.isalpha())					# checks if its in char class
# print(a.isdigit())
# print(a.isspace())
# print(a.replace('World','kirthi'))    #replace old with new
# print(a.split(' '))					#splits when ' '
# print(a.join(b))					#joins b and a
# print(a)							#actual string

################

# a='Hi %s has %d pens' %('kirthi',5)    #passing values throrugh construct %
# print(a)
###############

# a="Hello"					#slicing
# print(a[1])
# print(a[-1])
# print(a[1:4])
# print(a[1:])
# print(a[:])
#print(a[-1:-4])

#############
# pi = 3.14
# t = 'The value of pi is '  + str(pi)		#convert int to str
# print(t)
##############

# raw = "this\t\n and that"          #op:this
# 								   # and that
# print raw
############

# multi = """It was the best of times.\n\tIt was the worst of times."""    #extra ""
# print(multi)

###########

# t = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')		 # % operator
# print(t)

#########

# t= (
#     "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down."			# Add parentheses to make the long line work:
#     % (3, 'huff', 'puff', 'house'))
# print(t)

#########
 
# t = (
#     "%d little pigs come out, "										# Split the line into chunks, which are concatenated automatically by Python
#     "or I'll %s, and I'll %s, "
#     "and I'll blow your %s down."
#     % (3, 'huff', 'puff', 'house'))
# print(t)

############

# u = u'A unicode \u018e string \xf1'					#unicode
# print(u)

########
# def speedfn(speed):
# 	if speed >= 80: 
# 		print ("You are so busted")                         #################
# 	else: 
# 		print ('Have a nice day')
# def main():
# 	speedfn(90)
# 	speedfn(50)

# if __name__ == '__main__':
#  	main()
###################
# def speedfn(speed,mood):
# 	if speed >= 80:
# 	    print 'License and registration please'
# 	    if mood == 'terrible' or speed >= 100:
# 	      print 'You have the right to remain silent.'
# 	    elif mood == 'bad' or speed >= 90:
# 	      print "I'm going to have to write you a ticket."
# 	    else:
# 	      print "Let's try to keep it under 80 ok?"

# def main():
# 	speedfn(90,'terrible')
# 	speedfn(80,'good')
# 	speedfn(110,'good')

# if __name__ == '__main__':
#  	main()
##################
# c=['yellow','pink','green']
# print(c)
# print(c[2])
# print(len(c))

# b=c
# print(b)

##############
# square=[1,4,6,8]
# sum=0
# for num in square:
# 	sum=sum+num
# print(sum)

#########
# list=['kirthi','puthran']
# if 'kirthi' in list:
# 	print ("present")
# else:
# 	print("Not present")
#########

# for i in range(1,101):				#1 to 100
# 	print(i)

########
# a="Hello World"							#access every 3 elements
# i=0;
# while(i <len(a)):
# 	print(a[i])
# 	i =i+3;

############
# list=['kirthi','neshma','swati']
# print(list)

# list.append('lishel')
# list.insert(2,'vrinda')
# list.extend(['anjali','sahana'])
# print(list)

# print(list.index('anjali'))

# list.pop(2)
# list.remove('anjali')
# print(list)

#########
# list=[1,2,3]
# list.append(4)
# print(list)

#########
# list=[]
# list.append('a')
# list.append('b')
# print(list)
########

# list=['a','b','c','d']
# print(list[1:-1])
# list[0:2]='x'
# print(list)

###########

# a=[3,9,4,5,1,2]
# print(sorted(a))

# b=['aa','kir','XYZ','thi','AAA','neshu']
# print(sorted(b))
# print(sorted(b,reverse=True))
# print(sorted(b,key=len))
# print(sorted(b,key=str.lower))					# force to treat upper case and lower case same

# str=['kir','thi','swati','neshu']

# def myfn(s):
# 	return s[-1]


# print(sorted(str,key=myfn))
##########
# list=[5,7,1,2,3]
# list.sort()
# print(list)
#########

# t=(5,2,4,'hi')
# print(t)
# print(t[2])
#############


# (x,y,z)=('kir','thi','neshu')
# print(x)
# print(y)
# print(z)

############

# num=[1,3,4,2]
# square=[n*n  for n in num]
# print(square)

############
# str=['kir','thi','swati','neshu']
# up=[s.upper() +'!!!'  for s in str]
# print(up)

###########
# num=[5,2,8,4,1]
# small=[ n for n in num if n<=4]
# print(small)

##########
# fruits=['apple','banana','mango','kiwi','muskmelon']
# capf=[f.upper()  for f in fruits if 'a' in f]
# print(capf)

##########

# dict={'a':'kirthi','b':'neshu'}
# print(dict)

# print(dict['a'])
# dict['a']=6
# print(dict)

# if 'z' in dict:
# 	print(dict['z'])
# print dict.get('z')

########

# dict={}
# dict['a']='kirthi'
# dict['b']='neshu'
# print(dict)
#######

# dict={'b':'neshu','a':'kirthi'}
# for key in dict:
# 	print(dict[key])

# for key in dict:
# 	print (key)

# for key in dict.keys():
# 	print (key)

# print(dict.keys())
# print(dict.values())

# for key in sorted(dict):
# 	print (key,dict[key])

# print(dict.items())

# for k,v in dict.items():
# 	print(k+">"+v)

#########

# hash={}
# hash['word']='kirthi'
# hash['count']=50
# s= "I have written %(word)s in my book %(count)d times" %(hash)
# print (s)

#########
# list=[1,6,3,2,9,7,8]
# del list[2]
# print(list)
# del list[1:3]
# print(list)

########
# dict={'b':'neshu','a':'kirthi'}
# del dict['b']
# print(dict)

#########

# f= open('foo1.txt','rU')
# for line in f:
# 	print(line)
# f.close()
# 
# import re
# str="Hello World Hello World Hello World"
# reg=re.search("Worl\w",str)
# print(reg)
# print(reg.span())
# print(reg.group())
# print(reg.string)

# str='An example word:cat'
# match=re.search('word:\w\w\w',str)
# if match:
# 	print(match.group())
# else:
# 	print("Not found")


# f= open('foo1.txt','rU')
# for line in f:
# 	match=re.search('are.*',line)
# 	if match:
# 		print(match.group())
# f.close()

###############

# match=re.search('iii','piiiing')
# if match:
#  	print(match.group())

# match=re.search('iigs','piiiing')
# if match:
#  	print(match.group())
# else:
# 	print("Not present")
###############

# match=re.search('i.g','piiiing')
# if match:
#  	print(match.group())

###############
# match = re.search('\d\d\d', 'p123g') 
# if match:
#   	print(match.group())
##############
# match = re.search('\w\w\w', '@@abcd!!')
# if match:
#   	print(match.group())
##############

# match=re.search('i+','piiing')				#occurance of i
# if match:
#   	print(match.group())
############
# match=re.search('pi+','piiing')				#occurance of i
# if match:
#   	print(match.group())
###########
# match = re.search('\d\s*\d\s*\d', 'xx1 2   3xx')
# if match:
#   	print(match.group())
###########
# match = re.search('\d\s*\d\s*\d', 'xx12  3xx')
# if match:
#   	print(match.group())

###########
# match = re.search('\d\s*\d\s*\d', 'xx123xx')
# if match:
#   	print(match.group())
##########

# match = re.search('^b\w+', 'foobar')
# if match:
# 	print(match.group())

# match = re.search('b\w+r$', 'foobar')
# if match:
# 	print(match.group())


# str='keerthy-puthran@gmail.com'
# match=re.search('\w+@\w+',str)
# if match:
#  	print(match.group())


# str = 'purple alice1999-b@google.com monkey dishwasher'
# match = re.search(r'[\w.-]+@[\w.-]+', str)
# if match:
#     print match.group()

# str = 'purple alice-b@google.com monkey dishwasher'
# match = re.search('([\w.-]+)@([\w.-]+)', str)
# if match:
#     print match.group()   
#     print match.group(1)  
#     print match.group(2) 

# str='kirti@com and swati@com' 
# match=re.findall('[\w.-]+@[\w.-]+',str)
# for f in match:
# 	print(f)

# f=open('foo1.txt','r')
# match=re.findall('Kirthi',f.read())
# print(match)

# str = 'purple alice-b@google.com monkey dishwasher'
# match = re.findall('([\w.-]+)@([\w.-]+)', str)
# for i in match:
# 	print(i)
# 	print (i[0])
# 	print (i[1])

# import re
# str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# match=re.sub(r'([\w\.-]+)@([\w\.-]+)',r'\1@gmail.com',str)
# print(match)

# def reverse(str):
# 	s=str[::-2]
# 	return s
# str='kirthi'
# print(reverse(str))
import os
import subprocess
## Example pulls filenames from a dir, prints their relative and absolute paths
# def printdir(dir):
#   filenames = os.listdir(dir)
#   for filename in filenames:
#     print filename  ## foo.txt
#     print os.path.join(dir, filename) ## dir/foo.txt (relative to current dir)
#     print os.path.abspath(os.path.join(dir, filename)) ## /home/nick/dir/foo.txt

def listdir(dir):
  cmd = 'ls -l ' + dir
  print ("Command to run:", cmd)   ## good to debug cmd before actually running it
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print (output)

def main():
	listdir('mysite')

if __name__ == '__main__':
  	main()









