import pandas as pd
path = 'F:\Main Project\Python\Scikit MLT\dir.tsv'
dirData = pd.read_table(path, header=None, names=['Label', 'Group'])
# print dirData.shape
# print dirData.Label.value_counts()
X = dirData.Label
y = dirData.Group
# print (X)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import  CountVectorizer
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 1)
# print X_train
# print X_test.shape
vect = CountVectorizer()
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
# X_train_dtm = vect.fit_transform(X_train) is Equivalent to 15, 16
X_test_dtm = vect.transform(X_test)
# print X_test_dtm


from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_dtm,y_train)
y_pred_class = nb.predict(X_test_dtm)
print y_pred_class
#
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class)
metrics.confusion_matrix(y_test, y_pred_class)
# print X_test[y_pred_class < y_test]
y_pred_prob = nb.predict_proba(X_test_dtm)[:, 1]
print y_pred_prob
# print nb.predict_proba(X_test_dtm)
# print metrics.roc_auc_score(y_test,y_pred_prob)

# from sklearn.linear_model import LogisticRegression
# logreg = LogisticRegression()
# logreg.fit(X_train_dtm, y_train)
# y_pred_class = logreg.predict(X_test_dtm)
# print y_pred_class, X_test_dtm
# y_pred_prob = logreg.predict_proba(X_test_dtm)[:, 1]
# print metrics.accuracy_score(y_test, y_pred_class)

# metrics.roc_auc_score(y_test, y_pred_class)
