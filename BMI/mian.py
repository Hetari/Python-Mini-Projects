hight = float(input("Enter you hight in meters: "))
width = float(input("Enter you width in kilograms: "))

bmi = width / hight ** 2

print(round(bmi, 2))

if (bmi <= 18.5):
    print("underweight")
elif (bmi > 18.5 and bmi <= 25):
    print("normal weight")
elif (bmi > 25 and bmi <= 30):
    print("over weight")
elif (bmi > 30 and bmi <= 33):
    print("obese")
else:
    print("over obese")
