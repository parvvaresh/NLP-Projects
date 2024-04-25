from read_file import create_dataset
from pre_process import preprocessing
from word2vec.tf_idf import tfidf
from word2vec.freq_word import freqword 
from word2vec.select_best_feature import select_KBest
from word2vec.bow import bow


from sklearn.model_selection import train_test_split

from models.knn import knn
from models.decision_tree import decision_tree
from models.logstic_regression import logstic_regression
from models.naive_bayes import naive_bayes
from models.random_forest import random_forest 

from plots.plots import create_plot

import warnings
warnings.filterwarnings('ignore')



df = create_dataset()
y = df["target"].values

pre_proc = preprocessing()
df = pre_proc.fit(df)
t_i = tfidf()
tf_idf_x = t_i.fit(df, "Text")
tf_idf_x_train, tf_idf_x_test, tf_idf_y_train, tf_idf_y_test = train_test_split(tf_idf_x, y,random_state=0, test_size=0.2)
tf_idf_x_train, tf_idf_x_test, tf_idf_y_train, tf_idf_y_test = select_KBest(tf_idf_x_train, tf_idf_x_test, tf_idf_y_train, tf_idf_y_test , k=200)

fw = freqword(df, "Text", "target")
freq_word_x = fw.transform()
freq_word_x_train, freq_word_x_test, freq_word_y_train, freq_word_y_test = train_test_split(freq_word_x, y,random_state=0, test_size=0.2)


bw = bow()
bw.fit(df, "Text")
bw_x = bw.transform(df, "Text")
bow_x_train, bow_x_test, bow_y_train, bow_y_test = train_test_split(bw_x, y,random_state=0, test_size=0.2)

bow_x_train, bow_x_test, bow_y_train, bow_y_test = select_KBest(bow_x_train, bow_x_test, bow_y_train, bow_y_test , k=100)


tf_idf_acc = {
	"KNN" : None,
	"Logstic Regression" : None,
	"Decision Tree" : None,
	"Random Forest" : None,
	"Naive Bayes" : None,
}

freq_word_acc = {
	"KNN" : None,
	"Logstic Regression" : None,
	"Decision Tree" : None,
	"Random Forest" : None,
	"Naive Bayes" : None,
}


bow_acc = {
	"KNN" : None,
	"Logstic Regression" : None,
	"Decision Tree" : None,
	"Random Forest" : None,
	"Naive Bayes" : None,
}

lg_tf_idf = logstic_regression()

lg_tf_idf.fit(tf_idf_x_train, tf_idf_y_train)
y_pred = lg_tf_idf.predict(tf_idf_x_test)
acc_lg = lg_tf_idf.accuracy(y_pred, tf_idf_y_test)
print(f"accuracy of logstic regression for tf-idf vec is {acc_lg * 100} %")
tf_idf_acc["Logstic Regression"] = acc_lg



lg_fq = logstic_regression()

lg_fq.fit(freq_word_x_train, freq_word_y_train)
y_pred = lg_fq.predict(freq_word_x_test)
acc_lg = lg_fq.accuracy(y_pred, freq_word_y_test)
print(f"accuracy of logstic regression for freq-word vec is {acc_lg * 100} %")
freq_word_acc["Logstic Regression"] = acc_lg


lg_bow = logstic_regression()

lg_bow.fit(bow_x_train, bow_y_train)
y_pred = lg_bow.predict(bow_x_test)
acc_lg = lg_bow.accuracy(y_pred, bow_y_test)
print(f"accuracy of logstic regression for freq-word vec is {acc_lg * 100} %")
bow_acc["Logstic Regression"] = acc_lg

KNN_tf_idf = knn()

KNN_tf_idf.fit(tf_idf_x_train, tf_idf_y_train)
y_pred = KNN_tf_idf.predict(tf_idf_x_test, 11)
acc_knn = KNN_tf_idf.accuracy(y_pred, tf_idf_y_test)
print(f"accuracy of knn for tf-idf vec is {acc_knn * 100} %")
tf_idf_acc["KNN"] = acc_knn


KNN_fq = knn()

KNN_fq.fit(freq_word_x_train, freq_word_y_train)
y_pred = KNN_fq.predict(freq_word_x_test, 11)
acc_knn = KNN_fq.accuracy(y_pred, freq_word_y_test)
print(f"accuracy of knn for freq-word vec is {acc_knn * 100} %")
freq_word_acc["KNN"] = acc_knn


