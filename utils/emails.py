from django.template.loader import render_to_string
from django.core.mail import send_mail


import uuid
import secrets
import logging

import importlib

print("**************** email package ******************************")

# def get_template_data_func():
#     """This function returns the template data function"""
#     message_module = importlib.util('email_messages_content', '/utils/email_messages_content.py')
#     content_data = message_module.email_content
#     return content_data
# import importlib.util

import importlib.util

import importlib.util
import os

def get_template_data_func():
    """This function returns the template data function."""
    # Define the absolute path to your module
    module_path = os.path.join(os.path.dirname(__file__), 'email_messages_content.py')  # Correctly pointing to the file

    # Create a module specification from the file location
    spec = importlib.util.spec_from_file_location("email_messages_content", module_path)

    # Check if spec is None before proceeding
    if spec is None:
        raise ImportError(f"Cannot find module at {module_path}")

    # Create a module from the spec
    message_module = importlib.util.module_from_spec(spec)

    # Load the module
    spec.loader.exec_module(message_module)

    # Access the email_content function or variable
    content_data = message_module.email_content
    return content_data



def email_middleware(identifier, data, email_sender):
    """
    Middleware function to handle email processing.

    Args:
        identifier (str): Identifier for the email content.
        data (dict): Data required to populate the email content.\n
        {
            "verification_code": "<Verifcation Code>",
            "token": "<Token>",
            "uuid": "<UUID>"

        }
        \n
        email_sender (list): List of email addresses to send the email to.

    Notes:
        - Imports email_content from email_messages_content.py to retrieve email content.
        - Checks if the identifier is present in the content; throws an error if not found.
        - Retrieves the data corresponding to the identifier and calls email_content with the necessary data.
        - Utilizes string formatting to dynamically append data into the email content.
        - Calls send_mail with the obtained content to send the email.
    """
    email_content = get_template_data_func()
    content_data = email_content(identifier, data)
    # Calling send mail function to send email.
    mail_send = send_email(email_sender,content_data)
    if not mail_send:
        return False
    return True


from django.core.mail import send_mail
from django.template.loader import render_to_string
import logging

def send_email(email_sender, content_data):
    """
    Function to send email.
    Args:
    email_sender (list): List of email addresses to send the email to.
    content_data (dict): Data required to populate the email content.
    """
    # Email template for the messages.
    email_template_name = "mail.html"

    # Subject and sender details from content data
    subject = content_data["subject"]
    sender = content_data["from"][-1]  # Assuming "from" contains sender email

    # Render the email content
    mail_content = render_to_string(email_template_name, content_data)

    try:
        # Ensure email_sender is a list
        if isinstance(email_sender, str):
            email_sender = [email_sender]  # Wrap in a list if it's a single string

        # Send mail to user
        send_mail(
            subject,
            "",  # Use an empty string for plain text content
            sender,
            email_sender,  # This should now be a list
            fail_silently=False,
            html_message=mail_content,
        )
        logging.info("Successfully sent email")

        return True

    except Exception as error:
        logging.exception(
            f"Add exception for {error.__class__.__name__} in send_email"
        )
        logging.error(f"Error while sending email: {error}")
        return False
