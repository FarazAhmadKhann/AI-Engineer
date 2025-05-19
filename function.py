x="faraz"
def global_variables():
 global x
 print("i am",x)
 
 x = "badar"
 global y
 y="dani"
 print("i am",x)
global_variables()
print("i am",y)
print("i am",x)
