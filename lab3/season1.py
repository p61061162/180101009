month = int(input("Please enter a number for month between 1 and 12: "))
day = int(input("Please enter a number for day between 1 and 31: "))

elif month >=3 and month <= 5:
  if month == 3 and day < 20:
    print("Winter", "day " + str(day), "month " + str(month))
  elif month == 3 and day >= 20:
    print("Spring", "day " + str(day), "month " + str(month))
  else:    
    print("Spring", "day " + str(day), "month " + str(month))
elif month >=6 and month <= 8:
  if month == 6 and day < 21:
    print("Spring", "day " + str(day), "month " + str(month))
  elif month == 6 and day >= 21:
    print("Summer", "day " + str(day), "month " + str(month))     
  else:    
    print("Summer", "day " + str(day), "month " + str(month))
elif month >=9 and month <= 11:
  if month == 9 and day < 22:
    print("Summer", "day " + str(day), "month " + str(month))
  elif month == 6 and day >= 22:
    print("Fall", "day " + str(day), "month " + str(month))     
  else:    
    print("Fall", "day " + str(day), "month " + str(month))  
elif month >=12 and month <= 2:
  if month == 12 and day < 21:
    print("Fall", "day " + str(day), "month " + str(month))
  elif month == 12 and day >= 21:
    print("Winter", "day " + str(day), "month " + str(month))     
  else:    
    print("Winter", "day " + str(day), "month " + str(month))       