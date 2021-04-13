#Brings in the pickled model

import pickle
from test_data import test_data

def load_run_model(test_data):
    with open('model.pkl', 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        pipe = pickle.load(f)
        predictions = pipe.predict_proba(test_data)
        return predictions

print(load_run_model(test_data))