import re


def valid_email(mail):
    if mail.count('@') == 1:
        return True
    return False


def valid_login(login):
    if len(login) >= 6:
        if login[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            regex = "^[a-zA-Z0-9_]+$"
            pattern = re.compile(regex)
            if pattern.search(login) is not None:
                return True
    return False


def valid_password(password):
    k1 = False
    k2 = False
    k3 = False
    k4 = False
    if len(password) >= 8:
        for i in password:
            if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                k1 = True
            if i in 'abcdefghijklmnopqrstuvwxyz':
                k2 = True
            if i in '0123456789':
                k3 = True
            if i in '_-+*.!%$#@&*^|\/~[]{}':
                k4 = True
        if k1 and k2 and k3 and k4:
            return True
    return False

# print(valid_password('Qwer1ty@'))
