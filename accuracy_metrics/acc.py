
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
print( accuracy_score(y_true, y_pred) )

print(confusion_matrix(y_true, y_pred))
