import os
import pickle
from typing import Any

def check_path(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def save_model(model: Any, path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(model, f)