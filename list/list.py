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

#add list items
# 1- append 2- insert 3- extend
city=["islamabad","karachi","lahore","multan","peshawar"]
province=["Punjab","KPK","Balochistan","Sindh"]
city.append("Rawalpindi")
province.insert(1,"Kashmir")
print(city)
print(province)
city.extend(province[1:3])
print(city)


# 1- remove("islamabad") 2- pop() 3- pop(1) 4- del thelist[2] 5- del thislist 6- thislist.clear()
print("we doing delete now")
del city[1:3]
print(city)
city.pop(0)
print(city)
city.clear()
print(city)
del city


#1- list.sort() 2- list.sort(reverse=true) 3- list.reverse() 4-list.sort(key=func)
print("we do sort now")
number=[1,6,4,88,92,34,54,3,1]
number.sort()
print(number)
number.sort(reverse=True)
print(number)
def func(n):
 return abs(n-60)
number.sort(key=func)
print(number)

