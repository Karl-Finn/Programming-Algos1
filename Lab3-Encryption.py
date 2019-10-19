# Program to encrypt or decrypt a string
# Assumes valid input from the user

usr_string = input("Enter your string: ")
key = int(input("\nPress 1 to Encrypt or 2 to Decrypt: "))

if key == 1:
    reversed_string = usr_string[::-1]
    encrypted_str = ""
    for i in reversed_string:
        encrypted_str += chr(ord(i) + 1)
# NB: encrypted_str = chr(ord(i) + 1) + encrypted_str (would have done the reversing and ordinal change in one line)
# See: the Else clause for this example in decryption
    print("\nOriginal: {0}\nEncrypted: {1}".format(usr_string, encrypted_str))
else:
    decrypted_str = ""
    for i in usr_string:
        decrypted_str = chr(ord(i) - 1) + decrypted_str
    print("\nEncrypted: {0}\nDecrypted: {1}".format(usr_string, decrypted_str))
