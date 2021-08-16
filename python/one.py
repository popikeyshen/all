

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


# лямбда функции (любое число аргументов, не более одной инструкции)
(lambda x: x**2)(5)

# присваиваем переменной 
sqrt = lambda x: x**0.5
print( sqrt(25) )


# исключения (иерархия исключений https://devpractice.ru/python-lesson-11-work-with-exceptions/ )
print("start")
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)
except(ValueError, ZeroDivisionError):
   print("Error!")
print("stop")


try:
   raise Exception("Some exception")
except Exception as e:
   print("Exception exception " + str(e))



### работа с файлами
f = open("test.txt", "r")
print(f.read())
#'1 2 3 4 5\nWork with file\n'
f.close()


### https://devpractice.ru/python-lesson-15-iterators-and-generators/
### создание итератора 
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter1 = SimpleIterator(3)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))


### генераторы
def simple_generator(val):
   while val > 0:
       val -= 1
       yield 1

gen_iter = simple_generator(5)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))














