

###https://devpractice.ru/python-lessons/


k = 15
print('get memory id', id(k) )
print('get type',    type(k) )


# деление
print(9 / 3)
# целая часть от деления
print( 9 // 3)
# остаток
print( 9 % 5)


# кортежи и списки
# списки удобнее, кортежи быстрее и легче
lst = [10, 20, 30]
tpl = (10, 20, 30)
print(lst.__sizeof__())
print(tpl.__sizeof__())

# словари  (ассоциативный массив)
d2 = {"A1":"123", "A2":"456"}
print(d2)


# лямбда функции (любое число аргументов, не более одной инструкции/одна формула )
(lambda x: x**2)(5)

# присваиваем переменной 
sqrt = lambda x: x**0.5
print( sqrt(25) )


# исключения (иерархия исключений https://devpractice.ru/python-lesson-11-work-with-exceptions/ )
print('\n exceptions \n')
print("start")
try:
   val = 0 #int(input("input number: "))  ## enter some int
   tmp = 10 / val
   print(tmp)
except(ValueError, ZeroDivisionError):
   print("Error!")
print("stop")


try:
   raise Exception("Some exception raise 52")
except Exception as e:
   print("Exception : " + str(e))
   #exit()


print('\n files \n')
### работа с файлами
def file():
	f = open("test.txt", "r")
	print(f.read())
	#'1 2 3 4 5\nWork with file\n'
	f.close()
#file()

### відкриття файла через контекстний менеджер дозволяє не турбуватись про закриття після помилки
with open('file.txt', 'w') as file_data:
    file_data.write('hello')

print('\n manager1 \n')
### якийсь ресурс який потребує закриття функцією post_work()
class Resource:
    def __init__(self, name):
        print('Resource: create {}'.format(name))
        self.__name = name
    def get_name(self):
        return self.__name
    def post_work(self):
        print('Resource: close')

## власні менеджери
## variant 1
class ResourceForWith:
    def __init__(self, name):
        self.__resource = Resource(name)
    def __enter__(self):
        return self.__resource
    def __exit__(self, type, value, traceback):
        self.__resource.post_work()

with ResourceForWith('Worker') as r:
    print(r.get_name())

## variant 2
print('\n manager2 \n')
from contextlib import contextmanager
@contextmanager
def processor():
    print('--> start processing')
    yield
    print('<-- stop processing')

with processor():
    print(':: processing')


## sudo pip3 install mypy
## python3 -m mypy one.py
## Success: no issues found in 1 source file

print('\n annotation \n')
### annotation
def repeater(s: str, n: int) -> str:
   return s * n

print(  repeater('10', 10) )



if __name__ == "__main__":
	print('main')



