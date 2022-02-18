#!/usr/bin/env python
# coding: utf-8

# In[2]:


#map function

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))



#convert the map into a list, for readability:
print(list(x))


# In[4]:


def fahrenheit(celsius):
    return (9/5)*celsius + 32
    
temps = [0, 22.5, 40, 100]

F_temps = map(fahrenheit, temps)

#Show
list(F_temps)


# In[5]:


# we don't have to define our functions beforehand; we can use a lambda expression instead:
list(map(lambda x: (9/5)*x + 32, temps))


# In[1]:


a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11]

list(map(lambda x,y,z:x+y+z,a,b,c))


# In[11]:


# python code to demonstrate working of reduce() function
 
# importing functools for reduce()
from functools import reduce

lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)


# In[12]:


#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b
lst =[47,11,42,13]
#Find max
reduce(max_find,lst)


# In[13]:


#Filter() function

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


# In[15]:


def even_check(num):
    if num%2 ==0:
        return True
lst =range(20)

list(filter(even_check,lst))


# In[16]:


list(filter(lambda x: x%2==0,lst))


# In[17]:


#zip function
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))


# In[18]:


x = [1,2,3]
y = [4,5,6]

# Zip the lists together
list(zip(x,y))


# In[22]:


x = [1,2,3]
y = [4,5,6,7,8]
list(zip(x,y))
# Zip the lists together

#Note how the zip is defined by the shortest iterable length. 
#Its generally advised not to zip unequal length iterables unless your very sure you only need partial tuple pairings.


# In[21]:


#dictionaries
# simply iterating through the dictionaries will result in just the keys.
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

list(zip(d1,d2))


# In[23]:


list(zip(d2,d1.values()))


# In[25]:


#enumerate()
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))


# In[1]:


lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number)
    print(item)


# In[27]:


for count,item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)


# In[28]:


#enumerate() takes an optional "start" argument to override the default value of zero:
months = ['March','April','May','June']

list(enumerate(months,start=3))


# In[29]:


#all()
mylist = [True, True, True]
x = all(mylist)
print(x)


# In[30]:


mylist = [0, 1, 1]
x = all(mylist)
print(x)

# Returns False because 0 is the same as False


# In[31]:


lst = [True,True,False,True]
all(lst)


# In[2]:


#any
mylist = [False, True, False]
x = any(mylist)
print(x)


# In[3]:


#complex
x = complex(3, 5)
print(x)


# In[4]:


# Create 2+3j
complex(2,3)


# In[5]:


complex(10,1)


# In[7]:


#We can also pass strings:
complex('12+2j')


# In[ ]:




