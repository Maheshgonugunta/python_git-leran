

#1.write a function sum of given numbers pass 1,2,3 and return result is 6
# def java(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#     return a+b+c
# d=java(1,2,3)
# print(d)
# o/p:6


#2.write a function to print even and odd numbers in list,pass list to function x=list(range(1,11)->(1,10)
# x=list(range(1,11))
# even_list=[]
# odd_list=[]
# def dev(x):
#
#     for i in range(len(x)):
#         if(x[i]%2==0):
#             even_list.append((x[i]))
#         else:
#             odd_list.append((x[i]))
#     return even_list,odd_list
#print(dev(x))
#o/p:
#([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])



#3.write a program for default arguments and return result
# def add(b,c,a=200):
#     return(a+b,c)
#     print("a val",a)
#     print("b val",b)
#     print("c val",c)
# A=add(20,30)
# print(A)
# o/p:(220, 30)


#4.write a program to print multiplication table and pass n from keyboard
# def table(n):
#     for i in range(1,11):
#         print(n,'*',i,'=',n*i)
# n=7
# table(n)
# o/p:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# 7 * 4 = 28
# 7 * 5 = 35
# 7 * 6 = 42
# 7 * 7 = 49
# 7 * 8 = 56
# 7 * 9 = 63
# 7 * 10 = 70


#5.write a fun pass n of args and return list using variable len args
# def divya(*k):
#     return(list(k))
# print(divya("forensic","document","examination"))
#o/p:['forensic', 'document', 'examination']



#6.write a function pass keyword args and return dict(a=10,b=20,c=30)->{a:100,b:400,c:900}
# def java(a,b,c):
#     print(a*a)
#     print(b*b)
#     print(c*c)
# java(10,20,30)
# def python(**java):
#     print(java)
# python(a=100,b=400,c=900)
# o/p:{'a': 100, 'b': 400, 'c': 900}



#
#7.write a fun to fetch first word from list elements x=["PYTHON IS GOOD","JAVA IS GOOD"] #O/P:["PYTHON","JAVA"]
# x=["PYTHON IS GOOD","JAVA IS GOOD"]
# out=[]
# for i in range(len(x)):
#     temp=x[i].split()
#     out.append(temp[0])
# print(out)
# O/P:["PYTHON","JAVA"]


#8.write a fun to change string lower to upper and upper to lower and return the string
# a="GOd hAS diffeRENT PLanS FOR every ONE"
# def python(x):
#     return x.swapcase()
# i=python(a)
# print(i)
#o/p:goD Has DIFFErent plANs for EVERY one



#9.write a function to get only vowels from the list x=["PYTHON IS GOOD","JAVA IS GOOD"]->[I,O,I,O,O,A,A,I,O,O]->
#remove the duplicates->[['O', 'I', 'A']]


# x=['PYTHON IS GOOD','JAVA IS GOOD']
# vowels_list=['A','E','I','O','U']
#
# def b(vowels_list,x):
#     out=[]
#     y=''.join(x)
#     print(y)
#     for i in y:
#         if i in vowels_list and i not in out:
#             out.append(i)
#     return out
# duplicates=b(vowels_list,x)
#print(duplicates)
#o/p:['O', 'I', 'A']


#10.write a function get the max num from list without using predefined fun max x=[101,200,3000,400]#max:3000

# def max_value(x):
#     max=x[0]
#     for i in x:
#         if i>max:
#             max=i
#     return max
# x=[101,200,3000,400]
# print(max_value(x))
# o/p:3000

#11.write a fun to sort the list without using sort fun
# x=[1,4,5,2,37,79,7869,86,357]
# print(sorted(x))
# o/p:[1, 2, 4, 5, 37, 79, 86, 357, 7869]



