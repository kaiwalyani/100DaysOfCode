print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is their name?") # What is their name?
com_name = name1 + name2
cname = com_name.lower()
t = cname.count("t")
r = cname.count("r")
u = cname.count("u")
e = cname.count("e")
fsttot = t+r+u+e
l = cname.count("l")
o = cname.count("o")
v = cname.count("v")
e = cname.count("e")
sctot = l+o+v+e
score1 = str(fsttot) + str(sctot)
score = int(score1)
if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
