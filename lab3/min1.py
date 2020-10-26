num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))

if num1 < num2:
  minNumber = num1
else:
  minNumber = num2
    
if minNumber < num3:
  print(num1)
else:
  print(num3)
  