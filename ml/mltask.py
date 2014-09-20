import numpy as np
from sklearn import linear_model, cross_validation
from task import Task
from algorithms import METHODS

METADATA = {
        'desc': {
            'type': 'text',
            'default': None
            },
        'feature_names': {
            'type': 'list',
            'default': None
            },
        'target_names': {
            'type': 'list',
            'default': None
            },
        'cross_validation_run': {
            'type': 'bool',
            'default': False
            },
        'test_run': {
            'type': 'bool',
            'default': False
            },
        'cross_validation_iterations': {
            'type': 'int',
            'default': 10
            },
        'cross_validation_size': {
            'type': 'float',
            'default': 0.2
            },
        }

class MLTask(Task):
    '''
    Object to encapsulate Machine Learning
    '''
    def __init__(self, model, meta_data={}, data={}, test={}):
        self._meta_data, self._data, self._test = ({},) * 3
        self._results = {'score': None}

        self._set_meta_data(meta_data)
        self._set_model(model)
        self._set_training_data(data)
        self._set_test_data(test)

    def run(self):
        if self._meta_data['cross_validation_run']:
            self._cross_validate()
        if self._meta_data['test_run']:
            self._test()

    def results(self):
        return self._results['score']

    def _set_meta_data(self, s):
        for key, value in METADATA.items():
            self._meta_data[key] = value['default'] if not s.has_key(key) else s[key]

    def _set_model(self, m):
        '''
        Set ML model based on input dict and Algorithms available
        '''
        #TODO: ensure setting the model doesn't break
        self._model = METHODS[m[0]][m[1]]['class']()

    def _set_training_data(self, d):
        if len(d):
            self._data['features'] = np.array([]) if len(d['features']) == 0 else d['features']
            self._data['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']

    def _set_test_data(self, d):
        if len(d):
            self._test['features'] = np.array([]) if len(d['features']) == 0 else d['features']
            self._test['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']
            
    def _cross_validate(self):
        scores = cross_validation.cross_val_score(
                self._model, self._data['features'], self._data['targets'],
                cv=self._meta_data['cross_validation_iterations'])
        self._results['score'] = np.mean(scores)
            
    def _test(self):
        self._model.fit(self._data['features'], self._data['targets'])
        self._results['test_score'] = self._model.score(self._test['features'], self._test['targets'])
