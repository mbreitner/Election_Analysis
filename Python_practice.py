print("Hello World")
## math Equations
5+2*3
8//5-3
8+22*2-4
16-3/2+7-1
3**3%5
5+9*3/2-4

(5+2)*3
(8//5)-3
8+(22*(2-4))
16-3/(2+7)-1
3**(3%5)
5+(9*3/2-4)
5+(9*3/(2-4))

##Lists
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
print(counties[2])
print(counties[-1])
print(len(counties))
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
counties.append("El Paso")
print(counties)
counties.insert(2,"El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
counties.remove("El Paso")
counties.append("Jefferson")
counties[2] = "El Paso"
counties[2] = "Jefferson"
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties.insert(2, "Denver")
counties.remove("Denver")
counties.insert(3,"Denver")
counties.remove("Denver")
counties.append("Arapahoe")
print(counties)


##tuples
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
