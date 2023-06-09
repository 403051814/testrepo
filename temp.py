# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import scipy.stats as stats
import scipy as scy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv('labels.csv')
common_keys = set(data.columns) & set(labels.columns)
data_w_labels = pd.merge(data, labels, on='Unnamed: 0')
corr= data_w_labels.corr()
sns.heatmap(corr,annot=True)