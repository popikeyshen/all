from sklearn import svm

X = [[0, 0], [1, 1], [2, 2], [3, 3]]
y = [0, 1, 2, 3]
clf = svm.SVC()
clf.fit(X, y)

print(clf.predict([[0.55, 0.55]]),  clf.predict([[0.45, 0.45]])   )


regr = svm.LinearSVR()
regr.fit(X, y)

print(regr.predict([[4, 4]]),  regr.predict([[5, 5]])  )
