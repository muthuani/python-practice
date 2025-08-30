# Python Program to read height in centimeters and then convert the height to feet and inches
cm=float(input("Please Enter the height in CM : "))
feet = round(cm * 0.0328,2)
inch =round(cm * 0.3937,2)
print(f"Height in Feet = {feet}")
print(f"Height in Inch = {inch}")
