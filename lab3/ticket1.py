normalTicket = 3
age = int(input("Please enter your age: "))

if age < 6 or age > 60:
  ticket = 0
  print("Bus ticket Free!")
elif 6 < age and age < 18:
  ticket = normalTicket / 2
  print(ticket)
else:
  ticket = normalTicket
  print(ticket)
