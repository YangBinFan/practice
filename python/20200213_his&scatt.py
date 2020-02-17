# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:37:56 2020

@author: (Dell) Yang-Bin Fan
"""
import numpy as np
import matplotlib.pyplot as plt

set_seed = 123

samples_1 = np.random.RandomState(set_seed).normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.RandomState(set_seed).standard_t(df=10, size=1000)
bins = np.linspace(-3, 3, 100)

plt.subplot(2, 2, 1)
plt.hist(samples_1, bins=bins, alpha=0.5, label='samples 1')
plt.hist(samples_2, bins=bins, alpha=0.5, label='samples 2')
plt.legend(loc='upper left')

plt.subplot(1, 2, 2)
plt.scatter(samples_1, samples_2, alpha=0.2)

plt.savefig('chart.png')
plt.show()