


class figure:
	param1=1
	param2=2

	def __init__(self,):
		print('init')

	def run():
		print('run')


class rect(figure):
	param3=1

	def run(self,):
		print('run rect')


a = figure()
b = rect()

print( vars(figure) )
print( vars(rect) )



#####################################################################



class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

# Chield 
class NonDecreasingCounter(Counter):  
    def dec(self):
        pass

n = NonDecreasingCounter()
n.inc()
n.inc()
n.inc()
print(n.value)
n.dec()
n.dec()
n.dec()
print(n.value)


#########################################################################

## память предков)
class DoubleCounter(Counter):
    def inc(self):
        super().inc()
        super().inc()




