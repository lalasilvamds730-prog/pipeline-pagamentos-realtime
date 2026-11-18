import csv

ARQUIVO = "pagamentos_teste.csv"
LIMITE_SUSPEITO = 1000.00

print("=" * 50)
print("ANALISE DE PAGAMENTOS EM TEMPO REAL")
print("=" * 50)

total = 0
suspeitos = 0
valor_total = 0.0

with open(ARQUIVO, mode="r", encoding="utf-8-sig") as arquivo:
    pagamentos = csv.DictReader(arquivo)

    for pagamento in pagamentos:
        total += 1

        valor = float(pagamento["amount"])
        valor_total += valor

        print(f"\nTransacao: {pagamento['transaction_id']}")
        print(f"Cartao: {pagamento['card_id']}")
        print(f"Valor: R$ {valor:.2f}")
        print(f"Status: {pagamento['status']}")

        if valor >= LIMITE_SUSPEITO:
            suspeitos += 1
            print("ALERTA: valor elevado! Verificar pagamento.")

print("\n" + "=" * 50)
print("RESUMO DA ANALISE")
print("=" * 50)
print(f"Total de pagamentos: {total}")
print(f"Pagamentos suspeitos: {suspeitos}")
print(f"Valor total: R$ {valor_total:.2f}")
print("Analise concluida!")