"""AdaBoost Model

https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html


An AdaBoost classifier is a meta-estimator that begins by fitting a classifier on the original dataset &
 then fits additional copies of the classifier on the same dataset but where the weights of incorrectly
 classified instances are adjusted such that subsequent classifiers focus more on difficult cases.

This class implements the algorithm known as AdaBoost-SAMME

"""

from sklearn.ensemble import AdaBoostClassifier
import sklearn.metrics
from sklearn import metrics
from sklearn.metrics import f1_score, log_loss, accuracy_score
from sklearn.metrics import roc_curve, auc #for model evaluation
from sklearn.metrics import classification_report, balanced_accuracy_score #for model evaluation
from sklearn.metrics import confusion_matrix #for model evaluation
from sklearn.model_selection import train_test_split #for data splitting



X_train, X_test, y_train, y_test = train_test_split(dt.drop('target', 1), dt['target'], test_size = .3, random_state=5) #split the data

model = AdaBoostClassifier()
model.fit(X_train, y_train) #fit

y_predict = model.predict(X_test)
y_pred_quant = model.predict_proba(X_test)[:, 1]
y_pred_bin = model.predict(X_test)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)
print("Training Data Shape:", y_train.shape)
print("Testing Data Shape:", y_test.shape)


#Confusion Matrix
cm = confusion_matrix(y_test, y_pred_bin)
plt.title("AdaBoost Confusion Matrix")
sns.heatmap(cm,annot=True,cmap="Blues",fmt="d",cbar=False, annot_kws={"size": 24})
plt.show


#Printing results
total=sum(sum(cm))

print((metrics.classification_report(y_test, y_pred_bin, digits=3)))

sensitivity = cm[0,0]/(cm[0,0]+cm[1,0])
print('Sensitivity : ', sensitivity )

specificity = cm[1,1]/(cm[1,1]+cm[0,1])
print('Specificity : ', specificity)

print('Balanced Accuracy : ', balanced_accuracy_score(y_test, y_pred_bin,sample_weight=None, adjusted=False))

print('f1 score :', f1_score(y_test, y_pred_bin, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn'))



#ROC Curve & AUC Score
fpr, tpr, thresholds = roc_curve(y_test, y_pred_quant)

fig, ax = plt.subplots()
ax.plot(fpr, tpr)
ax.plot([0, 1], [0, 1], transform=ax.transAxes, ls="--", c=".3")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.rcParams['font.size'] = 12
plt.title('ROC Curve')
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.grid(True)
auc(fpr, tpr) #auc score
