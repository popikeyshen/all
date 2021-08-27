import numpy as np 
from collections import Counter
from decision_Tree import DecisionTree

def bootstrap_sample(X, y):
    n_samples = X.shape[0]
    idxs = np.random.choice(n_samples, n_samples, replace=True)
    return X[idxs], y[idxs]
def most_common_label(y):
    counter = Counter(y)
    most_common = counter.most_common(1)[0][0]
    return most_common
class RandomForest:
    
    def __init__(self, n_trees=10, min_samples_split=2,
                 max_depth=100, n_feats=None):
        self.n_trees = n_trees
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_feats = n_feats
        self.trees = []

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            tree = DecisionTree(min_samples_split=self.min_samples_split, max_depth=self.max_depth, n_feats=self.n_feats)
            X_samp, y_samp = bootstrap_sample(X, y)
            tree.fit(X_samp, y_samp)
            self.trees.append(tree)

    def predict(self, X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        y_pred = [most_common_label(tree_pred) for tree_pred in tree_preds]
        return np.array(y_pred)

from sklearn import datasets
from sklearn.model_selection import train_test_split
def accuracy(y_true, y_pred):   
    accuracy = np.sum(y_true == y_pred)/len(y_true)   
    return accuracy

def test1():
	data = datasets.load_breast_cancer()
	X = data.data
	y = data.target
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=123)
	clf = RandomForest(n_trees = 3)
	clf.fit(X_train, y_train)
	y_pred = clf.predict(X_train) 
	acc1 = accuracy(y_train, y_pred)
	print("Training Accuracy: ", acc1)

def test2():
	X_train = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
	y_train = np.array([0, 1, 2, 3])

	X_test = np.array([[-0.1,-0.1]])
	y_test = np.array([0])

	clf = RandomForest(n_trees = 3)
	clf.fit(X_train, y_train)
	y_pred = clf.predict(X_train) 
	print(y_pred)
	acc1 = accuracy(y_train, y_pred)
	print("Training Accuracy: ", acc1)

	y_pred = clf.predict(X_test) 
	print(y_pred)

if __name__ == "__main__":
	#test1()
	test2()


# https://python.plainenglish.io/random-forest-from-scratch-fcaeb0bed09a
# https://medium.com/swlh/decision-tree-from-scratch-a72069240293
# https://towardsdatascience.com/master-machine-learning-random-forest-from-scratch-with-python-3efdd51b6d7a






