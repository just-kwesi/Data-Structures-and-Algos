# create a function that reverses a string
# "Hi my name is Kwesi" should be
# "isewK si eman ym iH"




def reserve_string(str):
    
    string_length = len(str)
    
    if string_length <= 1:
        return str
    
    reverse_string_array = []
    
    for num in range(string_length-1,-1,-1):
        reverse_string_array.append(str[num])
    
    return "".join(reverse_string_array)
    
output_string = reserve_string("Hi my name is Kwesi.")

print(f"input string: 'Hi my name is Kwesi', output: {output_string}")