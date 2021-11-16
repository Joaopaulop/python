def ler_vetores(n):
  linha1 = input ("Vetor 1: ")
  itens1 = linha1.split()
  vetor1 = list(map(float, itens1))

  linha2 = input ("Vetor 2: ")
  itens2 = linha2.split()
  vetor2 = list(map(float, itens2))

  if (len(vetor1)==len(vetor2)): 
    print(vetor1[0:n])
    print(vetor2[0:n])
  else :
    print("Os vetores tem de possuir o mesmo número de elementos!")
  
  return vetor1, vetor2

def produto_escalar(u, v):
  soma = 0
  for i in range(len(u)):
    soma = soma + u[i]*v[i]
  return soma

n = int(input("Tamanho do vetor: "))
a, b = ler_vetores(n)
soma = produto_escalar(a, b)
print("Produto escalar: ", soma)