import random
k=random.randint(1,50)
print("=================================")
print("   This is num guessing Game     ")
print("=================================")
x=1
v=False
while x<=5 :
  z=int(input("Guess number between(1,50)"))
  if z==k :
    print("Congratulation You have guessed The number")
    v=True
    break
  elif z>k:
    print("Think Lower ")
  elif z<k:
    print("Think Higher")
if v==False :
  print(f"The Number Was {k}")
    
    
