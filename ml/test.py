from sklearn.datasets import load_iris
from MLTask import MLTask
from Algorithms import METHODS

d = load_iris()
data = {}
data['features'] = d.data
data['targets'] = d.target
schema = {'cross_validation_test_size': 0.5}
for method in METHODS:
    for sub_method in METHODS[method]:
        try:
            print sub_method
            ml = MLTask([method, sub_method], schema, data)
            ml.run()
            r = ml.results()
            print r
        except TypeError, e:
            print "ERROR: " + e.message
