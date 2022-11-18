#function : function is group of statements in single unit
# the main advantges of function is code reusebility
# in every function start with def keyword
# two types of function
# one is built in functions (or) predefined functions
# built in functions ex : len(),max(),input(),id(),type(),print(),sorted()
# second one is userdefined functions --> these functions whhich are developed by programers
# fun calling will be after the fun defination
# we can pass n num of arg in fun
# syntax : def_fun name(arg) # arg are optional (need to use depinding requirment)
# any userdefined functions start with keyword def
# def java():
 # sta1
 # sta2
 # sta3
# formal arguments : the arguments which are defined  in function defination those arguments are
# called formal arguments.
# actual arguments : the arguments which are calling the function those arguments are called
# actual arguments.

# when u came to other languages like c,c++,java
# fun declartion,fun defination,fun calling
# when u cames to python
# fun declaration
#def python():
 #  print("java is gud")
 #  print("c is gud")
#python()
# calling fun and fun defination contaiins same syntax

# fun calling should be after the fun defination
#def python():
 #   print("hello world")
 #   print("hello java")
  #  print("hello c++")
#python()


# four types of functions there in python
# without arguments without return value
# without arguments with return value
# with arguments with return value
# with arguments without return value

# without arguments without return value
#def python():
 #   print("hello world")
 #   print("hello java")
  #  print("hello c++")
#python()

# without arguments with return value
# without arguments without return value
# with arguments with return value
# with arguments without return value

# without argument with return value
#def add():
#    p=10
#    k=18
#    return p+k
#print("result :",add())

#def mahesh():
#    a=19
#    b=16
#    return a-b
#mahesh()
#print(mahesh)

#def mul():
#   p=100
 #  k=18
 #  return p*k
#c=mul()
#print(c)

# without arguments without return value
#def mul(a,b):  # a,b are called formul arguments
#    return a*b
#c=mul(15,17)  # 15,17, are called formul arguments
#print(c)
#print("Result:",mul(10,17))

# with argument without return value
#def sub(p,q):
#    print(p-q)
#sub(20,15)
#print(sub(20-10))

# return mulitple values from function
#def add(a,b):   # formul arguments
#    a=a+10
#    b=b+19
#    c=1000
#    d=70
 #   return a,b,c,d
#w,x,y,z=add(30,40)  # actual arguments  # w=a,x=b,y=c,z=d
#print("w value from",w)
#print("x value from",x)
#print("y value from",y)
#print("z value from",z)

# positional arguments
#def add(a,b,c):
 #   print("a val is",a)
 #   print("b val is",b)
 #   print("c val is",c)
#add(12,15,17)

# keyword arguments
#def add(a,b,c,d):  # formul args
#    a=a+10
#    b=b+20
#    print("a val",a)
#    print("b val",b)
#    print("c val",c)
 #   print("d val",d)
#    return a,b,c,d
#add(10,20,30,40)
#a,b,c,d
#x,y,z,i=add(a=300,d=400,c=479,b=234)  # actual args
#print(x)
#print(y)
#print(z)
#print(i)

# defalut arguments
# defalult arguments always right side of the function declaration
# if we pass the value for defalut arguments it will take,if we dont pass the defalut value will be printed
#def add(a,b,c,d,e=None,f=None): # here a,b,c are positional arguments 'e' is the defalut arguments
#    print("a val",a)
#    print("b val",b)
#    print("c val",c)
#    print("d val",d)
 #   print("e val",e)
 #   print("f val",f)
#add(15,17,18,19,70)
#add(a=10,b=12,c=13,d=12,f=45)


#list=[[]]*3
#list[1].append(5)
#print(list)

# list unpacking # assigning each and every element from the list and strong into the variable
# the length of the list is equal to number of variables
#y=[1,17,8]
#a,b,c=y
#print(a)
#print(b)
#print(c)

#list packing
#a,b,c,d=12,14,19,45
#y=[]
#y.append(a)
#y.append(b)
#y.append(c)
#y.append(d)
#print(y)
# list packing using functions
# def mul(a,b,c,d):
#    y=[]
#    print(a)
#    print(b)
#    print(c)
#    print(d)
#    return y #(12,35,78,98)
#out=mul(12,35,78,98)
#print(out)

# list unpacking using functions
#def unpack(x):
#    print(x)
#    a,b,c=x
#  return a,b,c
#z=[12,16,18]
#j,k,l=z
#print(j,k,l)

# varlen arg
# syntax : def function(* formul arguments)
# variable length arguments by default it will return tuple and will accept n num of arguments from
# fun calling
#def python(*m):
#    return m
#out=python(4,6,8,8,9,0,6,3,2)
#print(out)

#def python(b,v,*t):  # posiotional arguments + variable len arguments
#    print('a val is',t)
#    print('b val is',v)
#    print('c val is',b)
#python(7,8,9,0,5,7)
#def add(*a):
#    return a,sum(a),a[0]
#x,y,z=add(1,2,3,5,6,7)
#print(x)
#print(y)
#print(z)
#def add(*a):
#    return a[0],a[2]*20,max(a)
#x,y,z=mul(1,6,7,8,9,)
#print(x)
#print(y)
#print(z)

# keyword variable length
# we can declare keyword variable len arguments
# syntax : def function name(**variable name)
# keyword arg are stored in the from of dictionary
#def java(**a):
#    print(type(a))
 #   print(list(a.keys()))
#    print(list(a.values()))
#java(a=10,b=12,c=14)
#def java(**a):
#      print(type(a))
#      print(list(a.keys()))
#      print(list(a.values()))
#      return a
#out=java(a=10,b=12,c=14)
#print(out)
#def java(**x):
 #   return list(x.keys()),list(x.values()),700,800
#key,val,x,y=java(a=10,b=12,c=15)
#print(key,val,x,y)
#def python(**a):  # formal arguments
#    print(a.keys())
#    print(a.items())
#    return a
#x=python(a=10,b=12,c=14)  # keyword arguments
#def add(b,c,a="k"):
#    print(b)
#    print(c)
#    print(a)
#add(b=12,c='python')
#def python(*x,**y):  # variable len arg+ keyword var len
#    return x,y
#a,b=python(1,2,32,455,8,a=18,b=16,c=16)
#print(a)
#print(b)

#print("mahesh)
#print("mahi")


















