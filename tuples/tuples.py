thistuple=("orange","watermelon","apple")
print(thistuple[-1::-1])
thislist=list(thistuple)         #change tuple in list then make operation on list and covert into tuples
print(thislist)
thislist[0:1]=["guava","grapes"]
print(thislist)
del thislist[-1]
print(thislist)
thistuple=tuple(thislist)            #convertedback
print(thistuple)
del thistuple
thistuple=("orange","watermelon","apple")          #adding atuple ito another tuple
thistuple2=("guava","grapes")
thistuple+=thistuple2
print(thistuple)

(orange,*red,green)=thistuple                    #assigning  tuples to variables
print(orange)
print(red)
print(green)

thistuple=thistuple*2
print(thistuple)

print(thistuple.count("orange"))
print(thistuple.index("watermelon",3))           #value,start,stop

