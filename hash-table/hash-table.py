# defining and working with hash tables

def hash(key,arrayLen):
    total = 0
    for c in key:
      total += ord(c)
    #   print(total)
        
    return total%arrayLen

print(hash("hello",11))
