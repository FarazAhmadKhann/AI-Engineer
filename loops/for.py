a=1000000
for x in range(a):
  print(x)
  for y in range(6,0,-1):
    if x>a/2:
       x=a-x
    if not y-x<=0:
      print(" ",end="")
    else:
     break
  for z in range(x):
    print("* ",end= "")
  print("")     
           

n = 5  # Should be odd for symmetry
stars = "* "
spaces = " " * (n // 2)

# Top half
for i in range(1, n // 2 + 2):
    print(spaces + stars * i)
    spaces = spaces[:-1]

# Bottom half
spaces = " "  # Reset to one space
for i in range(n // 2, 0, -1):
    print(spaces + stars * i)
    spaces += " "
