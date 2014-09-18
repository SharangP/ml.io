import numpy as np
from sklearn import linear_model, cross_validation
from Task import Task
from Algorithms import METHODS


class MLTask(Task):
    '''
    Object to encapsulate Machine Learning
    '''
    def __init__(self, model, meta_data={}, data={}, test={}):
        self._meta_data, self._data, self._test = ({},) * 3
        self._results = {'score': None}

        self._set_meta_data(meta_data)
        self._set_model(model)
        self._set_data(data)
        self._set_test(test)

    def run(self):
        if self._test:
            self._model.fit(self._data['features'], self._data['targets'])
            self._results['score'] = self._model.score(self._test['features'], self._test['targets'])
        else: #TODO: move cross validation into a method that can take various params
            X_train, X_test, y_train, y_test = cross_validation.train_test_split(
                    self._data['features'], self._data['targets'],
                    test_size=self._meta_data['cross_validation_test_size'])
            self._model.fit(X_train, y_train)
            self._results['score'] = self._model.score(X_test, y_test)

    def results(self):
        return self._results['score']

    def _set_meta_data(self, s):
        self._meta_data['desc'] = None if not s.has_key('desc') else s['desc']
        self._meta_data['feature_names'] = None if not s.has_key('feature_names') else s['feature_names']
        self._meta_data['target_names'] = None if not s.has_key('target_names') else s['target_names']
        self._meta_data['cross_validation_test_size'] = 0.4 if not s.has_key('cross_validation_test_size') else s['cross_validation_test_size']

    def _set_model(self, m):
        '''
        Set ML model based on input dict and Algorithms available
        '''
        #TODO: ensure setting the model doesn't break better
        self._model = METHODS[m[0]][m[1]]['class']()

    def _set_data(self, d):
        if len(d):
            self._data['features'] = np.array([]) if len(d['features']) == 0 else d['features']
            self._data['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']

    def _set_test(self, d):
        if len(d):
            self._test['features'] = np.array([]) if len(d['features']) == 0 else d['features']
            self._test['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']
