# Implementation of whales algorithmm

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('Data.csv')
data.head()

model = DecisionTreeClassifier()
