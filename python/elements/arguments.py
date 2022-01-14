

def argsV1():
	import sys

	print( 'Number of arguments:', len(sys.argv), 'arguments.' )
	print( 'Argument List:', str(sys.argv) )


def argsV2():
	import argparse

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+',  help='an integer for the accumulator')

	args = parser.parse_args()
	print( args.integers )

argsV1()


### распаковка параметров (например листа)
def printScores(car, *scores):
   print(f"car name: {car}")
   for score in scores:
      print(score)
printScores("audi",100, 95, 88, 92, 99)



### передача ** именованных аргументов
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun(first ='one', mid ='two', last='three')  
