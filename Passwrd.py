import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password += random.choice(characters)
    return password

if __name__ == '__main__':
    length = int(input("Enter length of password: "))
    password = generate_password(length)
    print("Generated password: ", password)
