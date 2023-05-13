#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 00:11:51 2023

@author: gabriel
"""


import joblib
import pandas as pd
import os

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir , 'heart_prediction_machine')

model = joblib.load(file_path)

def predict_heart_disease(data):
    result = model.predict([data])
    if result == 0:
        return(False)
    else:
        return(True)
