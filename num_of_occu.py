ls = [1,2,1,3,2,5,7,4,3,1,4,7,9]

s = set(ls)
ls_un = list(s)
occu = {}

for i in range(len(ls)):
    if ls[i] in occu.keys():
        continue
    else:
        occu[ls[i]] = ls.count(ls[i])

print(occu)

##OR 

occu = {}

for i in range(len(ls)):
    count = 0
    for j in range(len(ls)):
        
        if ls[i] == ls[j]:
            count = count+1
    occu[ls[i]] = count

print(occu)