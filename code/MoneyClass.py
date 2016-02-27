import sys
class Money:	
	# Initialize
	def __init__(self,month):
		self.month=month
		self.desc=[]
		self.dols=[]
		self.online=0
		self.loans=0
		self.groceries=0
		self.gas=0
		self.food=0
		self.sports=0
		self.misc=0
		self.alcohal=0
		self.insurance=0
		self.checks=0
		self.plotvec=0
		self.numsorted=0
		self.numUNsorted=0
		self.triathlon=0
		self.paychecks=0
	# Sort the description into type of spending		
	def  sort_charges(self,chargetypes): 
		idx=0
		sortedcharge=[]   # keep track of which charges have been sorted				
		for charge in self.desc: # self.desc is a Mx1 vector where M is the number of charges, charge represents the counter and also the variable
				sortedflag=0
				for type in chargetypes.online: # 'type' will attain all values in chargetpes.online	
					if type in charge: 			# for the current value type has attained (a string associated with an online charge tag
						self.online=self.online+self.dols[idx]   # if it is, then add to the running total of online expenditures
						sortedcharge.append(idx)      			# keep the index (i.e. idx=the row number from the csv of this entry)
						sortedflag=1
				for type in chargetypes.loans: 	
					if type in charge:
						self.loans=self.loans+self.dols[idx]
						sortedcharge.append(idx)	
						sortedflag=1
				for type in chargetypes.groceries: 	
					if type in charge:
						self.groceries=self.groceries+self.dols[idx]
						sortedcharge.append(idx)
						sortedflag=1						
				for type in chargetypes.gas: 		
					if type in charge:
						self.gas=self.gas+self.dols[idx]
						sortedcharge.append(idx)	
						sortedflag=1	
				for type in chargetypes.food: 	
					if type in charge:
						self.food=self.food+self.dols[idx]
						sortedcharge.append(idx)
						sortedflag=1	
				for type in chargetypes.triathlon: 	
					if type in charge:
						self.triathlon=self.triathlon+self.dols[idx]
						sortedcharge.append(idx)
						sortedflag=1
				for type in chargetypes.sports: 	
					if type in charge:
						self.sports=self.sports+self.dols[idx]
						sortedcharge.append(idx)
						sortedflag=1
				for type in chargetypes.misc: 	
					if type in charge:
						self.misc=self.misc+self.dols[idx]
						sortedcharge.append(idx)
						sortedflag=1
				for type in chargetypes.alcohal: 	
					if type in charge:
						self.alcohal=self.alcohal+self.dols[idx]
						sortedcharge.append(idx)
						sortedflag=1
				for type in chargetypes.insurance: 		
					if type in charge:
						self.insurance=self.insurance+self.dols[idx]
						sortedcharge.append(idx)
						sortedflag=1		
				for type in chargetypes.checks: 		
					if type in charge:
						self.checks=self.checks+self.dols[idx]
						sortedcharge.append(idx)	
						sortedflag=1	
				for type in chargetypes.paychecks: 		
					if type in charge:
						self.paychecks=self.paychecks+self.dols[idx]
						sortedcharge.append(idx)	
						sortedflag=1
				idx=idx+1												
				if sortedflag==1:
					self.numsorted=self.numsorted+1
				else:				
					print charge
		print sortedcharge	
		self.numUNsorted=len(self.desc)-self.numsorted
		tmp=[self.online,self.loans,self.groceries, self.gas, self.food, self.sports, self.misc, self.alcohal, self.insurance, self.checks]	

		plotvec=[]
		for n in tmp:
			plotvec.append(abs(n))
			
		self.plotvec=plotvec
