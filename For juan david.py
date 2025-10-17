#estructura de control de ciclo FOR 
#ingresamos nombres 
nombres = [
    "ANGEL MAURICIO", "MARCO ANTONIO", "EDGAR DANIEL", "BETHZY ALEYDIZ", "FABIOLA MICHEL", "FRIDA VICTORIA", "ERNESTO YAHIR",
      "ANGEL YAEL", "AMBAR NAHOMI", "URIEL", "LUIS ENRIQUE", "BRAYAN ALEXANDER", "ERICK", "FERNANDA ABIGAIL", "ESTEFANI SARAHI",
        "YUMIKO JATZERY", "HANSEL DANIEL", "JULIO ALBERTO", "ENRIQUE UCIEL", "YOJAN JOEL", "PEDRO EDUARDO", "MIREYA YAMILE",
         "ALISON DAYANADA", "PRISCILA", "SERGIO ALEXIS", "RICARDO", "SAMUEL JESHUA", "VANESSA ISABEL", "SARAHI VALERIA", 
         "DAVID GERSSAYN", "JOSE ANGEL", "GABRIEL", "CHRISTIAN YUREM", "ARTURO AZAEL", "ARMANDO"
]
#1. nombres que se retiraran "ANGEL MAURICIO", "MARCO ANTONIO", "FABIOLA MICHEL"
NOMBRES = ("ANGEL MAURICIO", "MARCO ANTONIO", "FABIOLA MICHEL")
inicio_NOMBRE = 0 
for nombre in nombres: 
    if nombre[0] in NOMBRES:
        inicio_NOMBRE += 1
        print("nombres que inician con ANGEL MAURICIO, MARCO ANTONIO, FABIOLA MICHEL:")
#1. Cuantos nombres inicia con vocal
vocales = ("A", "E", "I", "O", "U")
inicio_vocal = 0 
for nombre in nombres: 
    if nombre[0] in vocales:
        inicio_vocal += 1
        print("nombres que inician con vocal:", inicio_vocal)

        #2 Cuantos nombres tienen mas de 10 letras
        mas_de_10=0
        for nombre in nombres:
            if len(nombre.replace(" ", "")) > 10:
                mas_de_10 += 1
                print("nombres con mas de 10 caracteres (sin espacio):", mas_de_10)

                #3. primeros 3 nombres en orden alfabetico 
                nombres_ordenados = sorted(nombres)
                print("primeros 3 nombres en orden alfabetico:")
for nombre in nombres_ordenados[:3]:
    print(nombre)

    #4. Buscar los nombres que contienen la letra "y"
    con_y = []
    for nombre in nombres:
        if "y" in nombre:
            con_y.append(nombre)
            print("nombres que contienen la letra Y:")
            for nombre in con_y:
                print(nombre)


                