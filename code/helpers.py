import pandas as pd

from code.constants import (AISLES_FNAME, 
                            DEPARTMENTS_FNAME, 
                            ORDERS_FNAME, 
                            ORDER_PRODUCTS_PRIOR_FNAME, 
                            ORDER_PRODUCTS_TRAIN_FNAME, 
                            PRODUCTS_FNAME, 
                            SAMPLE_SUBMISSION_FNAME)

_FILES = {
    'aisles': AISLES_FNAME, 
    'departments': DEPARTMENTS_FNAME, 
    'orders_meta': ORDERS_FNAME, 
    'orders_prior': ORDER_PRODUCTS_PRIOR_FNAME, 
    'orders_train': ORDER_PRODUCTS_TRAIN_FNAME, 
    'products': PRODUCTS_FNAME, 
    'samples_submission': SAMPLE_SUBMISSION_FNAME
}


def load_top_n(n=5):
    return {
        key: pd.read_csv(fname, nrows=n) for key, fname in _FILES.items()
    }