KNN_bow = knn()

KNN_bow.fit(bow_x_train, bow_y_train)
y_pred = KNN_bow.predict(bow_x_test, 11)
acc_knn = KNN_bow.accuracy(y_pred, bow_y_test)
print(f"accuracy of knn for bag of word vec is {acc_knn * 100} %")
bow_acc["KNN"] = acc_knn



dt_tf_idf = decision_tree(max_depth = 10)

dt_tf_idf.fit(tf_idf_x_train, tf_idf_y_train)
y_pred = dt_tf_idf.predict(tf_idf_x_test)
acc_dt = dt_tf_idf.accuracy(y_pred, tf_idf_y_test)
print(f"accuracy of decision tree for tf-idf vec is {acc_dt * 100} %")
tf_idf_acc["Decision Tree"] = acc_dt


dt_fq = decision_tree(max_depth = 10)

dt_fq.fit(freq_word_x_train, freq_word_y_train)
y_pred = dt_fq.predict(freq_word_x_test)
acc_dt = dt_fq.accuracy(y_pred, freq_word_y_test)
print(f"accuracy of decision tree for freq-word vec is {acc_dt * 100} %")
freq_word_acc["Decision Tree"] = acc_dt


dt_bow = decision_tree(max_depth = 10)

dt_bow.fit(bow_x_train, bow_y_train)
y_pred = dt_bow.predict(bow_x_test)
acc_dt = dt_bow.accuracy(y_pred, bow_y_test)
print(f"accuracy of decision tree for bag of word vec is {acc_dt * 100} %")
bow_acc["Decision Tree"] = acc_dt

rf_tf_idf = random_forest(n_trees = 5, max_depth = 10)

rf_tf_idf.fit(tf_idf_x_train, tf_idf_y_train)
y_pred = rf_tf_idf.predict(tf_idf_x_test)
acc_rf = rf_tf_idf.accuracy(y_pred, tf_idf_y_test)
print(f"accuracy of drandom forest for tf-idf vec is {acc_rf * 100} %")
tf_idf_acc["Random Forest"] = acc_rf



rf_fq = random_forest(n_trees = 5, max_depth = 10)

rf_fq.fit(freq_word_x_train, freq_word_y_train)
y_pred = rf_fq.predict(freq_word_x_test)
acc_rf = rf_fq.accuracy(y_pred, freq_word_y_test)
print(f"accuracy of drandom forest for freq-word vec is {acc_rf * 100} %")
freq_word_acc["Random Forest"] = acc_rf



rf_bow = random_forest(n_trees = 5, max_depth = 10)

rf_bow.fit(bow_x_train, bow_y_train)
y_pred = rf_bow.predict(bow_x_test)
acc_rf = rf_bow.accuracy(y_pred, bow_y_test)
print(f"accuracy of drandom forest for bag of word vec is {acc_rf * 100} %")
bow_acc["Random Forest"] = acc_rf

nb_tf_idf = naive_bayes()

nb_tf_idf.fit(tf_idf_x_train, tf_idf_y_train)
y_pred = nb_tf_idf.predict(tf_idf_x_test)
acc_nb = nb_tf_idf.accuracy(y_pred, tf_idf_y_test)
print(f"accuracy of naive bayes for tf-idf vec is {acc_nb * 100} %")
tf_idf_acc["Naive Bayes"] = acc_nb


nb_fq = naive_bayes()

nb_fq.fit(freq_word_x_train, freq_word_y_train)
y_pred = nb_fq.predict(freq_word_x_test)
acc_nb = nb_fq.accuracy(y_pred, freq_word_y_test)
print(f"accuracy of naive bayes for feq-word vec is {acc_nb * 100} %")
freq_word_acc["Naive Bayes"] = acc_nb

nb_bow = naive_bayes()

nb_bow.fit(bow_x_train, bow_y_train)
y_pred = nb_bow.predict(bow_x_test)
acc_nb = nb_bow.accuracy(y_pred, bow_y_test)
print(f"accuracy of naive bayes for bag of word vec is {acc_nb * 100} %")
bow_acc["Naive Bayes"] = acc_nb

create_plot(tf_idf_acc, freq_word_acc, bow_acc)
