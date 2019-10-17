# INTEGER TO HEXADECIMAL

holding_string = "0123456789ABCDEF"

testA = 1
while testA:
    try:
        usr_input1 = input("Enter an integer to convert to hexadecimal: ")
        usr_int = int(usr_input1)
        testA = 0
    except ValueError:
        print(f"{usr_input1} is not a valid integer. Please try again.")

if usr_int == 0:
    print(f"Decimal: {usr_input1}\nHexadecimal: 0\n\n")
else:
    hex_str = ""
    while usr_int != 0:
        remainder = usr_int % 16  # each remainder will correspond to its position in the holding_string
        hex_str = holding_string[remainder] + hex_str
        usr_int //= 16
    print(f"Decimal: {usr_input1}\nHexadecimal: {hex_str}\n\n")

# HEXADECIMAL TO INT
# Assumes valid input is entered
usr_input2 = input("Enter a whole hexadecimal number: ")
usr_hex = usr_input2.upper()
exponent = len(usr_hex) - 1
integer = 0
for i in usr_hex:
    integer += int(holding_string.index(i)) * 16**exponent
    exponent -= 1
print(f"Hexadecimal: {usr_input2}\nDecimal: {integer}\n")