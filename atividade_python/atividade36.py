meses =["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

numero_mes = int(input("Digite um numero de 1 a 12: "))

if 1<= numero_mes <=12:
    numero_do_mes = meses[numero_mes]
    print(f"O mês correspondente é: {numero_do_mes}")
else:
    print("Número inválido! Digite um número entre 1 e 12.") 