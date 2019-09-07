thisset={}
print(thisset)
{}

thisset={"apple","banana","cherry"}
print(thisset)
{"apple","banana","cherry"}

thisset={"Ahmmad","Ahmmad",1,2,1,5}
print(thisset)
{1,2,5,"Ahmmad"}

thisset={"apple","banana","cherry"}
for x in thisset:{
print(x)}
banana
cherry
apple

thisset={"apple","banana","cherry"}
print("banana" in thisset)
True

thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)
{"apple","banana","cherry","orange"}

thisset={"apple","banana","cherry"}
thisset.update(["orange","mango","grapes"])
print(thisset)
{"apple","mango","banana","grapes","cherry","orange"}
