
def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mul(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

operations = { "+" : add, "-" : sub, "*" : mul, "/" : div}

def calculator():
  n1 = float(input("Enter First Number : "))
  for symbol in operations:
    print(symbol)
  continue1 = True
    
  while continue1 :
    todo = input("Pick the operation you want to perform : ")
    n2 = float(input("Enter Next number : "))
    function = operations[todo]
    answer1 = function(n1,n2)
    print(f"Answer is : {n1} {todo} {n2} = {answer1}")
  
    conti = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to start again and 'e' to exit : ")
    if conti == "y":
      n1 = answer1
    elif conti == 'n':
      continue1 = False
      calculator()
    else:
      continue1 = False
      print("Thank You!")

calculator()
