unsortedArrayOfItems = [1, 6, 9, 5, 4, 3, 2, 1, 10, 22, 31, 2, 8] # list to find highest value item within

maximum = unsortedArrayOfItems[0] # setup maximum as first value in list for comparing against

for j in range(len(unsortedArrayOfItems)):
  if unsortedArrayOfItems[0] > maximum:
    maximum = unsortedArrayOfItems[0] # if value in list larger than current maximum set that to new maximum
    
print(unsortedArrayOfItems[0]) # checking it works
