prev_balance = float (raw_input ("Enter outstanding balance: "))
annual_interest = float (raw_input("Enter annual interest: "))
mmp = 120
months = 1
balance = mmp 

while months < 12:
	#mmp = monthly min. payment
	monthly_interest_rate = annual_interest/100/12.0
	prev_balance = prev_balance * (1 + monthly_interest_rate) - mmp
	months +=1

print "RESULT"
print "Number of months needed:" , months
print "mmp:" , mmp
print "balance: ",round(prev_balance, 1) 