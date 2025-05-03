def generate_random_string(length, char_set=ascii_lowercase):
    return ''.join(choices(char_set, k=length))

def generate_random_username(length=10):
    return generate_random_string(length)

def generate_random_password(length=10, char_set=ascii_letters + digits):
    return generate_random_string(length, char_set)

def generate_inbox_answer(length=6, char_set=ascii_lowercase + digits):
    return generate_random_string(length, char_set)