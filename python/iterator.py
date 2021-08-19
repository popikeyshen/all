class SimpleIterator:
	def __init__(self,):
		self.counter = 0
	def __next__(self):
		self.counter += 1
		return self.counter


s = SimpleIterator()
print( next(s) )
print( next(s) )

## not iterable cause has not __iter__ object
#for i in s:
#	print( i )


### https://devpractice.ru/python-lesson-15-iterators-and-generators/
### создание итератора 
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0


    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

s1 = SimpleIterator(3)
print('s1',next(s1))
print('s1',next(s1))
print('s1',next(s1))
##print(next(s_iter1)) error stop iteration

s2 = SimpleIterator(3)
for i in s2:
	print("s2", i)
