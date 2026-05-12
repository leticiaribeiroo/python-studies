deposito = float(input("Digite o valor do depósito: "))
taxa = float(input("Digite a taxa (%): "))

rendimento = deposito * (taxa / 100)
total = deposito + rendimento

print(f"Rendimento: R$ {rendimento:.2f}")
print(f"Total: R$ {total:.2f}")
