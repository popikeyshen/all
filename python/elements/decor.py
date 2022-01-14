

## func as object

def mul(a):
    def helper(b):
        return a * b
    return helper

print( mul(3)(5) )

a = mul(3)
print( a(5) )




### wrapper v1


def w1(fn):
	import time 
	def w2(arg):
		k=10	
		print('start k times:')

		t = time.time()
		for i in range(k):
			res = fn(arg)

		print((time.time()-t)/k)
	
		return res
	return w2


@w1 # simple decorator
def factorial(a):

	buf = 1	
	for i in range(a):  ## for a<0 look Gamma function
		buf *=a  
		a -= 1
	return buf



param = 5
print( factorial( param ) )
