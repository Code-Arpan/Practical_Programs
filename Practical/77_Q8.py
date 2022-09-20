ht = int(input("Enter your height(in centimetre): "))
#1 foot = 12 inches, 1 inch = 2.54 cm
ht_in_inch = ht / 2.54
feet = ht_in_inch // 12
inch = ht_in_inch % 12
print("Your height is", feet, "feet and", inch, "inches")