

#1.what is inheritance? how amny types are there and write examples?
# inheritance:acquiring the properties of one class to another class is called inheritance
# types of inheritance: single inheritnce, heirarchical inheritance,multi-level inheritance, multiple inheritance, and
# hybrid inheritance
#single inheritance: inheriting the properties of one class to another class is called single inheritance
# class v:
#     def A(self):
#         print("assignment")
# class k(v):
#     def B(self):
#         print("submitted")
#k=k()
# k.A()
# k.B()
# o/p:
# assignment
#submitted
print('ma')
#multi level inheritance: the concept of inheriting the properties n from multiple classes to single class with the
# concept of one after another is known as multilevel inheritance

# multi level inheritance:
# class A:
#     def P(self):
#         print('python python')
# class B(A):
#     def Q(self):
#         print("java java")
# class C(B):
#     def R(self):
#         print("hello hello")
# class D(C):
#     def S(self):
#         print("hi people")
# obj=D()
# obj.P()
# obj.Q()
# obj.R()
# obj.S()
# o/p:
# python python
# java java
# hello hello
#hi people

#heirarchical inheritance: the concept of inheriting properties from one class to another class into multiple classes
# which are present at same level is knoown as heirarchical inheritance

# class JAVA():
#     def A(self):
#         print("mr.cool")
# class python(JAVA):
#     def B(self):
#         print("ms dhoni")
# class coffee(JAVA):
#     def C(self):
#         print("forever captain")
# obj=JAVA()
# obj.A()
# python=python()
# python.B()
# python.A()
# coffee_c=coffee()
# coffee_c.C()
# coffee_c.A()
# o/p:
# mr.cool
# ms dhoni
# mr.cool
# forever captain
# mr.cool

#multiple inheritance: the concept of inheriting the properties from multiple classes into a single class at a  time, is
#known as multople inheritance
# class A:
#     def X(self):
#         print(123)
# class B:
#     def Y(self):
#         print(20.0)
# class c(A,B):
#     def Z(self):
#         print("string")
# obj=c()
# obj.X()
# obj.Y()
# obj.Z()
# o/p:
# 123
# 20.0
# string

#hybrid inheritance: combination of more than one inheritance is called hybrid inheritance
# class JAVA():
#     def A(self):
#         print("mr.cool")
# class python(JAVA):
#     def B(self):
#         print("ms dhoni")
# class coffee(JAVA):                                #multilevel+single
#     def C(self):
#         print("forever captain")
# class tea(coffee):
#     def D(self):
#         print("bhuvi")
#
# # obj=JAVA()
# # obj.A()
# # python=python()
# # python.B()
# python.A()
# coffee=coffee()
# # coffee.C()
# # coffee.A()
# obj_D=tea()
# obj_D.D()
# obj_D.A()
# obj_D.C()

# class v:
#     def A(self):
#         print("assignment")
# class k(v):
#     def B(self):
#         print("submitted")
# class J(k,v):
#     def C(self):
#         print ("error")
# obj=J()
# obj.A()
# obj.B()
# obj.C()
# o/p:
# assignment
# submitted
# error


#2. what is polymorphism write an example?
# polymorphism:An entity which represents in multiple forms is called polymorphism
# ex: '+' operator acts as concenation and also as arthematic addition operator
# a=2
# b=3
# print(a+b)
# x='python'
# y='c++'
# print(x+y)
# o/p:
# 5
# pythonc++


#3.does function overloading is possible in python if no how many ways u can achieve function overloading?
#function overloading is not directly possible in python but we can achieve function overloading by defining a special
# method in class definition
#by default argument and variable length argument we can achieve function overloading
# class X:
#     def subt(self,a=None,b=None,c=None,d=None):
#         print(a,b,c,d)
#         if a!=None and b!=None and c!=None and d!=None:
#             print("subtract the 4 numbers:",a-b-c-d)
#         elif a!=None and b!=None and c!=None:
#             print("output of numbers:",a-b-c)
#         elif a!=None and b!=None:
#             print("sub of 2 numbers:",a-b)
#         elif a!=None:
#             print("val of a",a)
#         else:
#             print(" attribute error occured ")
# obj=X()
# obj.subt(2,45,67,98)
# obj.subt(1,2,10)
# obj.subt(100,99)
# obj.subt(23)
# obj.subt()
# o/p:
# 2 45 67 98
# subtract the 4 numbers: -208
# 1 2 10 None
# output of numbers: -11
# 100 99 None None
# sub of 2 numbers: 1
# 23 None None None
# val of a 23
# None None None None
#  attribute error occured
# class med:
#     def multi(self,*x):
#         total=0
#         for i in x:
#             total=total+i
#         print(total)
# c=med()
# med.multi(10,20)
# med.multi(2,3,5,7)
# med.multi(2,1)
# med.multi(10)
# o/p:
# 20
# 15
# 1
#0

#4.what is operator overloading write an example?
#operator overloading: Using the same operator for multiple purposes are konown as operator overloading
#python supports operator overloading
# 1.'+'operator can be used as arthematic operator and also for concenation of two strings
# a=2
# b=3
# print(a+b)
# x='python'
# y='c++'
# print(x+y)
# o/p:
# 5
# pythonc++
#2.'*' operator is used for multiplication of string and integer and also as arthematic operator
# a=24
# b=30
# print(a*b)
# x="python"
# y=4
# print(x*y)
# o/p:
# 720
# pythonpythonpythonpython


