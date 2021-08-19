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
