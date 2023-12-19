import random
import string

def generate_password(length):
    spl_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(spl_characters) for _ in range(length))
    return password

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print(f"Generated password is {password}")