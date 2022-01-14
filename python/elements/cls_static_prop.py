
## class method and static method

from datetime import date
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    # a class method to create a Person object by birth year.
    # може ініціалізувати функцію наприклад з не стандартними параметрами
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
      
    # a static method to check if a Person is adult or not.
    # можна викликати до строверення об'єкта класу
    @staticmethod
    def isAdult(age):
        return age > 18
  
person1 = Person('slava', 28)
person2 = Person.fromBirthYear('slava', 1993)
  
print (person1.age)
print (person2.age)
  
# print the result
print (Person.isAdult(28))



### property and setter
### можемо наприклад перевірити параметри перед передачею в функцію
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError


    def area(self):
        self.k = self.__width * self.__height
        return self.k


r = Rectangle(-2,-2)  ##  not error
#r.width=-10          ## it's error





