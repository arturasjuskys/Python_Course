print("How many kilometers did you cycle today?")
km = input()
miles = float (km)/1.60934
#miles = round(float(km)/1.60934, 2)
miles = round(miles, 2)
print(f"Your {km}km ride was {miles}mi")
#print(f"Your {km}km ride was {round(miles, 2)}mi")