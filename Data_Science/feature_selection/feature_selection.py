

def feature_importance(X,y):
	from sklearn.ensemble import ExtraTreesClassifier
	from sklearn.datasets import load_iris
	from sklearn.feature_selection import SelectFromModel
	print('data shape',X.shape)

	clf = ExtraTreesClassifier(n_estimators=50)
	clf = clf.fit(X, y)
	print( clf.feature_importances_ )  

	model = SelectFromModel(clf, prefit=True)
	X_new = model.transform(X)
	print('new shape',X_new.shape)               
	return X_new, model 
