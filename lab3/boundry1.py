minBoundary = 1
maxBoundary = 100

num = int(input("Please enter a number: "))

if num < minBoundry:
  print("Number is not in range!")

elif minBoundry < num and num < maxBoundry:
  print("Number is in range!")
  