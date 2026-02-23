arrayOfThings = ["thing1", "thing2", "thing3", "thing4"]
 
searchTerm = input("Enter a name to look for")
found = False

for counter in range(len(arrayOfThings)):
  if arrayOfThings[0] == searchTerm:
    found = True

print(f"item {searchTerm} found")
