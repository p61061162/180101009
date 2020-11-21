password1 = "abc123"
password2 = input("please enter your password: ") 

while True:
  if password1 == password2:
    print("welcome")
    break
  elif password2 == "help":
    print("a")
    break
  else:
    print("Wrong")
    break
    
        
