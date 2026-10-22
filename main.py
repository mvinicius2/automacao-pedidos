import csv

with open("pedidos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    faturamento = 0
    pedidos_processados = 0
    pedidos_rejeitados = 0
    relatorio = []

    for pedido in leitor:
        identificador = pedido["pedido_id"]

        try:
            preco = float(pedido["preco"])

        except ValueError:
            print(f"Pedido {identificador} rejeitado: preço inválido.")
            pedidos_rejeitados += 1
            continue

        try:
            quantidade = int(pedido["quantidade"])
        except ValueError:
            print(f"Pedido {identificador} rejeitado: quantidade inválida.")
            pedidos_rejeitados += 1
            continue

        if preco < 0 or quantidade < 0:
            print(f"Pedido {identificador} rejeitado: preço ou quantidade negativos.")
            pedidos_rejeitados += 1
            continue
        else:

            resultado = preco * quantidade
            relatorio.append(
                {
                    "pedido_id": identificador,
                    "quantidade": quantidade,
                    "total": resultado,
                }
            )

            faturamento += resultado

            pedidos_processados += 1

            print(f"Pedido {identificador}: R${resultado:.2f}")

print(f"Pedidos processados: {pedidos_processados}")
print(f"Pedidos rejeitados: {pedidos_rejeitados}")
print(f"Faturamento total R${faturamento:.2f}")

with open("relatorio.csv", "w", newline="", encoding="utf-8") as arquivo_saida:
    escritor = csv.DictWriter(
        arquivo_saida, fieldnames=["pedido_id", "quantidade", "total"]
    )
    escritor.writeheader()
    escritor.writerows(relatorio)

resumo = {
    "pedidos_processados": pedidos_processados,
    "pedidos_rejeitados": pedidos_rejeitados,
    "faturamento": faturamento,
}

with open("resumo.csv", "w", newline="", encoding="utf-8") as arquivo_saida:
    escritor = csv.DictWriter(
        arquivo_saida,
        fieldnames=["pedidos_processados", "pedidos_rejeitados", "faturamento"],
    )
    escritor.writeheader()
    escritor.writerow(resumo)
