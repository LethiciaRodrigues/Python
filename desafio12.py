print('Calculando descontos')
p = float(input('Qual o valor atual do produto? R$'))
d = p - (p * 5 / 100)
print(f'O produto que custava R${p :.2f}, com 5% de desconto vai custar R$ {d :.2f}.')