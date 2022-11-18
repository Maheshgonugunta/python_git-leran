


#1.x=[[0.0,1.0,2.0],[4.0,5.0,6.0]] count how many zeros in list
# x=[[0.0,1.0,2.0],[4.0,5.0,6.0]]
# out=[]
# for i in range(len(x)):
#     out.extend(x[i])
# print(out)
# print(out.count(0))
# o/p:1


#2.x=[[1,2,3,4],[4,7,5,6]] swap first and last element in nested list  o/p:[[4,2,3,1],[6,7,5,4]]
# x=[[1,2,3,4],[4,7,5,6]]
# for y in x:
#     y[0],y[-1]=y[-1],y[0]
# print(y)
# x[0],x[-1]=x[-1],x[0]
# print(x)
# z=x
# print(z)
# z.reverse()
# print(z)
#o/p:[[4, 2, 3, 1], [6, 7, 5, 4]]



#3.x=list(range(11)) print all even numbers use list comprehension
# x=list(range(11))
# # print(x)
# for i in x:
#     if i%2==0:
#         print(i,end='')
# x=[i for i in x if i%2==0]
# print(x)
# x=[x[i] for i in range(len(x)) if x[i]%2==0]
# print(x)
# # o/p:[0, 2, 4, 6, 8, 10]



# #4.x=[1,2,3,4,5,6,7] print all prime numbers from list
# x=[1,2,3,4,5,6,7]
# for i in range(len(x)+1):
#     count=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             count=count+1
#     if(count==2):
#         print(i,end='')

#o/p:2357


#5.x='ABCADA' print each character how many times its existed
# o/p:A-3
#     B-1
#     C-1
#     D-1
# x='ABCADA'
# a=x.count('A')
# b=x.count('B')
# c=x.count('C')
# d=x.count('D')
# print("A-".format({a}),a)
# print("B-".format({b}),b)
# print("C-".format({c}),c)
# print("D-".format({d}),d)
#o/p:
# A- 3
# B- 1
# C- 1
# D- 1
#or
# x=input("enter a string")
# y=set()
# a=''
# for i in x:
#     if i not in y:
#         y.add(i)
#         a=a+str(x.count(i))+i
# print("the count along with char is:" + a)
#o/p:3A1B1C1D



#6.how to remove element from list with example
#to remove elemnts in the list we use remove function
# a=['divya','navya','shanvi']
# a.remove('shanvi')
# print(a)
# o/p:['divya', 'navya']


#7.how to compare two strings
#To compare two strings we need to check 1.length of both strings and then 2.the order of elements are ckecked
#weather they are same or not


#8.find the longest palindrome string in list x=['hi','madam','java','python','amma'] o/p:['madam']
# x=['hi','madam','java','python','amma']
# max=0
# for i in range(len(x)):
#     temp=x[i]
#     print(temp)
#     rev=temp[::-1]
#     if rev==temp:
#         if len(temp)>max:
#             max=len(temp)
#             long_palindrome_str=temp
# print("longest palindrome string is",long_palindrome_str)


#9.x='python is good' o/p:'Java is good' do not use replace function
# x='python is good'
# y=x.split()
# print(y)
# y[0]="Java"
# print(y)
# z=" ".join(x)
# print(z)
#o/p:Java is good

