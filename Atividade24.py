# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
m = 0
c = 0

while True:
    n = int(input("Digite a quantidade de números que você quer tirar a média, digite -1 para parar: "))
    if n == -1:
        break

    m += n 

    c += 1

    if c > 0:
        med = m//c
print (med)