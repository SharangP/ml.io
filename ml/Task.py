import numpy as np
from sklearn import linear_model

class Task(object):
    """
    Abstract task object
    """

    def __init__(self):
        pass

    def run(self):
        pass

    def results(self):
        pass


class MLTask(Task):

    def __init__(self, schema, model, data, test = None):
        self._schema, self._data, self._test = ({},) * 3
        self._model = ''
        self._results = {'score': None}
        set_schema(schema)
        set_model(model)
        set_data(data)
        set_test(test)

    def run(self):
        self.train_model()
        if len(self._test['features']) > 0:
            self._results['score'] = self._model.score(self._test['features'])
        elif self._schema['cross_validation']:
            pass

    def results(self):
        return self._results['score']

    def set_schema(self, s):
        self._schema['desc'] = None if not s.has_key('desc') else s['desc']
        self._schema['feature_names'] = None if not s.has_key('feature_names') else s['feature_names']
        self._schema['target_names'] = None if not s.has_key('target_names') else s['target_names']
        self._schema['cross_validation'] = False if not s.has_key('cross_validation') else s['cross_validation']

    def set_model(self, m):
        self._model = linear_model.LinearRegression()

    def set_data(self, d):
        self._data['features'] = np.array([]) if len(d['features']) == 0 else d['features']
        self._data['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']

    def set_test(self, d):
        self._test['features'] = np.array([]) if len(d['features']) == 0 else d['features']
        self._test['targets'] = np.array([]) if len(d['targets']) == 0 else d['targets']

    def train_model(self):
        self._model.fit(self._data['features'], self._data['targets'])
