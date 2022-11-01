
def banner(text):
    n = len(text)
    print('***' + '*' * n + '***')
    print('*  ' + text    + '  *')
    print('***' + '*' * n + '***')


def banner(text, width = None, c = '*'):
    n = len(text)
    if width:
        prefix = ((width - n) // 2) * ' '
    else:
        prefix = ''
    print(prefix + c * (n + 6))
    print(prefix + c + '  ' + text    + '  ' + c)
    print(prefix + c * (n + 6))

def create_banner(text, c='*'):
    n = len(text)
    s  = c * (n + 6) + '\n'
    s += c + '  ' + text + '  ' + c + '\n'
    s += c * (n + 6)
    return s

def print_banner(text):
    print(create_banner(text, '+'))


# ----------------------------------------------------------------

if __name__ == '__main__':

    banner('abacadabra')