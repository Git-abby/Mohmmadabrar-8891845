def is_valid_phone_number(phone_number, max_length=15):
    """
    Check if the given phone number is valid and within the maximum length.
    """
    phone_str = str(phone_number)
    if phone_str.startswith('+') or (phone_str and phone_str[0].isdigit()):
        # Additional checks for digits and length can be performed here
        if phone_str[1:].isdigit() and len(phone_str) <= max_length:
            return True
    return False

def is_valid_email(email):
    """
    Check if the given email is valid.
    """
    # This is a simple check, and in a real-world scenario, you'd want a more comprehensive validation.
    return '@' in email and '.' in email.split('@')[-1]
