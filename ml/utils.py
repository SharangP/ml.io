import numpy as np

#TODO error check
def parse_data(data):
  parsed = {}

  parsed['features'] = np.array(data['features'])
  parsed['targets'] = np.array(data['targets'])

  return parsed
