unsortedArrayOfItems = [1, 6, 9, 5, 4, 3, 2, 1, 10, 22, 31, 2, 8] # list to find highest value item within

minimum = unsortedArrayOfItems[0] # setup minimum as first value in list for comparing against

for j in range(len(unsortedArrayOfItems)):
  if unsortedArrayOfItems[0] < minimum:
    minimum = unsortedArrayOfItems[0] # if value in list smaller than current minimum set that to new minimum
    
print(minimum) # checking it works
