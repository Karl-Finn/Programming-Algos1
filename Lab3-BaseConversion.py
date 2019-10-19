# A program to convert from an decimal integer to an alternate base or vice versa
# NB: either the 'from' base or the 'to' base must be decimal
# Assumes valid input from the user

holding_str = "0123456789ABCDEF"

from_base = int(input("Enter the base (2-16) you are converting from: "))
if from_base == 10:
    to_base = int(input("\nEnter the base you would like to convert to: "))
    usr_input = input("\nEnter the integer you want to convert: ")
    usr_num = int(usr_input)
    converted_num = ""
    while usr_num != 0:
        remainder = usr_num % to_base
        converted_num = holding_str[remainder] + converted_num
        usr_num //= to_base
    print("\n{0} in decimal is {1} in base{2}".format(usr_input, converted_num, to_base))
else:
    usr_input = input("\nEnter the base{} number to convert to decimal: ".format(from_base))
    usr_input = usr_input.upper()
    integer = 0
    exponent = len(usr_input) - 1
    for i in usr_input:
        integer += holding_str.find(i) * (int(from_base) ** exponent)
        exponent -= 1
    print("\n{0} in base{1} is {2} in decimal".format(usr_input, from_base, integer))
