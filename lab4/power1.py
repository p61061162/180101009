baseNumber = int(input("Please enter an basenumber: "))
powerNumber = int(input("Please enter another powernumber: "))

result = 1
for i in range (1, powerNumber+1):
  result = result*baseNumber
print(result)