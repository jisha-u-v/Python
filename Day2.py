#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string
string1 = "{1} {0} {2}".format('welcome', 'to', 'ust')
print(string1)


# In[2]:


A = 10
B = float(A)
print(B)


# In[3]:


A = 10.78
B = int(A)
print(B)


# In[4]:


a = [1,2,3,4,5,11]
a.remove(11)
print(a)


# In[6]:


#remove duplicates
list1 = ['a','b','c','b','c','a']
b = print(list(dict.fromkeys(list1)))
print(b)


# In[7]:


#range of index
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
print(mylist[2:5])


# In[8]:


#last index
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
print(mylist[-1])


# In[9]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
print(mylist[:4])


# In[10]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
print(mylist[2:])


# In[11]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
print(mylist[-4:-1])


# In[13]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
if 'CSk' in mylist:
    print('CSK in mylist')


# In[14]:


#replace
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist[2] = "IND"
print(mylist)


# In[15]:


#replace
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist[1:2] = ["IND","ENG"]
print(mylist)


# In[16]:


#insert
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.insert(2,'IND')
print(mylist)


# In[17]:


#insert at the end
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.append('IND')
print(mylist)


# In[18]:


#extend function
mylist1 = ['python','java','php']
mylist2 = ['c','c++','dotnet']
mylist1.extend(mylist2)
print(mylist1)


# In[19]:


#remove
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.remove('MI')
print(mylist)


# In[20]:


#pop
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.pop(1)
print(mylist)


# In[22]:


#remove last item
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.pop()
print(mylist)


# In[23]:


#clear  item
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.clear()
print(mylist)


# In[24]:


#for loop
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
for x in mylist:
    print(X)


# In[25]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
for x in mylist:
    print(x)


# In[26]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
for x in range(len(mylist):
    print(x)


# In[27]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
for x in range(len(mylist)):
    print(x)


# In[28]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
for x in range(len(mylist)):
    print(mylist[x])


# In[30]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
i= 0
while(i < len(mylist)):
    print(mylist[i])
    i = i+1


# In[31]:


#sort
mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.sort()
print(mylist)


# In[33]:


numlist = [100,55,75,26,28]
numlist.sort()
print(numlist)


# In[34]:


mylist = ['RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR']
mylist.sort(reverse = True)
print(mylist)


# In[35]:


numlist = [100,55,75,26,28]
numlist.sort(reverse = True)
print(numlist)


# In[37]:


alist = ['chennai','bangalore','hydrabad','tvm','Delhi']
alist.sort()
print(alist)
#sort method is case sensitive


# In[38]:


alist = ['chennai','bangalore','hydrabad','tvm','Delhi']
alist.sort(key = str.lower)
print(alist)


# In[39]:


alist = ['chennai','bangalore','hydrabad','tvm','Delhi']
alist.reverse()
print(alist)


# In[40]:


#copy list
alist = ['chennai','bangalore','hydrabad','tvm','Delhi']
blist = list(alist)
print(blist)


# In[41]:


#tuple
mytuple = ("sandee","anil","umrah","gousya")
print(mytuple)


# In[42]:


mytuple = ("sandee","anil","umrah","gousya")
print(len(mytuple))


# In[43]:


x = ("sandee","anil","umrah","gousya")
y = list(x)
print(y)


# In[44]:


z= tuple(y)
print(z)


# In[45]:


myset = {"sandee","anil","umrah","gousya"}
print(myset)


# In[46]:


mydict = {
    "brand" : "maruti",
    "model" : "swift",
    "year" : 1983
    
}
print(mydict)


# In[48]:


print(mydict["brand"])


# In[50]:


mydict = {
    "brand" : "maruti",
    "model" : "swift",
    "year" : 1983,
    "year" : 1965
    
}
print(mydict)


# In[51]:


mydict = {
    "brand" : "maruti",
    "model" : "swift",
    "year" : 1983,
    "year" : 1965
    
}
print(mydict.keys())


# In[52]:


print(mydict.values())


# In[53]:


mydict = {
    "brand" : "maruti",
    "model" : "swift",
    "year" : 1983,
    "year" : 1965
    
}
mydict['model'] = 'celerio'
print(mydict)


# In[54]:


a = """sdfghasdfghjk,l
dfghjkl
ssssssssssssssssss"""
print(a)


# In[56]:


a='Hello,World'
print(a[2:5])


# In[57]:


a='Hello,World'
print(a[:5])


# In[58]:


a='Hello,World'
print(a[5:])


# In[60]:


a='Hello,World'
print(a.upper())


# In[61]:


a='Hello,World'
print(a.lower())


# In[63]:


a='Hello,World'
print(a.replace("o","q"))


# In[64]:


a = "hello"
b = "world"
c = a+b
print(c)


# In[66]:


tuple1 = ('a','b','c','a')
b = print(tuple(dict.fromkeys(tuple1)))
print(b)


# In[67]:


mytuple = ('a','b','c','d','e','f','g');
print(mytuple[2:5])


# In[68]:


mytuple = ('a','b','c','d','e','f','g');
print(mytuple[-1])


# In[69]:


mytuple = ('a','b','c','d','e','f','g');
print(mytuple[-4:-1])


# In[71]:


mytuple = ('a','b','c','d','e','f','g');
if 'b'in mytuple:
    print('b is in mytuple')


# In[73]:


mytuple = ('a','b','c','d','e','f','g');
mytuplelist =list(mytuple)
mytuplelist[2] = 'l'
mytuple = tuple(mytuplelist)

print(mytuple)


# In[74]:


mytuple = ('a','b','c','d','e','f','g');
y = list(mytuple)
y.append('h')
print(y)


# In[75]:


a = ('a','b','c','d','e','f','g');
b = ('h','i','j')
c = a + b
print(c)


# In[80]:


a = ('a','b','c','d','e','f','g');
b = list(a) 
b.remove('g')
print(b)


# In[82]:


a = ('a','b','c','d','e','f','g');
b = list(a) 
b.pop(0)
print(b)


# In[84]:


a = ('a','b','c','d','e','f','g');
b = list(a)
b.clear()


# In[88]:


a = ('a','b','c','d','e','f','g');
for x in a :
    print(x)


# In[89]:


a = ('a','b','c','d','e','f','g');
for x in range(len(a)) :
    print(x)


# In[90]:


a = ('RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR')
i= 0
while(i < len(a)):
    print(a[i])
    i = i+1


# In[92]:


a = ('RCB' , 'MI' , 'CSK' , 'KKR','SRH','RR')
list(a).sort()
print(a)


# In[95]:


myset = {"sandee","anil","umrah","gousya"}
print(myset)


# In[96]:


myset = {"sandee","anil","umrah","gousya"}
print(len(myset))


# In[102]:


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[104]:


thisset = {"apple", "banana", "cherry"}
if 'banana'in thisset:
    print('banana is in mytuple')


# In[106]:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)


# In[107]:


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# In[110]:


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# In[111]:


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# In[113]:


thisset = {"apple", "banana", "cherry"}

thisset.pop()

print(thisset)


# In[115]:


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# In[117]:


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[118]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[119]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# In[121]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# In[122]:


x = thisdict.keys()
print(x)


# In[124]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car['color'] = 'white'
print(car)


# In[125]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# In[127]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


# In[129]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


# In[130]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# In[131]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# In[132]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# In[133]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


# In[134]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)


# In[135]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(thisdict[x])


# In[136]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# In[137]:


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


# In[138]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# In[139]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# In[140]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# In[ ]:




