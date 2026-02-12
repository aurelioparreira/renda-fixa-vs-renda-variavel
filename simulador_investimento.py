valor = float(input("Valor inicial: "))
taxa = float(input("Taxa anual (ex: 0.12 para 12%): "))
anos = int(input("Número de anos: "))

montante = valor * (1 + taxa) ** anos

print("\nResultado da simulação:")
print("Valor final:", round(montante, 2))
