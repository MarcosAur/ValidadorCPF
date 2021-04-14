def calcular(cpf):
    soma = 0
    for pos, valor in enumerate(reversed(cpf)):
        soma += int(valor) * (pos + 2)
    return soma
def gerarDigito(soma):
    confirmacao = 11 - (soma % 11)
    if confirmacao > 9:
        return '0'
    else:
        return str(confirmacao)

validador = False
cpf = input("Digite o CPF  que será validado (Formato: XXX.XXX.XXX-XX): ").split('.') #168.995.350-09
cpf_cortado = "".join(cpf).split('-')
cpf = cpf_cortado[0]
cpf_cortado = "".join(cpf_cortado)

soma = calcular(cpf)
cpf += gerarDigito(soma)

soma = calcular(cpf)
cpf += gerarDigito(soma)
for valor in cpf:
    if valor != cpf[0]:
        validador = True
        break
valido = 'Valido' if cpf == cpf_cortado and validador else 'Invalido'
print(valido)

