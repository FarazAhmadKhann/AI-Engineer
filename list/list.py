list=['apple','banana','watermelon','dates']
print(list)
print(type(list))
if "mango" not in list:
 print("not found")
if "apple" in list:
 print(" yes found")
 print(list[-3:-1])


 # change list items
 thislist=['apple','banana','watermelon','dates']
 thislist[0:1]=["cherry","orange"]
 print(thislist)
 thislist[1:3]=["strawberry"]
print(thislist)
thislist.insert(1,"dryfruit")
print(thislist)
