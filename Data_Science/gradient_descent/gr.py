
# example of gradient descent for a one-dimensional function
from numpy import asarray
from numpy.random import rand
 
# objective function
def objective(x):
	return x**2.0
 
# derivative of objective function
def derivative(x):
	return x * 2.0
 
# gradient descent algorithm
def gradient_descent(objective, derivative, bounds, n_iter, step_size):
	# generate an initial point
	solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	print('s ',solution)
	# run the gradient descent
	for i in range(n_iter):
		# calculate gradient
		gradient = derivative(solution)

		# take a step
		solution = solution - step_size * gradient

		# evaluate candidate point
		solution_eval = objective(solution)
		# report progress
		print('>%d f(%s) = %.5f, gradient %.5f' % (i, solution, solution_eval,gradient))
	return [solution, solution_eval]
 
# define range for input
bounds = asarray([[-1.0, 1.0]])
# define the total iterations
n_iter = 30
# define the step size
step_size = 0.1
# perform the gradient descent search
best, score = gradient_descent(objective, derivative, bounds, n_iter, step_size)
print('Done!')
print('f(%s) = %f' % (best, score))


## https://machinelearningmastery.com/gradient-descent-optimization-from-scratch/
## https://towardsdatascience.com/gradient-descent-from-scratch-e8b75fa986cc
