#!/usr/bin/env python
# coding: utf-8

# In[2]:


#if/else/elif
a = 33
b = 33
if b  > a:
    print('b > a')
elif b == a :
    print('a=b')
else :
    print('a>b')
    


# In[3]:


#nested
x = 41
if x > 40 :
    print('Above ten')
    if x > 20 :
        print('above 20')
    else :
        print('nothing above 20')


# In[4]:


color = ['red','yellow','green']
fruits = ['apple','banana','grapes']
for x in color :
    for y in fruits :
        print(x,y)
        


# In[10]:


#functions
def myfunction() :
    print('Hello world')

myfunction()
     
    


# In[ ]:




