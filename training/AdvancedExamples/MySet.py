#Create set
items = {"arrow", "spear", "arrow", "arrow", "rock"}

#print set
print(items)

#search for rocks
if "rock" in items:
    print("we got rocks")

#Create an empty set
items = set()

#add items
items.add("cat")
items.add("dog")
items.add("fish")

print (items)

numbers1 = {1, 3, 5, 7}
numbers2 = {1, 3}

if numbers2.issubset(numbers1):
    print("is a subset")

if numbers1.issuperset(numbers2):
    print("is a superset")

print(numbers1.intersection(numbers2))