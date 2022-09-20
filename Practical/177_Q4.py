hr = int(input("Enter hour between 1-12 : "))
hr_ahead = int(input("How many hours ahead : "))

time = hr + hr_ahead
if time > 12:
    time-= 12

print("Time at that time would be : ",time,"O'clock")