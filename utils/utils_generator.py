GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
RESET = "\033[0m"

print(f"{YELLOW_BOLD}LOADING GENERATORS MODULE FROM 'utils_generator.py'{RESET}")



import random
import string
import uuid


def generate_random_string():
    """
    Generate a random string with a UUID and additional random characters.
    The random string will have a fixed length of 10 characters, 
    and will include digits, uppercase and lowercase letters, and special characters.
    
    :return: Randomly generated string with a UUID prefix.
    """
    
    # Fixed parameters for character sets
    length = 10
    use_digits = True
    use_uppercase = True
    use_lowercase = True
    use_special_chars = True

    # Define character sets
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Generate a random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    # Generate a UUID
    unique_id = str(uuid.uuid4())
    
    # Combine UUID and random string
    combined_string = f"{unique_id}_{random_string}"
    
    return combined_string




def generate_otp():
    """
    Generate a random 6-digit OTP that does not start with zero.

    :return: A string representing the randomly generated OTP.
    """
    first_digit = random.choice('123456789')  # First digit cannot be 0
    remaining_digits = ''.join(random.choices('0123456789', k=5))  # Remaining 5 digits can be 0-9
    otp = first_digit + remaining_digits
    return otp


print(f"{GREEN_BOLD}****************************** generator module loaded successfully ******************************{RESET}")
