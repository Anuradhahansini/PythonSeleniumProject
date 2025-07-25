#Python Object and classes

#Class: සැබෑ Object එකක් නිර්මාණය කිරීමට අවශ්‍ය සැකිල්ල (blueprint).

#Object: Class එකකින් නිර්මාණය කරන ලද සැබෑ දේ (actual instance), එයටම ආවේණික දත්ත (attributes) සහ ක්‍රියාවන් (methods) සමගින්.
# class Class Name :
#Statement

#Defining a class in python
class Student:
    name= "ram"
    rank = 1

    def show(self):
        print(self.name)
        print(self.rank)




#creating an object in python
student1 = Student()
print(student1.rank)
student1.show()

#constructors in python
class Car:
    def __init__(self,name,price):

        self.name =name
        self.price = price
    def show(self):
        print(self.name)
        print(self.price)


bmw = Car("bmw",10000)
bmw.show()

benze = Car("benz",20000)
benze.show()
