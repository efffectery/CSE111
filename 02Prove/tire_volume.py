import math
from datetime import datetime

date = datetime.now()

width = int(input("Enter the width of the tire in milimeters: "))
aspect_ratio = int(input("Enter the Aspect ratio of the tire: "))
diameter_in_inches = int(input("Enter the Diameter in inches of the wheel: "))

volume_of_tire = round(math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter_in_inches) / 10_000_000_000, 2)

answer = input(f"The volume of the tire is {volume_of_tire} would you like to purchese a tire with the current dimentions? (yes/no) ")

phone_num = "not provided"

if answer == "yes":
    phone_num = input("what is your phone number for us to contact you? ")
    print("thanks we will contact you shortly!")
else:
    print("feel free to run this program again!")


with open("volumes.txt", mode="at") as f:
    print(f"Current Date {date}", file=f)
    print(f"width of tire in mm {width}", file=f)
    print(f"aspect_ratio {aspect_ratio}", file=f)
    print(f"diameter in inches {diameter_in_inches}", file=f)
    print(f"The approximate volume of the tire is {volume_of_tire} liters", file=f)
    print(f"Coustemers phone number is {phone_num}", file=f)


