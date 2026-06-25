def validarCPF(cpf):

    if len(cpf) != 11:
        return False

    for i in range(11):
        if cpf[i] < '0' or cpf[i] > '9':
            return False

    soma = 0

    for i in range(9):
        soma = soma + int(cpf[i]) * (10 - i)

    d1 = 11 - (soma % 11)

    if d1 == 10 or d1 == 11:
        d1 = 0

    if d1 != int(cpf[9]):
        return False

    soma = 0

    for i in range(10):
        soma = soma + int(cpf[i]) * (11 - i)

    d2 = 11 - (soma % 11)

    if d2 == 10 or d2 == 11:
        d2 = 0

    if d2 != int(cpf[10]):
        return False

    return True

def validarEmail(email):

    if "@" not in email:
        return False

    if "." not in email:
        return False

    return True