import pandas as pd
path = 'F:\Main Project\Python\Scikit MLT\dir.tsv'
t_path = 'F:\Main Project\Python\Scikit MLT\dirE.tsv'
dirData = pd.read_table(path, header=None, names=['Label', 'Group'])
tData = pd.read_table(t_path,header=None, names=['Label', 'Group'])
# print dirData.shape
# print dirData.Label.value_counts()
X_train = dirData.Label
y_train = dirData.Group
X_test = tData.Label
y_test = tData.Group
# print X_test.head(30)
# print (X)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import  CountVectorizer
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 1)
# print X_train
# print X_test.shape
vect = CountVectorizer()
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
# # X_train_dtm = vect.fit_transform(X_train) is Equivalent to 15, 16
X_test_dtm = vect.transform(X_test)
print X_test_dtm [25]
# print pd.DataFrame(X_test_dtm.toarray(), columns= vect.get_feature_names())
ls = vect.get_feature_names()
print ls[18], ls[23], ls[50], ls[85], ls[91], ls[114], ls[151]
# print X_test_dtm[17].toarray()
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier()
# knn.fit(X_train_dtm, y_train)
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
od= X_test_dtm[25].toarray()
print od
print OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train_dtm, y_train).predict(od)
# print knn.predict(X_test_dtm[17].toarray)