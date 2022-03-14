#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst = [1,2,3]


# In[ ]:


lst.count(2)


# In[ ]:


print(type(1))
print(type([]))
print(type(()))
print(type({}))


# In[ ]:


# Create a new object type called Sample
class Sample:
    pass

# Instance of Sample
x = Sample()

print(type(x))


# In[ ]:


class Dog:
    def __init__(self,breed):
        self.breed = breed
        
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')


# In[ ]:


sam.breed


# In[ ]:


frank.breed


# In[ ]:


class Dog:
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


# In[ ]:


sam.breed


# In[ ]:


sam.name


# In[ ]:


sam.species


# In[ ]:


class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())


# In[ ]:


c.setRadius(2)

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())


# In[ ]:


class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


# In[ ]:


d = Dog()


# In[ ]:


d.whoAmI()


# In[ ]:


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())


# In[ ]:


for pet in [niko,felix]:
    print(pet.speak())


# In[ ]:


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)


# In[ ]:


class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

