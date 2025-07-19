def calcular_tributos(valor_unitario, quantidade, regime):
    total_bruto = valor_unitario * quantidade
    if regime == "Simples Nacional":
        icms = total_bruto * 0.04
        ipi = 0
        pis = total_bruto * 0.0065
        cofins = total_bruto * 0.03
    else:
        icms = total_bruto * 0.12
        ipi = total_bruto * 0.05
        pis = total_bruto * 0.0165
        cofins = total_bruto * 0.076

    total = total_bruto + ipi
    return total, icms, ipi, pis, cofins
