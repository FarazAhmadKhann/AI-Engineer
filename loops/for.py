a=6
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
           