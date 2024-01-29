# defining and working with hash tables

#use a prime number as arrray length
def hash(key,arrayLen):
    total = 0
    WIERD_PRIME = 31
    for c in key:
      total += ord(c)
    #   print(total)
        
    return (total*WIERD_PRIME) %arrayLen

print(hash("hello",11))
