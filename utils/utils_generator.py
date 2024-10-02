

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
    Generate a random 6-digit OTP.

    :return: A string representing the randomly generated OTP.
    """
    otp = ''.join(random.choices('0123456789', k=6))
    return otp

