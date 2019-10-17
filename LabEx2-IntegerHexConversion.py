# INTEGER TO HEXADECIMAL
testA = 1
while testA:
    try:
        usr_input = input("Enter an integer to convert to hexadecimal: ")
        usr_int = int(usr_input)
        testA = 0
    except ValueError:
        print(f"{usr_input} is not a valid integer. Please try again.")

if usr_int == 0:
    print(f"Decimal: {usr_input}\nHexadecimal: 0\n\n")
else:
    holding_string = "0123456789ABCDEF"
    hex_str = ""
    while usr_int != 0:
        remainder = usr_int % 16 # each remainder will correspond to its position in the holding_string
        hex_str = holding_string[remainder] + hex_str
        usr_int //= 16
    print(f"Decimal: {usr_input}\nHexadecimal: {hex_str}\n\n")

# HEXIDECIMAL TO INT

5f9a