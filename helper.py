import os
import pickle
import random
import numpy as np
import tensorflow as tf
from typing import Any

def check_path(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def save_model(model: Any, path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(model, f)


def seed_everything(seed=0):
    def seed_basic(seed=seed):
        random.seed(seed)
        os.environ['PYTHONHASHSEED'] = str(seed)
        np.random.seed(seed)
        
    def seed_tf(seed=seed):
        tf.random.set_seed(seed)
    seed_basic(seed)
    seed_tf(seed)