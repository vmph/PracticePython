# -*- coding: utf-8 -*-
"""
Created on Wed Aug 06 15:20:14 2014

@author: Valerie
"""

dataPath = "C:/Users/Anthony/My Documents/Kaggle/"
outPath = "C:/Users/Anthony/My Documents/Kaggle/"

import pandas as pd

def loadData(datafile):
    return pd.read_csv(datafile)

def createWildernessArea(data):

    for i in range(4):
        coded = {'1': i+1, '0': 0}
        col = 'Wilderness_Area' + str(i+1)
        data[col] = data[col].astype(str).map(coded)

    data['Wilderness_Area'] = data['Wilderness_Area1'] + \
                              data['Wilderness_Area2'] + \
                              data['Wilderness_Area3'] + \
                              data['Wilderness_Area4']
 
    for i in range(4):
        col = 'Wilderness_Area' + str(i+1)
        data = data.drop(col, 1)

    return data

def createSoilType(data):

    for i in range(40):
        coded = {'1': i+1, '0': 0}
        col = 'Soil_Type' + str(i+1)
        data[col] = data[col].astype(str).map(coded)    

    data['Soil_Type'] = 0
    for i in range(40):
        col = 'Soil_Type' + str(i+1)
        data['Soil_Type'] += data[col] 
 
    for i in range(40):
        col = 'Soil_Type' + str(i+1)
        data = data.drop(col, 1)

    return data



def main():
    train = loadData(dataPath + "trainval.csv")
    test = loadData(dataPath + "testval.csv")
    
    train = createWildernessArea(train)
    train = createSoilType(train)
    train.to_csv(outPath + "trainval.csv")

    test = createWildernessArea(test)
    test = createSoilType(test)
    test.to_csv(outPath + "testval.csv")


if __name__ == '__main__':
    main()
 
