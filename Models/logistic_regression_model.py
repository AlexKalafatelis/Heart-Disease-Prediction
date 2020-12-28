"""Logistic Regression Model

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable,
 although many more complex extensions exist.

In a binary logistic regression model, the dependent variable has two levels (categorical).
  Outputs with more than two values are modeled by multinomial logistic regression and, if the multiple categories are ordered,
  by ordinal logistic regression (for example the proportional odds ordinal logistic model).

The logistic regression model itself simply models probability of output in terms of input and does not perform
  statistical classification (it is not a classifier), though it can be used to make a classifier,
  for instance by choosing a cutoff value and classifying inputs with probability greater than the cutoff as one class,
  below the cutoff as the other; this is a common way to make a binary classifier.

    via wikipedia (https://en.wikipedia.org/wiki/Logistic_regression)
"""

from sklearn.linear_model import LogisticRegression
import sklearn.metrics
from sklearn import metrics
from sklearn.metrics import f1_score, log_loss, accuracy_score
from sklearn.metrics import roc_curve, auc #for model evaluation
from sklearn.metrics import classification_report, balanced_accuracy_score #for model evaluation
from sklearn.metrics import confusion_matrix #for model evaluation
from sklearn.model_selection import train_test_split #for data splitting



X_train, X_test, y_train, y_test = train_test_split(dt.drop('target', 1), dt['target'], test_size = .3, random_state=5) #split the data

model = LogisticRegression()
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
plt.title("Logistic Regression Confusion Matrix")
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
