import pandas as pd
import numpy as np
from sklearn.metrics import log_loss

df = pd.read_csv('train.csv')
print df
log_loss(actual_labels,  [[1, 0, 0], [0, 1, 0], [0, 0, 1]])