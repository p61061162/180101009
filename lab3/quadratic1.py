a = int(input("Please enter a number for a: "))
b = int(input("Please enter a number for b: "))
c = int(input("Please enter a number for c: "))

delta = b*b - 4*a*c
print(delta)

if delta < 0:
  print("There are two real roots")
elif delta == 0:
  print("There are one real root")
else:
  print("There are two complex roots")