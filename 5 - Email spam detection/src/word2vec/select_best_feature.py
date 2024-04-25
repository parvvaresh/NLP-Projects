from sklearn.feature_selection import SelectKBest, chi2

def select_KBest(x_train, x_test, y_train, y_test, k = 250):
    
	transformer = SelectKBest(chi2, k=k).fit(x_train, y_train)
	x_train = transformer.transform(x_train)
	x_test = transformer.transform(x_test)

	return x_train, x_test, y_train, y_test
