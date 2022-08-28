
def foolproof_input(prompt, lower_bound, upper_bound):

    while True:
        try:
            response = input(prompt)
            number = int(response)

            if lower_bound <= number <= upper_bound:
                return number
            else:
                print('%d is not between %d and %d.' % (number, lower_bound, upper_bound))

        except ValueError:
            print('"%s" is not a number.' % response)

        except KeyboardInterrupt:
            print('\nOK. Stoping now.')
            break

# ============================================

if __name__ == '__main__':

    number = foolproof_input('Give me a number between 1 and 10: ', 1, 10)

    if number is not None:
        print('The number you entered (%d) is OK' % number)
