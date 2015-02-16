import csv 
import numpy as np
import matplotlib.pyplot as plt
from MoneyClass import Money
from ChargeDefinitions import ChargeType

# Initialize Variables
month='January'
Period=Money(month)
Charges=ChargeType()
  
# Read in the values
with open('Checking_Jan15.CSV', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
	Period.desc.append(row['Description'])
	Period.dols.append(float(row['Amount']))
	
# Sort and Identify any outliers
Period.sort_charges(Charges)

str=['Online','Loans','Groceries','Gas','Food','Sports','Misc','Alcohal','Insurance','Checks']

# Plot the results
plt.bar(range(len(Period.plotvec)), Period.plotvec, align='center')
plt.xticks(range(len(str)), str, size='small')
plt.show()

