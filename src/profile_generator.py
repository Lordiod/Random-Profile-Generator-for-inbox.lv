"""
Performance-optimized profile generator
Uses minimal imports and pre-computed data for faster generation
"""

from random import choices, randint
from string import ascii_lowercase, ascii_letters, digits
from datetime import datetime

# Pre-computed character sets for faster access
_LOWER_CHARS = ascii_lowercase
_ALL_CHARS = ascii_letters + digits
_ANSWER_CHARS = ascii_lowercase + digits

# Cache for name generation - only import when needed
_names_cache = None


def _get_names_module():
    """Lazy import names module"""
    global _names_cache
    if _names_cache is None:
        import names

        _names_cache = names
    return _names_cache


def generate_random_string(length, char_set=_LOWER_CHARS):
    """Fast string generation using pre-computed character sets"""
    return "".join(choices(char_set, k=length))


def create_random_profile_fast():
    """
    Ultra-fast profile generation with minimal overhead
    """
    # Generate basic data without imports
    username = generate_random_string(10)
    email = f"{username}@inbox.lv"
    password = generate_random_string(10, char_set=_ALL_CHARS)
    inbox_answer = generate_random_string(6, char_set=_ANSWER_CHARS)

    # Only import names when actually generating profile
    names_module = _get_names_module()
    first_name = names_module.get_first_name()
    last_name = names_module.get_last_name()

    # Fixed data for speed
    date_of_birth = "01 January 2000"
    passsssss = f"{password}{randint(100, 999)}"

    # Pre-formatted template for speed
    profile = f"""Login email: {email}
Password email: {passsssss}
Password epic games: {passsssss}
First name: {first_name}
Last name: {last_name}
Date of birth: {date_of_birth}
Country: Egypt
Cars unlocked: 11
Question: What is your pet's name?
Answer: {inbox_answer}

username: {username}
"""
    return profile


# Alias for compatibility
create_random_profile = create_random_profile_fast
