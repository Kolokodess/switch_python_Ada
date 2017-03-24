prev_balance = float (raw_input ("Enter outstanding balance: "))
annual_interest = float (raw_input("Enter annual interest: "))
months = 12


#mplb = monthly payment lower bound, mpub = monthly payment upper bound
mplb = prev_balance / 12.0
mpub = (prev_balance * (1 + (annual_interest/ 12.0)) ** 12.0) / 12.0
mmp = (mplb + mpub) / 2
monthly_interest_rate = (annual_interest/100)/12.0
prev_balance = prev_balance * (1 + monthly_interest_rate) - mmp
# prev_balance -= 


print "RESULT"
print "Monthly payment to pay off debt in 1 year: ", mmp
print "Number of months needed: ", months
print "Balance: ", prev_balance