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
		
	# Sort the description into type of spending		
	def  sort_charges(self,chargetypes): 
		idx=0
		sortedcharge=[]   # keep track of which charges have been sorted
		
		
		for charge in self.desc: # go through each charge from bank statement
		
			for type in chargetypes.online: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.online=self.online+self.dols[idx]
					sortedcharge.append(idx)
			for type in chargetypes.loans: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.loans=self.loans+self.dols[idx]
					sortedcharge.append(idx)	
			for type in chargetypes.groceries: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.groceries=self.groceries+self.dols[idx]
					sortedcharge.append(idx)						
			for type in chargetypes.gas: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.gas=self.gas+self.dols[idx]
					sortedcharge.append(idx)		
			for type in chargetypes.food: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.food=self.food+self.dols[idx]
					sortedcharge.append(idx)	
			for type in chargetypes.triathlon: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.triathlon=self.triathlon+self.dols[idx]
					sortedcharge.append(idx)
			for type in chargetypes.sports: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.sports=self.sports+self.dols[idx]
					sortedcharge.append(idx)
			for type in chargetypes.misc: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.misc=self.misc+self.dols[idx]
					sortedcharge.append(idx)
			for type in chargetypes.alcohal: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.alcohal=self.alcohal+self.dols[idx]
					sortedcharge.append(idx)
			for type in chargetypes.insurance: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.insurance=self.insurance+self.dols[idx]
					sortedcharge.append(idx)		
			for type in chargetypes.checks: # compare against dictionary of charge types to identify what I bought		
				if type in charge:
					self.checks=self.checks+self.dols[idx]
					sortedcharge.append(idx)						
			idx=idx+1
		tmp=[self.online,self.loans,self.groceries, self.gas, self.food, self.sports, self.misc, self.alcohal, self.insurance, self.checks]	

		plotvec=[]
		for n in tmp:
			plotvec.append(abs(n))
			
		self.plotvec=plotvec
