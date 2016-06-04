import math


def Acoordenadas(gen):
    if gen == 1 or gen == 9:
        return [1, 1.5]
    if gen == 15 or gen == 16:
        return [7.5, 2]

    if gen % 8 == 0:
        x = 8
    else:
        x = round(gen % 8 - 0.1)
    if gen % 8 == 0:
        y = gen / 8
    else:
        y = gen / 8 + 1
    return [x, y]


def distanciaEuclideana(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))


estaciones = []

estaciones.append("Materia Prima1")  # fija
estaciones.append("Materia Prima2")
estaciones.append("Tripay")  # fija
estaciones.append("Estacion 1")
estaciones.append("Estacion 2")
estaciones.append("Estacion 3")
estaciones.append("Esclopeadora")
estaciones.append("Destrozadora")
estaciones.append("Trompo")
estaciones.append("Cepillo")
estaciones.append("Sierra cinta")
estaciones.append("Soporte U 1")
estaciones.append("Soporte U 2")
estaciones.append("Canteadora R")
estaciones.append("Canteadora")
estaciones.append("Almacen Producto1")  # fija
estaciones.append("Almacen Producto2")
estaciones.append("Bano")  # fija

ruta1 = [estaciones.index("Estacion 1"),
         estaciones.index("Materia Prima1"),
         estaciones.index("Canteadora R"),
         estaciones.index("Cepillo"),
         estaciones.index("Soporte U 2"),
         estaciones.index("Canteadora"),
         estaciones.index("Soporte U 1"),
         estaciones.index("Estacion 1"),
         estaciones.index("Tripay"),
         estaciones.index("Estacion 1"),
         estaciones.index("Sierra cinta"),
         estaciones.index("Estacion 1"),
         estaciones.index("Soporte U 2"),
         estaciones.index("Estacion 1"),
         estaciones.index("Almacen Producto1")
         ]

ruta2 = [estaciones.index("Estacion 2"),
         estaciones.index("Tripay"),
         estaciones.index("Estacion 2"),
         estaciones.index("Sierra cinta"),
         estaciones.index("Trompo"),
         estaciones.index("Estacion 2"),

         estaciones.index("Materia Prima1"),
         estaciones.index("Destrozadora"),
         estaciones.index("Canteadora R"),
         estaciones.index("Estacion 2"),
         estaciones.index("Sierra cinta"),
         estaciones.index("Canteadora"),
         estaciones.index("Cepillo"),
         estaciones.index("Estacion 2"),
         estaciones.index("Trompo"),
         estaciones.index("Estacion 2"),
         estaciones.index("Soporte U 2"),
         estaciones.index("Estacion 2"),
         estaciones.index("Esclopeadora"),
         estaciones.index("Estacion 2"),
         estaciones.index("Almacen Producto1")
         ]

ruta3 = [estaciones.index("Estacion 3"),
         estaciones.index("Materia Prima1"),
         estaciones.index("Destrozadora"),
         estaciones.index("Canteadora R"),
         estaciones.index("Cepillo"),
         estaciones.index("Soporte U 2"),
         estaciones.index("Canteadora"),
         estaciones.index("Estacion 3"),
         estaciones.index("Soporte U 1"),
         estaciones.index("Estacion 3"),
         estaciones.index("Trompo"),
         estaciones.index("Estacion 3"),
         estaciones.index("Esclopeadora"),
         estaciones.index("Estacion 3"),
         estaciones.index("Almacen Producto1")
         ]

fijas = [[estaciones.index("Materia Prima1"), 1],
         [estaciones.index("Materia Prima2"), 9],
         [estaciones.index("Tripay"), 17],
         [estaciones.index("Almacen Producto1"), 15],
         [estaciones.index("Almacen Producto2"), 16],
         [estaciones.index("Bano"), 25]
         ]


def eval_func(cromosoma):
    score1 = 0
    score2 = 0
    score3 = 0
    # Fijos
    for f in fijas:
        if cromosoma[f[0]] != f[1]:
            return 10000
    # ruta1 tiene los indices de las estaciones a recorrer
    for r1 in range(0, len(ruta1) - 1):
        score1 += distanciaEuclideana(Acoordenadas(cromosoma[ruta1[r1]]), Acoordenadas(cromosoma[ruta1[r1 + 1]])) * 2.2

    for r2 in range(0, len(ruta2) - 1):
        score2 += distanciaEuclideana(Acoordenadas(cromosoma[ruta2[r2]]), Acoordenadas(cromosoma[ruta2[r2 + 1]])) * 2.2

    for r3 in range(0, len(ruta3) - 1):
        score3 += distanciaEuclideana(Acoordenadas(cromosoma[ruta3[r3]]), Acoordenadas(cromosoma[ruta3[r3 + 1]])) * 2.2

    return score1 + score2 + score3


res = [1, 9, 17, 10, 31, 24, 5, 3, 29, 19, 2, 11, 20, 18, 12, 15, 16, 25]
res2 = [1, 9, 17, 15, 16, 25]

# print(len(estaciones))
# print(len(res))
print(ruta1)

print(eval_func(res))


# for r1 in range(0, len(ruta1) - 1):
#    print(ruta1[r1])

# for r1 in range(0, len(ruta1) - 1):
# score1 += distanciaEuclideana(Acoordenadas(res[ruta1[r1]]), Acoordenadas(res[ruta1[r1+1] ])) * 2.2
