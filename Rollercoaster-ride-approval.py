print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = input("What is your age?")
  if int(age) < 12:
    print("Please pay $5.")
  elif int(age) <=18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("So sorry, you have to grow taller before you can ride.")
