#estructura de control de ciclo WHILE
#solicitar al usuario la cantidad de datos a analizar
n = int(input("¿cuantos datos deseas ingresar?"))

#leer los datos 
datos = []
contador = 0
while contador < n:
    valor = float(input(f"ingrese el valor {contador + 1}:"))
    datos.append(valor)
    contador += 1

    #analisis con ciclo while
    indice = 0
    suma = 0 
    maximo = datos[0]
    minimo = datos [0]
    positivos = 0 
    negativos = 0
    ceros = 0

    while indice < n:
        valor = datos[indice]
        suma += valor
        if valor > maximo:
            maximo = valor
            if valor < minimo:
                if valor > 0: 
                    positivos += 1
                elif valor < 0:
                    negativos += 1
                else:
                    ceros += 1 
                    indice += 1 

                    #resultados
                    promedio = suma / n

                    print("\nResultados del analisis:")
                    print("datos imgresados:", datos)
                    print("suma:", suma)
                    print("promedio:", promedio)
                    print("valor maximo:", maximo)
                    print("valor minimo:", minimo)
                    print("cantidad de positivos:", positivos)
                    print("cantidad de negativos:", negativos)
                    print("cantidad de ceros:", ceros)
