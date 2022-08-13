numero=int(input("Digite un numero entero: "))

residuo=numero%3
print(f'el residuo  es {residuo}')


#CONDICIONAL SIMPLE EN PYTHON
if(residuo==0):
    print(f"{numero} es multiplo de 3")
    
else:
    print(f'{numero} no es multiplo de 3')
print("fin del programa")
    