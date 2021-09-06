

#5 cats, 5 no cats
labels = [1,1,1,1,1,0,0,0,0,0,0]
resalt = [1,1,1,1,0,0,0,0,0,1,1]

# TP = true positive  = 4 
# FP = false positive = 2
# FN = false negative = 1
# TN = true negative  = 4

# recall / sensitivity / True positive rate
# 4/5 = TP/(TP+TN) = how many cats we have detected from all cats

# false negative rate / miss rate
# 1/5 = TN(TP+TN) = how many cats we have not detected from all cats

# true negative rate / selectivity / specificity
# 4/6 = TN/(FP+TN) = how many negatives are detected as negative

# false positive rate / false detections / Fall-out
# 2/6 = FP/(FP+TN) = false detections

### summary 

# prelevalence
# 5/11 = Condition positive / Total population

# PPV / precision
# 4/6 = TP/(TP+FP) = how many positive results are really true 
# as example if sensitivity = 0.9, specificity = 0.8 but Prevalence<0.5 then precision will fall fast

# accuracy 
# 8/11 = TP+TN/(all) = contain in self true and false detection rates



from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]

print( accuracy_score(y_true, y_pred) )
print(confusion_matrix(y_true, y_pred))





