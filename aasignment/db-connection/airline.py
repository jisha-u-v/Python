#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install mysqlconnector


# In[4]:


pip install mysql-connector-python


# In[1]:


import mysql.connector
mydb  = mysql.connector.connect(host="localhost", user="root", password="", database="travel")


# In[2]:


def Add_airline():
 
 
        Name = input("Enter  Name : ")
        No = input("Enter  No : ") 
        status = 1
        data = (Name,No)
 
        # Inserting Employee details in the Employee
       
        mycursor = mydb.cursor()
        sql = "INSERT INTO airline (air_no, air_name) VALUES (%s, %s)"
        val = data
        mycursor.execute(sql, val)
        mydb.commit()
 
        # commit() method to make changes in the table
      
        print("Employee Added Successfully ")
        menu()


# In[3]:


# Function to Remove Employee with given Id
def Remove_airline():
    Id = input("Enter Airline Id : ")
    # Query to Delete Airline from Table
    mycursor = mydb.cursor()
    sql = 'delete from airline where air_no=%s'
    data = (Id,)
    mycursor.execute(sql, data)
    mydb.commit()

    print("Airline Removed")
    menu()


# In[4]:


# Function to Display All Airline
# from Employee Table
 
def Disply_airline():
   
    mycursor = mydb.cursor()
    sql = 'select * from airline' 
     
    # Executing the SQL Query
    mycursor.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = mycursor.fetchall()
    for i in r:
        print("Airline Id : ", i[0])
        print("Airline No : ", i[1])
        print("Airline Name : ", i[2])
        print("Status : ", i[3])
       
    menu()


# In[ ]:


# menu function to display menu
def menu():
    print("Welcome to Airline Travel Management System ")
    print("Press ")
    print("1 to Add Airline")
    print("2 to Remove Airline ")   
    print("3 to Display Airline")
    print("4 to Exit")
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_airline()
    elif ch == 2:
        Remove_airline()
    elif ch == 3:
        Disply_airline()
   
    else:
        print("Invalid Choice")
        menu()
 
 
# Calling menu function
menu()


# In[ ]:





# In[ ]:




