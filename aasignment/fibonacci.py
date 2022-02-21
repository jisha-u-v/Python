#!/usr/bin/env python
# coding: utf-8

# In[1]:


nterms = int(input("How many no of terms"))
n1 , n2 = 0,1
count = 0
if nterms <=0 :
    print('Enter a positive no')
elif nterms == 1 :
    print('Fibonacci series up to n terms is:',n1)
else:
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    
    


# In[ ]:




