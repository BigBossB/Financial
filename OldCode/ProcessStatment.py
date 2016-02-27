import csv 
import pdb
import numpy as np
import matplotlib.pyplot as plt
from MoneyClass import Money
from ChargeLib import ChargeType
from pprint import pprint



# Initialize Variables
statementname='January'
Period=Money(statementname) # inititate class 'Money'
Charges=ChargeType() # initiate class ChargeType
  
# Read in the values
with open('../Statements/Freedom/Freedom_2105.CSV', 'rb') as csvfile: # open the csv
    reader = csv.DictReader(csvfile)  # read the file in
    for row in reader:  # iterate over the rows, an enitre row is contained in row, i.e. row stores the row and is also the counter in the for loop
				 # reader is the handle on the read in file, contains the field name (think of as the first row column headers)
	Period.desc.append(row['Description']) # populate the field Description of object Period which is a Money class object
								       # so every iteration on the for loop updates 'row'. 'Decription' and 'Amount' are fields in 'row'
								       # the field 'Description' is a string value from the csv
	Period.dols.append(float(row['Amount'])) # the field 'Amount' in the dollar amout from the csv 

# Sort and Identify any outliers

Period.sort_charges(Charges)

# Plot the results
str=['Online','Loans','Groceries','Gas','Food','Sports','Misc','Alcohal','Insurance','Checks']
print'Statement Filename:',statementname
print'Number of Charges Sorted:',Period.numsorted
print'Number of Charges UN-Sorted:',Period.numUNsorted
#plt.bar(range(len(Period.plotvec)), Period.plotvec, align='center')
#plt.xticks(range(len(str)), str, size='small')
#plt.show()
#plt.close()



	
