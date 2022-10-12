

#1.What is dictionary and write all dictionary functions with example
#dictionary:dictionary is a collection of key and value pairs
#To access dictionary values we use 'get' function
# x={'A':23,'B':"python"}
# print(x.get('A'))
# print(x.get('B'))
# o/p:
# 23
# python
#del keyword
#del is useful for to delete the particular key-values
# x={'A':'java is good',1:35,'C':'python python'}
# x['B']=24
# print(x)
# del x[1]
# print(x)
# o/p:{'A': 'java is good', 1: 35, 'C': 'python python', 'B': 24}
# {'A': 'java is good', 'C': 'python python', 'B': 24}
#pop:pop is used to remove the particular key and val and returns the val of that particular key
# x={'A':'java is good',1:35,'C':'python python'}
# x.pop('C')
# print(x)
# print(x.pop('A'))
# #o/p:{'A': 'java is good', 1: 35}
#java is good
#popitem:always removes the last key-value pair from dictionary
# x={'A': 'java is good', 1: 35,'B':999,'python':1000}
# print(x)
# x.popitem()
# print(x)
# o/p:
# {'A': 'java is good', 1: 35, 'B': 999, 'python': 1000}
# {'A': 'java is good', 1: 35, 'B': 999}
#clear:it removes everything from the dictionary and gives empty dictionary
# x={'A': 'java is good', 1: 35,'B':999,'python':1000}
# x.clear()
# print(x)
# o/p:{}
#update:update is used to update the value of particular keys and we can update new keys and values also
# x={'A': 'java is good', 1: 35,'B':999,'python':1000}
# print(x)
# x.update({1:'divya','B':'navya'})
# print(x)
# o/p:
# {'A': 'java is good', 1: 35, 'B': 999, 'python': 1000}
# {'A': 'java is good', 1: 'divya', 'B': 'navya', 'python': 1000}
#copy:copying of an element from one dictionary to another
# x={'A': 'java is good', 1: 'divya', 'B': 'navya', 'python': 1000}
# print(x)
# z=x.copy()
# print(z)
# o/p:
# {'A': 'java is good', 1: 'divya', 'B': 'navya', 'python': 1000}
# {'A': 'java is good', 1: 'divya', 'B': 'navya', 'python': 1000}
#setdefault:if key is available in the given function returns the key value,key is'nt available thenit will
#append the key to dictionary
# x={'A': 'java is good', 1: 'divya', 'B': 'navya', 'python': 1000}
# print(x.setdefault('C'))
# print(x.setdefault(9,'k'))
# print(x)
# o/p:
# None
# k
# {'A': 'java is good', 1: 'divya', 'B': 'navya', 'python': 1000, 'C': None, 9: 'k'}
# fromkeys:it updates the commomn values for all the keys in the dictionary
# x={'A':['a','b','c','d'],'B':('java','python')}
# x=x.fromkeys(x.keys(),'AB')
# print(x)
# print(x.fromkeys(x.keys(),'pypy'))
# o/p:
# {'A': 'AB', 'B': 'AB'}
# {'A': 'pypy', 'B': 'pypy'}
# keys=['a','b','c','d']
# val=9
# y=dict.fromkeys(keys,val)
# print(y)
# o/p:{'a': 9, 'b': 9, 'c': 9, 'd': 9}
#zip:zip is used to combine two iterable objects
# x=[1,2,3]
# y=['p','q','r']
# z={}
# z=dict(zip(y,x))
# print(z)
# o/p:{'p': 1, 'q': 2, 'r': 3}
#enumerate:gives automatically index values
# x={'A': 'pypy', 'B': 200}
# for i,j in enumerate(x):
#     print([i,j])
# o/p:
# [0, 'A']
# [1, 'B']



#2.x={'A':1,'B':'5'} o/p:{1: 'A', '5': 'B'}interchange the keys and values
# x={'A':1,'B':'5'}
# out={}
# key=list(x.keys())
# val=list(x.values())
# out=dict(zip(val,key))
# print(out)
# o/p:{1: 'A', '5': 'B'}



