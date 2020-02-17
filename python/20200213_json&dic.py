# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:03:34 2020

@author: (Dell) Yang-Bin Fan
"""

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string(single)
print(x)
# the result is a Python object dictionary(double)
print(y)
# a slight difference between single/double quotation
print(type(x))
print(type(y))