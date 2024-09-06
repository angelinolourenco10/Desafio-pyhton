
faturamento_diario = [1000, 1500, 0, 0, 1200, 1800, 0, 0, 0, 3000, 500, 0, 0, 2200] # e assim por diante...

def calcular_faturamento(faturamento_diario):
    dias_com_faturamento = [dia for dia in faturamento_diario if dia > 0]
    
    # Se não houver dias com faturamento, não faz sentido continuar
    if not dias_com_faturamento:
        return "Não há dias com faturamento disponível para cálculo."

    menor_faturamento = min(dias_com_faturamento)

    maior_faturamento = max(dias_com_faturamento)

    media_anual = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = len([dia for dia in dias_com_faturamento if dia > media_anual])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, acima_da_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Dias com faturamento superior à média anual: {acima_da_media}")
