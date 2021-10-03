# trabalhando com listas

bicicletas = ['trek','cannondale','redline','specialized']

print(bicicletas)
print(bicicletas[2].title())

# alterando elementos da lista

bicicletas[2] = "caloi"

print(bicicletas)

# adicionando elementos na lista

bicicletas.append("bicicleta1")

bicicletas.insert(5, "bicicleta2")

bicicletas.insert(6,"bicicleta3")

print(bicicletas)

# remover elementos da lista

bicicletas_alteradas = bicicletas.pop()

print(bicicletas_alteradas)

print(bicicletas)

bicicletas.remove("bicicleta2")

print(bicicletas)

# ordenando a lista

# sort()
print(bicicletas)
bicicletas.sort()
print(bicicletas)

# sorted()

carros = ['bmw','audi','toyota','subaru']

print(carros)
print(sorted(carros))

# imprimindo lista em ordem inversa

print(carros)
carros.reverse()
print(carros)

#tamanho da lista

print(len(carros))

#
