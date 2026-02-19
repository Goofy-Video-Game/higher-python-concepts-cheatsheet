def readFile():
    
    #opens file, grabs all the lines, closes
    file = open("filename.text", "r")
    filelines = file.readlines()
    file.close()
    
    #initializes all x csv value arrays in order
    value1 = ["variable type here"] * len(filelines)
    value2 = ["variable type here"] * len(filelines)
    value3 = ["variable type here"] * len(filelines)
    value4 = ["variable type here"] * len(filelines)
    value5 = ["variable type here"] * len(filelines)
    value6 = ["variable type here"] * len(filelines) 
    #have as many or as few as needed
    
    #unpacks csv file for each line putting each value in corresponding array returns all arrays
    for j in range(len(filelines)):
        parts = filelines[j].split(",")
        value1[j], value2[j], value3[j] = parts[0], parts[1], parts[2]
        value4[j], value5[j], value6[j] = parts[3], parts[4], parts[5] 
        #repeat for how many needed
        
    return value1, value2, value3, value4, value5, value6
