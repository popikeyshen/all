
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def sample1():
	X, y = make_classification(n_samples=1000, n_features=4,
		                   n_informative=2, n_redundant=0,
		                   random_state=0, shuffle=False)
	clf = RandomForestClassifier(max_depth=2, random_state=0)
	clf.fit(X, y)

	print(clf.predict([[0, 0, 0, 0]]))


def sample2():
	X = [[0, 0], [1, 1], [2, 2], [3, 3]]
	y = [0, 1, 2, 3]
	clf = RandomForestClassifier(max_depth=2, random_state=0)
	clf.fit(X, y)

	print(clf.predict([[0.4,0.4]]))
	print(clf.predict([[0.6,0.6]]))

if __name__ == '__main__':
	#sample1()
	sample2()

