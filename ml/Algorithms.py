from sklearn import svm, neighbors, tree, ensemble, naive_bayes, lda, qda, cluster, linear_model

METHODS = {
'Classifiers' : {
    'Support Vector Machine' : {
        'class' : svm.SVC, 
        'required_params' : ['kernel', 'C']
        },
    'K Neighbors Classifier' : {
        'class' : neighbors.KNeighborsClassifier,
        'required_params' : ['k']
        },
    'Decision Tree Classifier' : {
        'class' : tree.DecisionTreeClassifier,
        'required_params' : ['max_depth']
        },
    'Random Forest Classifier' : {
        'class' : ensemble.RandomForestClassifier,
        'required_params' : ['max_depth', 'n_estimators', 'max_features']
        },
    'AdaBoost Classifier' : {
        'class' : ensemble.AdaBoostClassifier,
        'required_params' : []
        },
    'Gaussian Naive Bayes' : {
        'class' : naive_bayes.GaussianNB,
        'required_params' : []
        },
    'Linear Discriminant' : {
        'class' : lda.LDA,
        'required_params' : []
        },
    'Quadratic Discriminant' : {
        'class' : qda.QDA,
        'required_params' : []
        },
    },
'Clustering' : {
    'K Means' : {
        'class' : cluster.KMeans,
        'required_params' : ['k']
        }
    },
'Regression' : {
    'Linear Regression' : {
        'class' : linear_model.LinearRegression,
        'required_params' : []
        }
    }
}
