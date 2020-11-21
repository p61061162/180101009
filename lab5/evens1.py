numbers1 = int(input("How many numbers? "))

#even1 = 0
sumeven1 = 0
sum1 = 0

for i in range(0,numbers1):
  list1 = int(input("please enter an integer: "))
  if list1 % 2 == 0:
    sumeven1 += 1

percent1 = (sumeven1 / numbers1) * 100
print(percent1 , "%")