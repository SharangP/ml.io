CLASSIFIERS = {
        'Support Vector Machine' : {
            'class' : 'SVC',
            'required_params' : ['kernel', 'C']
            },
        'K Neighbors Classifier' : {
            'class' : 'KNeighborsClassifier',
            'required_params' : ['k']
            },
        'Decision Tree Classifier' : {
            'class' : 'DecisionTreeClassifier',
            'required_params' : ['max_depth']
            },
        'Random Forest Classifier' : {
            'class' : 'RandomForestClassifier',
            'required_params' : ['max_depth', 'n_estimators', 'max_features']
            },
        'AdaBoost Classifier' : {
            'class' : 'AdaBoostClassifier',
            'required_params' : []
            },
        'Gaussian Naive Bayes' : {
            'class' : 'GaussianNB',
            'required_params' : []
            },
        'Linear Discriminant' : {
            'class' : 'LDA',
            'required_params' : []
            },
        'Quadratic Discriminant' : {
            'class' : 'QDA',
            'required_params' : []
            },
        }

CLUSTERING = {
        'K Means' : {
            'class' : 'KMeans',
            'required_params' : ['k']
            }
        }

REGRESSION = {
        'Linear Regression' : {
            'class' : 'LinearRegression',
            'required_params' : []
            }
        }
