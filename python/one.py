

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











