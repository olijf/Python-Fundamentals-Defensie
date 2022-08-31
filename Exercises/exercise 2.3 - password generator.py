import random

def generate_wachtwoord(required_length = 8,
                        n_lowercase = 2,
                        n_uppercase = 2,
                        n_numbers = 1,
                        n_special = 1):
    """Deze functie genereerd een wachtwoord
    required_length is de minimale lengte"""

    LOWERCASE_CHARACTERS = 'abcdefghijkmnopqrstuvwxyz'    # removed l
    UPPERCASE_CHARACTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ'     # removed I and O
    NUMBER_CHARACTERS = '0123456789'
    SPECIAL_CHARACTERS = '@#$%&*+?!'

    lower = random.choices(LOWERCASE_CHARACTERS, k = n_lowercase)
    upper = random.choices(UPPERCASE_CHARACTERS, k = n_uppercase)
    numbers = random.choices(NUMBER_CHARACTERS, k = n_numbers)
    special = random.choices(SPECIAL_CHARACTERS, k = n_special)
    extra = random.choices(LOWERCASE_CHARACTERS +
                           UPPERCASE_CHARACTERS +
                           NUMBER_CHARACTERS +
                           SPECIAL_CHARACTERS,
                           k = required_length - n_lowercase - n_uppercase - n_numbers - n_special)

    all_characters = lower + upper + numbers + special + extra

    random.shuffle(all_characters)

    password = ''.join(all_characters)

    return password

def wachtwoord_met_invoer():
    required_length = int(input('Hoe lang? '))
    n_lowercase = int(input('Aantal kleine letters? '))
    n_uppercase = int(input('Aantal hoofdletters? '))
    n_numbers = int(input('Aantal cijfers? '))
    n_special = int(input('Aantal speciale karakters? '))

    wachtwoord = generate_wachtwoord(required_length,
                        n_lowercase,
                        n_uppercase,
                        n_numbers,
                        n_special)

    return wachtwoord

# -----------------------------------------------------

print('New password: ', generate_wachtwoord())
print('New password: ', generate_wachtwoord(required_length =7))
print('New password: ', generate_wachtwoord(20))

print('New password: ', generate_wachtwoord(required_length = 1, n_uppercase = 5))

print(wachtwoord_met_invoer())