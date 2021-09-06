import numpy as np
from collections import Counter
def entropy(y):
    hist = np.bincount(y)
    ps = hist / len(y)
    return -np.sum([p * np.log2(p) for p in ps if p > 0])
class Node:

    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:

    def __init__(self, min_samples_split=2, max_depth=100, n_feats=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_feats = n_feats
        self.root = None

    def fit(self, X, y):
        self.n_feats = X.shape[1] if not self.n_feats else min(self.n_feats, X.shape[1])
        #print('grow')
        self.root = self._grow_tree(X, y)
        #print('  root  ',self.root.left)

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        #print('samples and features',  n_samples, n_features)
        #print(X,y)
        n_labels = len(np.unique(y))

        #stopping criteria
        if (depth >= self.max_depth or n_labels == 1  or n_samples < self.min_samples_split):

            leaf_value = self._most_common_label(y)
            #print('leaf_value',leaf_value)
            return Node(value=leaf_value)

        #print(n_features, self.n_feats)
        feat_idxs = np.random.choice(n_features, self.n_feats, replace=False)
        #print('random choise',feat_idxs)

        #greedily select the best split according to information gain
        #print('select best from X=', X, 'y=', y, 'feat=', feat_idxs)
        best_feat, best_thresh = self._best_criteria(X, y, feat_idxs)
        #print('best', best_feat, best_thresh)
        
        #grow the children that result from the split
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth+1)
        return Node(best_feat, best_thresh, left, right)

    def _best_criteria(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_thresh = None, None
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            #print('X_column',X_column)
            thresholds = np.unique(X_column)
            
            for threshold in thresholds:
                #print("thr's", thresholds,threshold)
                gain = self._information_gain(y, X_column, threshold)
                #print('gain',gain)
                if gain > best_gain:
                    #print('best_gain',best_gain)
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold

        return split_idx, split_thresh

    def _information_gain(self, y, X_column, split_thresh):
        #parent loss
        parent_entropy = entropy(y)

        #generate split
        left_idxs, right_idxs = self._split(X_column, split_thresh)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        #compute the weighted avg. of the loss for the children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = entropy(y[left_idxs]), entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        #print('child_entropy',child_entropy, 'parent_entropy', parent_entropy)
        #print('y[left_idxs]',y[left_idxs],'idx', left_idxs)
        #print('y[right_idxs]',y[right_idxs],'idx', right_idxs)
        #information gain is difference in loss before vs. after split
        ig = parent_entropy - child_entropy
        return ig

    def _split(self, X_column, split_thresh):
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

    def _most_common_label(self, y):
        counter = Counter(y)
        most_common = counter.most_common(1)[0][0]
        return most_common

from sklearn import datasets
from sklearn.model_selection import train_test_split
def accuracy(y_true, y_pred):   
    accuracy = np.sum(y_true == y_pred)/len(y_true)   
    return accuracy

def test1():
	data = datasets.load_breast_cancer()
	X = data.data
	y = data.target
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=123)

	clf = DecisionTree(max_depth = 10)
	clf.fit(X_train, y_train)
	y_pred1 = clf.predict(X_train)
	acc1 = accuracy(y_train, y_pred1)
	print("Training Accuracy: ", acc1)
	#Out:
	#Training Accuracy: 1.0
	y_pred2 = clf.predict(X_test) 
	acc2 = accuracy(y_test, y_pred2)
	print("Testing Accuracy: ", acc2)

def test2():
	X_train = np.array([[0, 0, 0],[0.1,0.11, 0.12], [1, 1,1], [1.4, 1.41,1.42], [2,2, 2], [3,3, 3]])
	y_train = np.array([0, 0, 1, 1, 2, 3])
	X_test =  np.array([[0,0,0],[0.7,0.7,0.7],[4,4,4]])
	y_test =  np.array([0, 1, 3])

	clf = DecisionTree(max_depth = 10)
	clf.fit(X_train, y_train)

	print('--predict--')
	y_pred1 = clf.predict(X_train)
	acc1 = accuracy(y_train, y_pred1)
	print("Training Accuracy: ", acc1)
	#Out:
	#Training Accuracy: 1.0
	y_pred2 = clf.predict(X_test) 
	acc2 = accuracy(y_test, y_pred2)
	print("Testing Accuracy: ", acc2)




if __name__ == "__main__":
	test2()







