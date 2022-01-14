class Mainclass:
    def __init__(self,):
        self.__private_variable = 2020

    def __private_method(self):
        print("Приватний")

    def insideclass(self):
        print("Приватна змінна:", Mainclass.__private_variable)
foo = Mainclass()

foo.__private_variable=2021     ## not error
print(foo.__private_variable)   ## not error
#foo.insideclass()              ## error
#foo.__private_method()         ## error


class Student:
    _sName = 'XYZ' # protected class attribute   # are also available to its sub-classes # https://www.tutorialsteacher.com/python/public-private-protected-modifiers
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute


class Student:
    __sName = 'XYZ' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')
