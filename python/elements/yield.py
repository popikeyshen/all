





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



print('as function() ', next(gen()))
print('as function() ', next(gen()))
print('as function() ', next(gen()))
print('as function() ', next(gen()))

a=gen()
print('as variable ', next(a))
print('as variable ', next(a))
print('as variable ', next(a))
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
    print('as function() ',item)

a = my_gen()
# Using for loop
for item in a:
    print('as variable ',item)

