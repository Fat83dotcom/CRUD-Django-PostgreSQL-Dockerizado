import re


def validar_senha(senha):
    regex = r"^(?=(?:[^a-zA-Z]*[a-zA-Z]){4})(?=(?:[^\W_]*[\W_]){4}).{12,}$"
    if re.match(regex, senha):
        return True
    else:
        return False
