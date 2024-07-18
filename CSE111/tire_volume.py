#we import Math because with this we will have the number "pi" more specific
import math
from datetime import datetime
#the date time, become from datetime, because we are meaning that comes from the library datetime, the function datetime.
widthwire = int(input("Enter the width of the tire in mm (example: 205): "))
ratiowire = int(input("Enter the aspect ratio of the tire (example: 60): "))
diameterwire = int(input("Enter the diameter of the wheel in inches (example: 15): "))
formulawire = (widthwire * ratiowire + 2540 * diameterwire) * widthwire**2 * ratiowire
formulawire2 = (formulawire * math.pi) / 10000000000
#I divided the formula in two parts because in this way was more easy to me.

print (f"The approximate volume is {formulawire2:.2f} liters")

#here starts the first part of the extra part where the customer can have the price of the wheel based on the spects entered.
if widthwire == 175 and ratiowire == 70 and diameterwire == 13:
    print("The price of this wheel is: $ 40.00")
elif widthwire == 195 and ratiowire == 65 and diameterwire == 15:
    print("The price of this wheel is: $ 50.00")
elif widthwire == 205 and ratiowire == 70 and diameterwire == 15:
    print("The prices of the wheel is: $65.00")
else:
    print("Sorry, We don´t have the price of that type of wheel")

#here start the part that is extra in case that if the people wants to purchase the wheel give us their contact to call them back.
personal_info = input("Do you want to purchase a wheel with the spects that you entered? ")
personal_info = personal_info.lower()
#it was added the lower module so the program take the information right.

date = datetime.now(tz=None)

with open("volumes.txt", mode="at") as data_file:
    if personal_info == "yes":
        name = input("Please enter your name: ")
        phone = input("Please enter your phone number: ")
        print(f"{date:%y-%m-%d}, Name: {name}, Phone: {phone}", file=data_file)
    print(f"{widthwire}, {ratiowire}, {diameterwire}, {formulawire2:.2f}", file=data_file)
        