soma = 0 

for i in range(10):
    numero = float(input(f"Digite o {i+1}° número: "))
    soma += numero
media = soma / 10 
print(f"A média dos números digitados é: {media}")    
