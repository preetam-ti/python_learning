weight = int(input("Enter weight "))
conv_type = input("K for kg or L for Lbs ")

if conv_type.upper() == "K":
    converted = weight / 0.45
    print("weight is "+str(converted)+" Lbs")

if conv_type.upper() == "L":
    converted = weight*0.45
    print("weight is "+ str(converted) +" Kgs")
