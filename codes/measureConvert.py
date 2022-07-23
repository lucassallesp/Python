#Esse programa converte uma medida em metros para centimetro e milimetros.

medida = float(input('Digite uma medida em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hec = medida / 100
km = medida / 1000
print(f'Conversões de {medida:.2f}m:\n {mm:.2f}mm\n {cm:.2f}cm\n {dm:.2f}dm\n {dam:.2f}dam\n {hec:.2f}hec\n {km:.2f}km')

