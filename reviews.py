import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Import data
reviews = pd.read_csv('reviews.csv')

# Print column names
print(reviews.columns)

# Print data types and info
print(reviews.info())
