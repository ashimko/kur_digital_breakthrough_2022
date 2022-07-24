import os

# PATHS
HOME_PATH = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(HOME_PATH, 'data')
ORIG_DATA_PATH = os.path.join(DATA_PATH, 'original')
ORIG_TRAIN_PATH = os.path.join(ORIG_DATA_PATH, 'train_dataset_train.csv')
ORIG_TEST_PATH = os.path.join(ORIG_DATA_PATH, 'test_dataset_test.csv')
SAMPLE_SUBMIT_PATH = os.path.join(ORIG_DATA_PATH, 'sample_solution.csv')
PREPROCESSED_DATA_PATH = os.path.join(DATA_PATH, 'preprocessed')

SUBMISSION_PATH = os.path.join(HOME_PATH, 'submissions')
OOF_PRED_PATH = os.path.join(HOME_PATH, 'oof_pred')
TEST_PRED_PATH = os.path.join(HOME_PATH, 'test_pred')
MODELS_PATH = os.path.join(HOME_PATH, 'checkpoints')

RANDOM_STATE= 1818
N_SPLITS = 3


TARGET = 'Категория'
THEME_COL = 'Тематика'
TEXT_COL = 'Текст Сообщения'
ID_COL = 'id'
CAT_COLS = [THEME_COL, 'Ответственное лицо']
TEXT_COLS = [TEXT_COL]