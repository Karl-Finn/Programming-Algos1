# INT TO BINARY
testA = 1
while testA:
    try:
        usr_input = input("Enter an integer to convert to binary: ")
        usr_int = int(usr_input)
        testA = 0
    except ValueError:
        print(f"{usr_input} is not a valid integer. Please try again.")

if usr_int == 0:
    print(f"Decimal: {usr_input}\nBinary: 0\n\n")
else:
    binary_str = ""
    while usr_int != 0:
        remainder = usr_int % 2
        binary_str = str(remainder) + binary_str
        usr_int //= 2
    print(f"Decimal: {usr_input}\nBinary: {binary_str}\n\n")

# BINARY TO INT
testB = 1
while testB:
    try:
        usr_input = input("Enter a whole-number-binary to convert to integer: ")
        usr_binary = int(usr_input)
        testB = 0
    except ValueError:
        print(f"{usr_input} is not a valid whole-number-binary. Please try again.")

# Gets the length of the usr_input string and subtracts 1 from it. This will be the starting exponent for base 2
# Going from left to right of usr_input the loop will then multiply each element of usr_input by 2 raised to the
# exponent
decimal = 0
exponent = len(usr_input) - 1
for i in usr_input:
    decimal += int(i) * 2**exponent
    exponent -= 1
print(f"Binary: {usr_input}\nDecimal: {decimal}")