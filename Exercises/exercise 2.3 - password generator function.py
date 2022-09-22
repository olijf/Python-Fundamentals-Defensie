import random
import string

def generate_wachtwoord(required_length = 8,
                        n_lowercase = 2,
                        n_uppercase = 2,
                        n_numbers = 1,
                        n_special = 1):

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

def check_password(password,
                   required_length = 8,
                   required_n_lowercase = 2,
                   required_n_uppercase = 2,
                   required_n_digits = 1,
                   required_n_special = 1):

    n_uppercase = len(list(filter(lambda c: c in string.ascii_uppercase, password)))
    n_lowercase = len(list(filter(lambda c: c in string.ascii_lowercase, password)))
    n_digits = len(list(filter(lambda c: c in string.digits, password)))
    n_special = len(list(filter(lambda c: c in string.punctuation, password)))

    if len(password) < required_length:
        return False
    elif n_lowercase < required_n_lowercase:
        return False
    elif n_uppercase < required_n_uppercase:
        return False
    elif n_digits < required_n_digits:
        return False
    elif n_special < required_n_special:
        return False
    else:
        return True

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

wachtwoord = input('Geef wachtwoord: ')
if check_password(wachtwoord):
    print('Wachtwoord is OK.')
else:
    print('Wachtwoord voldoet niet aan de eisen.')
