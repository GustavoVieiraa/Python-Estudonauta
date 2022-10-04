#Faça um programa que leia a largura e a altura de uma parede em metros, calcule
#sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro
#de tinta, pinta uma área de 2m².

print('=' * 15 + 'Pintura economica' + '=' * 15)

v_alt = float(input('Informe altura: '))
v_lar = float(input('Informe a largura: '))
v_area = (v_alt*v_lar)
v_tinta = (v_area/2)
print('Área: {}m²'.format(v_area))
print('Você precisa de {}L de tinta para pintar {}m².'.format(v_tinta, v_area))

print('=' * 15 + 'Pintura economica' + '=' * 15)