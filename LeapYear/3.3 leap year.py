# https://www.youtube.com/watch?v=xX96xng7sAE

year = int(input("Which year that you want to check: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