#3.x={'1':['a','b'],'2':['c','d']} expected output:['ac','ad','bc','bd']
# x={'1':['a','b'],'2':['c','d']}
# a=x['1']
# b=x['2']
# print(a,b)
# out=[]
# for i in range(len(a)):
#     for j in range(len(b)):
#         temp=a[i]+b[j]
#         out.append(temp)
# print(out)
#o/p: ['ac','ad','bc','bd']



#4.x='EMBEDDED'o/p:{'E':3,'M':1,'B':1,'D':3}
x='EMBEDDED'
# y=set(x)
# print(y)
# out=[]
# for i in x:
#     if i not in out:
#         out.append(i)
# print(out)
# final=[]
# for i in range(len(out)):
#     final.append(x.count(out[i]))
# print(final)
# a=dict(zip(out,final))
# print(a)
# o/p:{'E': 3, 'M': 1, 'B': 1, 'D': 3}



#5.x={'A':3,'B':5,'C':4,'D':2,'E':1} arrange keys and values as per ascending order of values
#o/p:{'E': 1, 'D': 2, 'A': 3, 'C': 4, 'B': 5}

# x={'A':3,'C':4,'E':1,'B':5,'D':2}
# print(type(x))
# out=(dict(sorted(x.items())))
# print(out)
# a=list(x.keys())
# b=list(x.values())
# z=dict(zip(b,a))
# print(z)
# p=dict(sorted(z.items()))
# print(p)
# a=list(p.keys())
# b=list(p.values())
# z=dict(zip(b,a))
# print(z)
# o/p:{'E': 1, 'D': 2, 'A': 3, 'C': 4, 'B': 5}


#6.{'A':'Red','D':'None','B':'Green','C':None}New Dictionary after dropping empty items o/p:{'A': 'Red', 'B': 'Green'}
# x={'A':'Red','D':'None','B':'Green','C':None}
# del x['C']
# del x['D']
# print(x)
# o/p:{'A': 'Red', 'B': 'Green'}


#7.x={'A':123,'B':100} check key is exists or not in dic
x={'A':123,'B':100}
# def python(i):
#     if i in x:
#         print('key is present in the dictionary')
#     else:
#         print('key is not present in the dictionary')
# python('A')
# python('B')
# o/p:
# key is present in the dictionary
# key is present in the dictionary


#8.x='Hello PYTHON who ARE YOU' o/p:{'H': 'HELLO', 'P': 'PYTHON', 'W': 'WHO', 'A': 'ARE', 'Y': 'YOU'}
# x='Hello PYTHON who ARE YOU'
# x=(x.upper())
# print(x)
# keys=[]
# values=[]
# x=x.split()
# for i in range(len(x)):
#     keys.append(x[i][0])
#     values.append(x[i])
# out=dict(zip(keys,values))
# print(out)
# o/p:{'H': 'HELLO', 'P': 'PYTHON', 'W': 'WHO', 'A': 'ARE', 'Y': 'YOU'}


#9.{'C1':[10,20,30],'C2':[20,30,40],'C3':[12,34]} reverse the list values in the dictionary:
# x={'C1':[10,20,30],'C2':[20,30,40],'C3':[12,34]}
# keys=list(x.keys())
# val=list(x.values())
# for i in range(len(val)):
#     val[i].reverse()
# print(val)
# out=dict(zip(keys,val))
# print(out)
# o/p:{'C1': [30, 20, 10], 'C2': [40, 30, 20], 'C3': [34, 12]}


#10.{1:'red',2:'green',3:'black',4:'white',5:'black'} length of dictionary values:
# def python(dic):
#     out = {}
#     for i in dic.values():
#         out[i]=len(i)
#     return out
# x={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print(x)
# print(python(x))
# o/p:{'red': 3, 'green': 5, 'black': 5, 'white': 5}

