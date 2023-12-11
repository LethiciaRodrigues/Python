print('Pintando uma parede')
l=float(input('Por favor, digite a largura da parede:')) 
h=float(input('Por favor, digite a altura da parede:'))
b = h * l
print(f'A parede possui as dimensões de {l}X{h} e a aréa é {b} m²')
t= b/2 
print(f'Para pintar essa parede, você precisará de {t}L de tinta')