#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:20:00 2022

@author: harshalbhoir
"""

import sys

#train_file = pd.read_csv()
#test_file = pd.read_csv(sys.argv[2])
    
import csv
import re
import pandas as pd
dataset = pd.read_csv( "SBD.train" , delimiter="\s", header=None )
train = dataset.iloc[ : , 1:2 ].values

# Feature extraction # Feature extraction # Feature extraction # Feature extraction # Feature extraction # Feature extraction 
with open('Features.csv', 'w', newline='') as f:
    save = csv.writer(f)
for i in range(0, (len(train)-5)):
    if "." in str(train[i]) :
        
        
        L = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i]))
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i-1]))
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i-2]))
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i-3]))  
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i-4]))    
        
        
        R = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i+1]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i+2]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i+3]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i+4]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(train[i+5]))    
        
                  
       #length of Left word 
        if len(str(L)) < 3:
            L_len = 0
        else:
            L_len = 1
        
        #Check for First charater of L
        ring = L[0]
        if ring.isupper():
            Lfc = 1
        else:
            Lfc = 0
        
        #Check for First charater of R
        ring = R[0] 
        if ring.isupper():
            Rfc = 1
        else:
            Rfc = 0
            
        if L.isnumeric() :
            L_number = 1
        else:
            L_number = 0
            
        
        if L.isnumeric() and R.isnumeric():
            its_number = 1
        else:
            its_number = 0
            
        if L =="Mr" or L=="Dr":
            abr = 1
        else:
            abr = 0
            
        result = dataset.iloc[ i:i+1 , 2:3 ].values
       
        
        # list of column names 
        Feature_names = ['isnum','Abbr','L_number','Result']
  
        
        dict = {"isnum": its_number, "Abbr": abr, "L_number":L_number, "Result": result}

        with open('Features.csv', 'a') as f:
            dict_object = csv.DictWriter(f, fieldnames=Feature_names) 
            dict_object.writerow(dict)
            
#######################################################

testdata = pd.read_csv( "SBD.test" , delimiter="\s", header=None )
test = testdata.iloc[ : , 1:2 ].values

# Feature extraction 
with open('TESTFeatures.csv', 'w', newline='') as tf:
    save = csv.writer(tf)
for i in range(0, len(test)-5):
    if "." in str(test[i]) :
        
        
        L = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i]))
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i-1]))
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i-2]))
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i-3]))  
        if len(str(L)) == 0:
            L = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i-4]))    
        
        
        R = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i+1]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i+2]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i+3]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i+4]))
        if len(str(R)) == 0:
            R = re.sub("[^a-zA-Z0-9 ]" , '',str(test[i+5]))    
        
                  
       #length of Left word 
        if len(str(L)) < 3:
            L_len = 0
        else:
            L_len = 1
        
        #Check for First charater of L
        ring = L[0]
        if ring.isupper():
            Lfc = 1
        else:
            Lfc = 0
        
        #Check for First charater of R
        ring = R[0] 
        if ring.isupper():
            Rfc = 1
        else:
            Rfc = 0
            
        if L.isnumeric() :
            L_number = 1
        else:
            L_number = 0
            
        
        if L.isnumeric() and R.isnumeric():
            its_number = 1
        else:
            its_number = 0
            
        if L =="Mr" or L=="Dr":
            abr = 1
        else:
            abr = 0    
            
            
            
            
        result = testdata.iloc[ i:i+1 , 2:3 ].values
       
        
        # list of column names 
        Feature_names = ['isnum','Abbr','L_number','Result']
  
        
        dict = {"isnum": its_number, "Abbr": abr, "L_number":L_number, "Result": result}

        with open('TESTFeatures.csv', 'a') as tf:
            dict_object = csv.DictWriter(tf, fieldnames=Feature_names) 
            dict_object.writerow(dict)       
# Feature extraction # Feature extraction # Feature extraction # Feature extraction # Feature extraction # Feature extraction         
       
     
 ################ ################  ################  ################  ################  ################   
        
        
# Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction        
data = pd.read_csv("Features.csv", header=None) 
X = data.iloc[:, 0:3 ]#.values
Y = data.iloc[:, 3:4]#.values

data = pd.read_csv("TESTFeatures.csv", header=None) 
pX = data.iloc[:, 0:3 ]#.values
gold_Y = data.iloc[:, 3:4]#.values



# Handling Catagorical data
x1 = X[0].to_list()
for i in range(0, len(x1)):
    x1[i] = hash(str(x1[i]))
    
x2 = X[1].to_list()
for i in range(0, len(x2)):
    x2[i] = hash(str(x2[i]))
    
X[0] , X[1] = x1 , x2   


px1 = pX[0].to_list()
for i in range(0, len(px1)):
    px1[i] = hash(str(px1[i]))
    
px2 = pX[1].to_list()
for i in range(0, len(px2)):
    px2[i] = hash(str(px2[i]))
    
pX[0] , pX[1] = px1 , px2  
# Handling Catagorical data




#Decission Tree classification algo
from sklearn.tree import DecisionTreeClassifier
dt  = DecisionTreeClassifier()
dt.fit(X,Y)

predictedY = dt.predict( pX )
# Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction # Prediction 

data[9] = predictedY



for row in range(len(data[[0,3,9]])):
    op_dict = data.loc[row,[0,3,9]].to_dict()
    with open('SBD.test.out','a') as pf:
        dict_object = csv.DictWriter(pf, fieldnames=[0,3,9]) 
        dict_object.writerow(op_dict)


# Accuracy # Accuracy # Accuracy # Accuracy # Accuracy # Accuracy # Accuracy 
from sklearn.metrics import balanced_accuracy_score
y_true = (gold_Y)
y_pred = (predictedY)
New_Accuracy = balanced_accuracy_score(y_true, y_pred)
print("Accuracy is:", (New_Accuracy*100))
# Accuracy # Accuracy # Accuracy # Accuracy # Accuracy # Accuracy # Accuracy 


  
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
