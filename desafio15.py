print('Alugel de carros')
dias = int (input('Por quantos dias o carro foi usado: '))
km = float (input(' Qual a quantidade de Kms rodados: '))
alugel = (dias * 60 ) + (km * 0.15)
print(f'Com os dias alugados {dias} e a quantidade de Kms rodados {km}, o total do alugel do carro é R$ {alugel} :')
