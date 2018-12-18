m = int(input("Input your height (cm) "))/100
n = int(input("Input your weight (kg) "))

bmi = n / (m**2)
print ("Your BMI is ", bmi)
print ("Hey, You are", end =" ")
if bmi < 16:
    print ("severely underweight")
elif bmi < 18.5:
    print ("underweight")
elif bmi < 25:
    print ("normal")
elif bmi < 30:
    print ("overweight")
else:
    print ("obese")

