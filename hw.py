import random
import string

def generate_simple_password(length=10):

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    password = ''.join(random.choice(characters) for i in range(length))
    
    return password
if __name__ == "__main__":

    new_password = generate_simple_password()
    print(f"Generated Password: {new_password}")

