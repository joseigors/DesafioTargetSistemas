import json

# abre o arquivo JSON e carrega os dados em uma lista de dicionários
with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)

# inicializa as variáveis para calcular o menor valor, o maior valor e a soma do faturamento mensal
menor_valor = float('inf')
maior_valor = float('-inf')
faturamento_mensal = 0

# percorre os dicionários de faturamento diário e calcula o menor valor, o maior valor e a soma do faturamento mensal
for dia in faturamento_diario:
    valor = dia['valor']
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    faturamento_mensal += valor

# calcula a média do faturamento diário, desconsiderando os dias sem faturamento
dias_com_faturamento = sum(1 for dia in faturamento_diario if dia['valor'] > 0)
media_mensal = faturamento_mensal / dias_com_faturamento

# conta o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for dia in faturamento_diario if dia['valor'] > media_mensal)

# imprime os resultados
print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias com faturamento acima da média mensal:', dias_acima_da_media)
