fibonacci_number = int(input("Plese enter how many Fibonacci numbers to generate: "))

terms = 0 
term1 = 0
term2 = 1
while(terms <= fibonacci_number): 
  term_n = term1 + term2
  terms += 1
  term1 = term2
  term2 = term_n
  print(term_n)
  