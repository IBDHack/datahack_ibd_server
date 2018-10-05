#!/usr/bin/env python3

import numpy as np

def predict(pickle_load, data, user):
    """
    Predicts using a pickled predictor.
    :param pickle_load: Output of pickle.load on the pickled predictor
    :param data: Data file (all_species.clean.csv)
    :param user: User provided file
    :return: Prediction
    """
    names = np.array(list(filter(lambda name: len(name) > 0, data.split('\n'))))
    vector = np.zeros(np.shape(names))
    
    for line in user.split('\n'):
        for part in line.split():
            if part.startswith('s__'):
                vector[np.where(names == part)] += 1
                break
    
    return pickle_load.predict(np.reshape(vector, (1, -1))).item() 
