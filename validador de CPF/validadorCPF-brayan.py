# Algoritimo para calcular número de CPF
# Iniciei as listas
noveNumeroCPF = []

noveNumeroCPF =int(input("Digite os nove números do CPF:"))

# A partir dos 9 primeiros digitos do CPF, multiplica-se cada dígito por um número, começando por 1 e imcrementando para cada digito.

primeiro_digito = int(str(noveNumeroCPF)[0])
primeiro_digito_multiplicado = primeiro_digito

segundo_digito = int(str(noveNumeroCPF)[1])
segundo_digito_multiplicado = segundo_digito * 2

terceiro_digito = int(str(noveNumeroCPF)[2])
terceiro_digito_multiplicado = terceiro_digito * 3

quarto_digito = int(str(noveNumeroCPF)[3])
quarto_digito_multiplicado = quarto_digito * 4

quinta_digito = int(str(noveNumeroCPF)[4])
quinta_digito_multiplicado = quinta_digito * 5

sexta_digito = int(str(noveNumeroCPF)[5])
sexta_digito_multiplicado = sexta_digito * 6

setimo_digito = int(str(noveNumeroCPF)[6])
setimo_digito_multiplicado = setimo_digito * 7

oitavo_digito = int(str(noveNumeroCPF)[7])
oitavo_digito_multiplicado = oitavo_digito * 8

nono_digito = int(str(noveNumeroCPF)[8])
nono_digito_multiplicado = nono_digito * 9

# somando os números os produtos:

soma_dos_nove_primeiros_digitos = primeiro_digito_multiplicado + segundo_digito_multiplicado + terceiro_digito_multiplicado + quarto_digito_multiplicado + quinta_digito_multiplicado + sexta_digito_multiplicado + setimo_digito_multiplicado + oitavo_digito_multiplicado + nono_digito_multiplicado


# dividindo os números os produtos:

decimo_digito = soma_dos_nove_primeiros_digitos % 11


# verificando o ultimo número

primeiro_digito = int(str(noveNumeroCPF)[0])
primeiro_digito_multiplicado = primeiro_digito * 0

segundo_digito = int(str(noveNumeroCPF)[1])
segundo_digito_multiplicado = segundo_digito * 1

terceiro_digito = int(str(noveNumeroCPF)[2])
terceiro_digito_multiplicado = terceiro_digito * 2

quarto_digito = int(str(noveNumeroCPF)[3])
quarto_digito_multiplicado = quarto_digito * 3

quinta_digito = int(str(noveNumeroCPF)[4])
quinta_digito_multiplicado = quinta_digito * 4

sexta_digito = int(str(noveNumeroCPF)[5])
sexta_digito_multiplicado = sexta_digito * 5

setimo_digito = int(str(noveNumeroCPF)[6])
setimo_digito_multiplicado = setimo_digito * 6

oitavo_digito = int(str(noveNumeroCPF)[7])
oitavo_digito_multiplicado = oitavo_digito * 7

nono_digito = int(str(noveNumeroCPF)[8])
nono_digito_multiplicado = nono_digito * 8

decimo_digito = decimo_digito
decimo_digito_multiplicado = decimo_digito * 9


# somando os números os produtos:


soma_dos_dez_primeiros_digitos = primeiro_digito_multiplicado + segundo_digito_multiplicado + terceiro_digito_multiplicado + quarto_digito_multiplicado + quinta_digito_multiplicado + sexta_digito_multiplicado + setimo_digito_multiplicado + oitavo_digito_multiplicado + nono_digito_multiplicado + decimo_digito_multiplicado


decimo_primeiro = soma_dos_dez_primeiros_digitos % 11

# reveland os números:
print(decimo_digito,decimo_primeiro)


