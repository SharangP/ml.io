from sklearn.datasets import load_iris
from mltask import MLTask
from algorithms import METHODS

d = load_iris()
data = {}
data['features'] = d.data
data['targets'] = d.target
meta_data = {
        'cross_validation_test_size': 0.5,
        'cross_validation_run': True,
        'test_run': False}
for method in METHODS:
    for sub_method in METHODS[method]:
        try:
            print sub_method
            ml = MLTask([method, sub_method], meta_data, data)
            ml.run()
            r = ml.results()
            print r
        except TypeError, e:
            print "ERROR: " + e.message