#5.what is method overriding write an example?
#method overriding:What ever memebers available in the parent class are by default available to the child class through
#inheritance.
# the method which is present in parent and derived class with same name and same args then parent class is overridden
#by child class

# class A:
#     def ipl(self):
#         print("virat")
#     def cap(self):
#         print("kohli")
# class B(A):
#     def cap(self):
#         print("rohit")
# t=B()
# t.cap()
# t.ipl()
# o/p:
# rohit
# virat

#from method of child we can call parent class method aslo by using super() method
# class A:
#     def ipl(self):
#         print("virat")
#     def cap(self):
#         print("kohli")
# class B(A):
#     def cap(self):
#         print("rohit")
#         super().cap()
# t=B()
# t.cap()
# t.ipl()
# o/p:rohit
# kohli
# virat


#6.what is abstract class write an example?
# abstract class:some times implementation of class is not complete, such type of partially implementation classes
# are called abstract classes.they are derived from abc class which is present in abc module.
# we cannot create abstrac
# t class when they contains abstract method and we can create class even it has abstract method
#when ABC class is not extended
#1.
# from abc import*
# class java(ABC):
#     pass
# a=java()
#2.
# from abc import*
# class python(ABC):
#     @abstractmethod
#     def x(self):
#         pass
# b=python()           #TypeError: Can't instantiate abstract class python with abstract method x
# b.x()
#3.
# from abc import*
# class C():
#     @abstractmethod
#     def S(self):
#         print('hey google')
# p=C()
# p.S()
#o/p:hey google

#

# 7.create a class that accepts 5 students data -> st1={'NAME':'NTR',ROLE_NO:123} st2={'NAME':'ALLU',ROLE_NO:133}
# st3={'NAME':'CHIRU',ROLE_NO:143} ....st5here names and roleno should not be repeated ,
# if we give same name or roleno ,its should be allowed to add
# -> need to display msg : name/role no already exits please give another name/roleno

# class student:
#     names=[]
#     rollno=[]
#     def data(self,name,Rno=None):
#         if name not in student.names:
#             student.names.append(name)
#         else:
#             print("{} is already exists please give another name".format(name))
#             return
#         if Rno not in student.rollno:
#             student.rollno.append(Rno)
#         else:
#             print("{} is already exists:".format(Rno))
#     def studentdetails(self):
#         out={}
#         out=dict(zip(student.names,student.rollno))
#         print(out)
# A=student()
# for i in range(1,6):
#     if hasattr(A,"data"):
#         name=input("Enter student name:")
#         Rno=int(input("Enter student Rno:"))
#         A.data(name, Rno)
# A.studentdetails()
# o/p:
# {'srinu': 116, 'padma': 24, 'navya': 7, 'divya': 13,'shanvi':97}

#8.what is ducktype polymorphism how to check particular method exits or not in class?
#duck type polymorphism:function name is same but actions are different are known as duck type polymorphism
# class kid1:
#     def play(self):
#         print("ringa rose")
# class kid2:
#     def play(self):
#         print("butterfly")
# class kid3:
#     def play(self):
#         print('snake n ladder')
# x=[kid1(),kid2(),kid3()]
# for i in x:
#     i.play()
# o/p:ringa rose
# butterfly
# snake n ladder
#by using hasaatr() method we can check particular method exits or not in the class
# class kid1:
#     def play(self):
#         print("ringa rose")
# class kid2:
#     def play(self):
#         print("butterfly")
# class kid3:
#     def play(self):
#         print('snake n ladder')
# class kid4:
#     def game(self):
#         print('ludo')
# def f1(obj):
#     if hasattr(obj,'play'):
#         obj.play()
#     else :
#         print("game is not there in the class")
# x=[kid1(),kid2(),kid3(),kid4()]
# for obj in x:
#     f1(obj)
# o/p:
# ringa rose
# butterfly
# snake n ladder
# game is not there in the class


#9) create a class that will accept the string and integer the string has to rotate anti clock wise based on
# integer val ex : x='python' a=int(input("Enter a val")) output format : hint :try to use loops and slicing
#  a=1 string o/p :'ythonp'
#  a=2 string o/p :'thonpy'
#  a=3 string o/p : honpyt
#
# x='python'
# a=int(input("Enter a val :"))
# y=x[a:]
# y=y+x[:a]
# print(y)


# 10) Create a class that will accept the string extract the number from string and convert remaining string
# into asscci converted string Ex:'A1B2c3'  output:# Extracted number is 123 after extracting number string become : ABc
# Ascci converted string is :656699

# class A:
#     def __init__(self):
#         self.x='A1B2c3'
#         for i in self.x:
#             if i.isdigit():
#                 print(i,end=' ')
#         print()
#         for i in self.x:
#             if i.isalpha():
#                 print(ord(i),end=' ')
# obj=A()
# o/p:
# 1 2 3
# 65 66 99






