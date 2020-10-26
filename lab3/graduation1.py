gpa = float(input("Please enter your GPA: "))
lecture = int(input("Please enter your Lecture: "))

if lecture < 47 and gpa < 2.0:
  print("Not enough number of lectures and GPA!")
if lecture < 47 and gpa >= 2.0:
  print("Not enough number of lectures!")
if lecture >= 47 and gpa < 2.0:
  print("Not enough GPA!")  
else:
  print("GRADUATED!!!")
  