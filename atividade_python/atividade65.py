numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)  

maior =max(numeros)
menor = min(numeros)    
print("\nNúmeros digitados:", numeros)
print("Maior número:", maior) 
print("Menor número:", menor)    
