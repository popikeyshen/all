





def gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n



print('1', next(gen()))
print('2', next(gen()))
print('3', next(gen()))
print('4', next(gen()))

a=gen()
print('a 1', next(a))
print('a 2', next(a))
print('a 3', next(a))
#print('a 4', next(a))  # error



def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)



