# Simulação Simplificada de ROI (Native Python)

months = range(1, 7)
tokens_saved = [100000, 250000, 500000, 1000000, 2500000, 5000000]
token_price = 0.000015 # por token

roi_log = []
total_roi = 0

for i, month in enumerate(months):
    savings = tokens_saved[i] * token_price
    cost = 50 * month # Manutenção crescente
    net = savings - cost
    total_roi += net
    roi_log.append((month, net))

print(f"Total ROI em 6 meses: ${total_roi:.2f}")
for m, n in roi_log:
    if n > 0:
        print(f"Ponto de Equilíbrio atingido no Mês {m} (Lucro: ${n:.2f})")
        break
