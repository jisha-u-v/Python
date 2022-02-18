#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector
mydb  = mysql.connector.connect(host="localhost", user="root", password="", database="travel")


# In[7]:


def Add_hotel():
 
 
        Name = input("Enter  Hotel Name : ")
        Place = input("Enter Place : ") 
        Budget = input("Enter Budget")
        status = 1
        data = (Name,Place,Budget,status)
 
        # Inserting Employee details in the Employee
       
        mycursor = mydb.cursor()
        sql = "INSERT INTO hotel (name, place,budget,status) VALUES (%s, %s, %s, %s)"
        val = data
        mycursor.execute(sql, val)
        mydb.commit()
 
        # commit() method to make changes in the table
      
        print("Hotel Added Successfully ")
        hotel_menu()


# In[12]:


# Function to Remove Hotel with given Id
def Remove_hotel():   
    Id = input("Enter Hotel Name : ")
    # Query to Delete Airline from Table
    mycursor = mydb.cursor()
    sql = 'Delete from hotel where name = %s'
    val = (Id,)
    mycursor.execute(sql, val)

    mydb.commit()

    print("Hotel Removed")
    
    hotel_menu()


# In[13]:


# Function to Display All Airline
# from Employee Table
 
def Disply_hotel():
   
    mycursor = mydb.cursor()
    sql = 'select * from hotel' 
     
    # Executing the SQL Query
    mycursor.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = mycursor.fetchall()
    for i in r:
        print("Hotel Id : ", i[0])
        print("Hotel Name : ", i[1])
        print("Hotel Place : ", i[2])
        print("Hotel Budget : ", i[3])
        print("Status : ", i[4])
       
    hotel_menu()


# In[14]:


# menu function to display hotel menu
def hotel_menu():
    print("Welcome to Hotel Travel Management System ")
    print("Press ")
    print("1 to Add Hotel")
    print("2 to Remove Hotel ")   
    print("3 to Display Hotel")
    print("4 to Exit")
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_hotel()
    elif ch == 2:
        Remove_hotel()
    elif ch == 3:
        Disply_hotel()
   
    else:
        print("Invalid Choice")
        hotel_menu()
 
 
# Calling menu function
hotel_menu()


# In[ ]:





# In[ ]:




