import random
import string

def GP(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

pass_len = int(input("Enter the length of the password: "))
if pass_len <= 8:
    print("Please enter a valid password length.")
else:
    password = GP(pass_len)
    print(f"Generated password: {password}")
