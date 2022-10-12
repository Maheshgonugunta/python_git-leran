

#1.What is class how to create a class write syntax and example?
#class:class is a collection of objects,methods and variables.
#class is a keyword
#syntax:"class keyword" "class name":
#ex:
# class A:
#     def chem(self):
#         print("Hello World")
#     def phy(self):
#         print("explore")
# obj=A()
# obj.chem()
# obj.phy()
# o/p:
# Hello World
# explore


#2.what is self,init method what is the use?
#self:
# self is a default variable which always pointing to the current obj
#self is usefui to access the instance methods of objects and instance variables.
#self is default argument and self is always the first parameter for instance methods

#init:
#init method is also known as constructor method it is a special; method in python
#syntax:def__init__(self)
# constructor will execute automatically when we create object
# the main purpose of constructor is to declare and initialize the variables
# constructor will take atleast one argument that called self
# constructor is optional and if we not providing any constructor then  python will provide default constructor


#3.what are the differences between init and instance method?
# name of method can be anything in instance method but in init method the name sholud always be__init__method.
# instance method will be executed whenever we call method but in constructor it will be executed automatically at the
# time of creation.
# instance method can be called many times but constructor can be called only one time.
# inside the instance method we can write but inside the constructor we can declare and initilize the variables.


#4.differences between instance, class and static method with example?

#instance method need a class and can access the instance through "self",class method don't need a class instance,they
# cannot access the class instance but they have access to the class through "cls",but static method don't have access
# to "cls" or "self"

#instance method should be called only by using "obj" but classmethod and static method no need of "obj" to call method

#instance method doesn't have any decorator,but class method and instance method have decorators before them  and they
# are "@classmethod" for class method and "@staticmethod" for static method

# class A():
#     def python(self):
#         print("instance method")
#     @classmethod
#     def java(cls):
#         print("class method")
#     @staticmethod
#     def chem():
#         print("static method")
# obj=A()
# obj.python()
# obj.java()
# A.chem()
# o/P:
# instance method
# class method
# static method


#5.what are inner functions and how to call the functions with example?
#inner function:function inside the function is called nested functions.
#def java():
#     print("oops python")
#     def python():
#         print(123)
#     python()
# java()
# # o/p:
#oops python
# 123

#6.what is lambda function and how to write exampls for map,filter,reuced function?
# lambda function:a function which is defined without a name is called anonymous function (or)lambda function
# the main purpose of lambda function is instant use,it is not suitable to write n no.of lines inside the function
# x=[1,2,3,4,5,6,7,8,9]
# y=list(map(lambda a:a**2,[1,2,3,4,5,6,7,8,9]))     #map
# print(y)
# o/p:[1, 4, 9, 16, 25, 36, 49, 64, 81]

# x=[1,2,3,4,5,6,7,8,9]
# y=print(list(filter(lambda i:i%2==0,x)))          #filter
# o/p:[2, 4, 6, 8]

# x=[1,2,3,4,5,6,7,8,9]
# from functools import reduce       #reduce
# z=reduce(lambda a,b:a+b,x)
# print("sum",z)
# o/p:sum 45


#7.what are inner classes how to access the data from inner classes
#inner classes:classes inside classes is called inner classes
# class MPC:
#     def __init__(self):
#         print(1234)
#     def inbuilt(self):
#         print(23.04,"good")
# class XYZ:
#     def __init__(self):
#         print("shanvi17")
#     def lucky(self):
#         print("class thanu")
# obj_MPC=MPC()
# obj_MPC.inbuilt()
# obj_XYZ=XYZ()
# XYZ.lucky(obj_XYZ)
# o/p:
# 1234
# 23.04 good
# shanvi17
# class thanu

#8.create a class which will take student name,age as a parameters print the student data in dic
#o/p:student:{'name':'python','age':'45'}
# class student:
#     def __init__(self):
#         self.name='python'
#         self.age=45
# obj=student()
# print(obj.__dict__)
#o/p:{'name': 'python', 'age': 45}


#9.create two different classes access the data from one class to another class without inheritance?
# class A():
#     def python(self,rag):
#         print("coffee")
# class B():
#     def java(self):
#         print('mango')
# obj=A()
# obj.python(B)
# obj=B()
# obj.java()
#o/p:coffee
#mango


#10.how to find how many objects are created for the class?
# class A:
#     count=0
#     def __init__(self):
#         A.count=A.count+1
#     def object_count(self):
#         print("No.of objects created for class is:",A.count)
# obj=A()
# obj1=A()
# obj2=A()
# obj2.object_count()
# o/p:No.of objects created for class is: 3




