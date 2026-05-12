## Projetos

- calculo_rendimento.py
- sistema_pagamento.py
entrada = input()

valor, parcelas = entrada.split()

valor = float(valor)
parcelas = int(parcelas)

if parcelas == 1:
    valor_final = valor * 0.95
    valor_parcelas = valor_final
elif parcelas == 2:
    valor_final = valor
    valor_parcelas = (valor_final / 2)
elif parcelas == 3:
    valor_final = valor * 1.05
    valor_parcelas = (valor_final / 3)
else:
    valor_final = valor * 1.10
    valor_parcelas = (valor_final / parcelas)
    
print(f"{valor_final:.2f} {valor_parcelas:.2f}")
