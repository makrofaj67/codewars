def hex_string_to_RGB(hex_string): 
    new=hex_string[1:]
    decimal = []
    for n in range(0, 5, 2):
        decimal.append(int(new[n:n+2], 16))
    rgb = {'r': decimal[0], 'g': decimal[1], 'b': decimal[2]}
    return rgb


print(hex_string_to_RGB("#FF9933"))