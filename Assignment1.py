balance = float(raw_input ("Enter Balance:"))
Annual_interest = float(raw_input("Enter Annual Interest rate:"))
min_payment_rate = float(raw_input("Enter Minimum payment rate:"))
total_payment = 0
months = 1 


while months <= 12:
	#m_m_p = minimum monthly payment
	m_m_p = min_payment_rate * balance
	monthly_interest = Annual_interest/12.0 * balance
	principal = m_m_p - monthly_interest
	balance = balance - principal
	print "month:", months
	print "m_m_p:", m_m_p
	print "monthly_interest:", monthly_interest
	print "principal:", principal
	print "balance:", balance
	total_payment +=m_m_p
	months +=1

print "Result"
print "total_payment: $",round(total_payment,2) 
print "Remaining balance: $", round(balance,2)
