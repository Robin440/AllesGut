
import random
import string
import re

from utils.emails import email_middleware

# List of valid domains
domain_list = ['gmail.com', 'begur.co.in','navadhiti.com']

# Regular expression for email validation
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

import re

def is_valid_email(email):
    # Check if email is too long (maximum length for email is 254 characters)
    if len(email) > 254:
        return False

    # Regular expression for a basic valid email format
    email_regex = r"^(?!\.)[\w!#$%&'*+/=?^`{|}~.-]+(?<!\.)@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$"

    # Check if email matches the regular expression
    if not re.match(email_regex, email):
        return False

    # Split the email into local part and domain part
    local_part, domain_part = email.split('@')

    # Check if local part exceeds 64 characters
    if len(local_part) > 64:
        return False

    # Check for consecutive dots in local part or domain part
    if '..' in local_part or '..' in domain_part:
        return False

    # Check if domain part contains only valid characters and has a valid format
    domain_regex = r'^[a-zA-Z\d-]+(\.[a-zA-Z\d-]+)*\.[a-zA-Z]{2,}$'
    if not re.match(domain_regex, domain_part):
        return False

    # Check if domain part starts or ends with a hyphen
    if domain_part.startswith('-') or domain_part.endswith('-'):
        return False

    # Check if local part starts or ends with a dot
    if local_part.startswith('.') or local_part.endswith('.'):
        return False

    # Check if domain part has a valid TLD (2-63 characters long)
    tld = domain_part.split('.')[-1]
    if len(tld) < 2 or len(tld) > 63:
        return False

    # Check for any leading or trailing spaces
    if email.strip() != email:
        return False

    return True


def  is_valid_domain(email):
    
    # Check if domain is in the allowed list
    domain = email.split('@')[-1].strip()  # Extract the domain part
    if domain not in domain_list:
        return False
    

def is_valid_password(password):
    # Regular expression for validating password strength
    password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$'
    
    return bool(re.match(password_regex, password))



def check_password_for_spaces(password):
    """
    Check if the password contains any spaces.
    
    Args:
    password (str): The password string to check.
    
    Returns:
    bool: Returns True if the password contains spaces, otherwise False.
    """
    if " " in password:
        return True
    return False


def verify_user(identifier,data):
    """
    Verify if the user is valid.
    """

    
    email_sender = [data.get('email')]


    response = email_middleware(identifier,data,email_sender)
    return response




    


