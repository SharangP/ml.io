import numpy as np
from sklearn import linear_model, cross_validation
from Task import Task
from Algorithms import *


class MLTask(Task):
    '''
    Object to encapsulate Machine Learning
    '''
    def __init__(self, schema={}, model={}, data={}, test={}):
        self._schema, self._data, self._test = ({},) * 3
        self._model = ''
        self._results = {'score': None}
        self.set_schema(schema)
        self.set_model(model)
        self.set_data(data)
        self.set_test(test)

    def run(self):
        if self._test:
            self._model.fit(self._data['features'], self._data['targets'])
            self._results['score'] = self._model.score(self._test['features'], self._test['targets'])
        else:
            X_train, X_test, y_train, y_test = cross_validation.train_test_split(
                    self._data['features'], self._data['targets'],
                    test_size=self._schema['cross_validation_test_size'])
            self._model.fit(X_train, y_train)
            self._results['score'] = self._model.score(X_test, y_test)

    def results(self):
        return self._results['score']

    def set_schema(self, s):
        self._schema['desc'] = None if not s.has_key('desc') else s['desc']
        self._schema['feature_names'] = None if not s.has_key('feature_names') else s['feature_names']
        self._schema['target_names'] = None if not s.has_key('target_names') else s['target_names']
        self._schema['cross_validation_test_size'] = 0.4 if not s.has_key('cross_validation_test_size') else s['cross_validation_test_size']

    def set_model(self, m):
        '''
        Set ML model based on input dict and Algorithms available
        '''
        self._model = linear_model.LinearRegression()

    def set_data(self, d):
        self._data['features'] = np.array([]) if len(d['features']) == 0 else d['features']
        self._data['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']

    def set_test(self, d):
        if len(d) > 0:
            self._test['features'] = np.array([]) if len(d['features']) == 0 else d['features']
            self._test['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']
