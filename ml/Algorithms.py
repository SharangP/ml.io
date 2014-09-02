import sklearn

CLASSIFIERS = {
        'Support Vector Machine' : {
            'class' : sklearn.svm.SVC, 
            'required_params' : ['kernel', 'C']
            },
        'K Neighbors Classifier' : {
            'class' : sklearn.neighbors.KNeighborsClassifier,
            'required_params' : ['k']
            },
        'Decision Tree Classifier' : {
            'class' : sklearn.tree.DecisionTreeClassifier,
            'required_params' : ['max_depth']
            },
        'Random Forest Classifier' : {
            'class' : sklearn.ensemble.RandomForestClassifier,
            'required_params' : ['max_depth', 'n_estimators', 'max_features']
            },
        'AdaBoost Classifier' : {
            'class' : ensemble.AdaBoostClassifier,
            'required_params' : []
            },
        'Gaussian Naive Bayes' : {
            'class' : sklearn.naive_bayes.GaussianNB,
            'required_params' : []
            },
        'Linear Discriminant' : {
            'class' : sklearn.lda.LDA,
            'required_params' : []
            },
        'Quadratic Discriminant' : {
            'class' : sklearn.qda.QDA,
            'required_params' : []
            },
        }

CLUSTERING = {
        'K Means' : {
            'class' : sklearn.cluster.KMeans,
            'required_params' : ['k']
            }
        }

REGRESSION = {
        'Linear Regression' : {
            'class' : sklearn.linear_model.LinearRegression,
            'required_params' : []
            }
        }
