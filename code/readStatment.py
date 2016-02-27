# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:14:27 2016

@author: uguiso
"""

import pandas as pd
from ChargeLib import ChargeType
from ChargeDict import Charges
#from InitiateData import InitiateDataFrame


def getClassChargesTypes(Class):
    if 'Gas' in Class:
        classCharges = ['Shell']
    elif 'Loans' in Class:
        classCharges = ['NelNet','Payment']
    elif 'Food' in Class:
        classCharges = ['FlatBreads','DUNKIN']
    elif 'Bills' in Class:
        classCharges = ['COMCAST','VERIZON']
    return classCharges    



def sortCharges(chargeDescriptions):
    Classes=['Gas',['Loans'],['Food']]
    for description in chargeDescriptions: # loop over all descriptions in csv
       for Class in Classes:                # loop over all charge classes until match         
            classCharges=getClassChargesTypes(Class)
            for charge in classCharges:  # loop over all charges in a class                  
                if charge in description:
                    print 'Found: ',charge;'\n','in:',description
                                     
# Import charge class, a library of sounds
#Charges=ChargeType() # initiate class ChargeType                                     
                                    
# Statment Filename
filename='../Statements/Freedom/Freedom_2105.CSV'

# Read Statment CSV
df = pd.read_csv(filename)

# Get keywords associated with each chargetype
chargeFrame=Charges()

# Sort the charges in each row 
df['chargeID']=sortCharges(df.Description)
    # call a function that returns the class ID, aka what type of charge it is
    # create a new field in the dataframe with the class ID
