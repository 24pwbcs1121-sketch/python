units=int(input("Enter Number of Units Consumed : "))
if( units<=100):
    bill =units*20
elif(units>100 and units<=200):
    bill = units*30
elif(units >200 and units<=500):
    bill = units*35
else:
    bill=units*40

    bill+=150

if (bill>5000):
    surcharge=bill*0.05
    bill+=surcharge
else:
    surcharge=0

    print("\n----- Electricity Bill -----")
print(f"Units Consumed: {units}")
print(f"Surcharge Applied: Rs. {surcharge:.2f}")
print(f"Total Bill: Rs. {bill:.2f}")