month_salary = int(input("Enter your Monthly Salary:$"))
utilities_bill = int(input('Utilities bill:$'))
monthly_groc = int(input('Monthly groceries:$'))
shops = int(input('Shopping:$'))
ccbill = int(input('Credit card bills:$'))
car_bills = int(input('Car spending:$'))
insurance = int(input('Insurance:$'))
remaining = month_salary - (utilities_bill + monthly_groc + shops + ccbill + car_bills + insurance)
print("Money left:","$",remaining) 
if remaining < month_salary*0.2 :
    print("Decrease spending for a better future!")
else:
	print("Happy savings!")