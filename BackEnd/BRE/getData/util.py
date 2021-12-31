import json
import pickle
import numpy as np

locations = None
Model = None
DataCollections = None

def getLocationNames():
    global locations
    global DataCollections
    with open("../../Model/columns.json",'r') as f:
    #with open("Model/columns.json",'r') as f:
        DataCollections = json.load(f)['data_columns']
        locations = DataCollections[3:]
        
    return locations

def getPredictions(loc,sqft,bhk,bath):
    global Model
    with open("../../Model/Bengaluru_Real_Estate.pickle",'rb') as f:
        Model = pickle.load(f)
    getLocationNames()
    #prediction begins here
    try:
        loc_index = DataCollections.index(loc.lower())
    except:
        loc_index=-1

    x = np.zeros(len(DataCollections))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if(loc_index>=0):
        x[loc_index] = 1

    return round(Model.predict([x])[0],2)


if __name__ == '__main__':
    print(getPredictions('1st Phase JP Nagar',1000,3,3))