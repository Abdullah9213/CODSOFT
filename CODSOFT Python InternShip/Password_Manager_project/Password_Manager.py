import random
import string


def generate_predefined_password(length):
    # Define the ratios of characters
    upper_ratio = 0.3
    lower_ratio = 0.3
    digit_ratio = 0.2
    special_ratio = 0.2

    # Calculate the number of characters for each type based on the length of the password
    upper_count = int(length * upper_ratio)
    lower_count = int(length * lower_ratio)
    digit_count = int(length * digit_ratio)
    special_count = length - (upper_count + lower_count + digit_count)

    # Generate character sets for each type
    upper_case = ''.join(random.choices(string.ascii_uppercase, k=upper_count))
    lower_case = ''.join(random.choices(string.ascii_lowercase, k=lower_count))
    digits = ''.join(random.choices(string.digits, k=digit_count))
    special_chars = ''.join(random.choices(string.punctuation, k=special_count))

    # Combine all character sets
    chars = upper_case + lower_case + digits + special_chars

    # Shuffle the characters to ensure randomness
    password = ''.join(random.sample(chars, k=length))

    return password


def generate_random_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    chars = lower_case + upper_case + digits + special_chars

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def generate_defined_password(length, upper_count, lower_count, digit_count, special_count):
    # Validate if the total count matches the length of the password
    total_count = upper_count + lower_count + digit_count + special_count
    if total_count != length:
        print("Error: Total count of characters must match the length of the password.")
        return None

    # Generate character sets for each type
    upper_case = ''.join(random.choices(string.ascii_uppercase, k=upper_count))
    lower_case = ''.join(random.choices(string.ascii_lowercase, k=lower_count))
    digits = ''.join(random.choices(string.digits, k=digit_count))
    special_chars = ''.join(random.choices(string.punctuation, k=special_count))

    # Combine all character sets
    chars = upper_case + lower_case + digits + special_chars

    # Shuffle the characters to ensure randomness
    password = ''.join(random.sample(chars, k=length))

    return password


