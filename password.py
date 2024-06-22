import random
import string

def generate_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        raise ValueError("Complexity should be one of 'low', 'medium', or 'high'")
    
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    print("---------------------------------")
    
    try:
        length = int(input("Enter the length of the password: "))
        
        if length <= 0:
            print("Password length should be greater than zero.")
            return
        
        complexity = input("Enter the complexity level (low, medium, high): ").lower()
        password = generate_password(length, complexity)
        
        print(f"Generated password: {password}")
        
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
