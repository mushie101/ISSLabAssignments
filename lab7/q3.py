
def UniqueSort (x):
    ar = x.split(", ")
    ar = set(ar)
    ar = list(ar)
    ar.sort()
    print(ar)
    
UniqueSort("red, white, black, green, black, red")

