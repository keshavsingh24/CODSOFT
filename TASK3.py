import random
import string

def generate_password():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired password length (minimum 4): "))
        
        # Validate length
        if length < 4:
            return "Error: Password length must be at least 4 characters"
        
        # Define possible characters for the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        return f"Your generated password is: {password}"
        
    except ValueError:
        return "Error: Please enter a valid number"

# Run the generator
print(generate_password())