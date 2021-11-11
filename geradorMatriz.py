def gerarMatriz(tamanhoMatriz, posicaoColuna,  posicaoLinha):
  matriz = []
  linha = []
  linhaStatus = False
  for i in range(tamanhoMatriz + 1):
    if i == posicaoColuna - 1 :
      for j in range(tamanhoMatriz):
        if j == posicaoLinha - 1:
          linha.append("1")
          linhaStatus = True
        else:
          linha.append("0")      
    else:
      if linhaStatus:
        matriz.append(linha)      
      matriz.append( ["0"] * tamanhoMatriz ) 
      linhaStatus = False 
  return matriz


def mostrarMatriz(tamanhoMatriz, posicaoLinha, posicaoColuna):
  for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):   
      print(" ", gerarMatriz(tamanhoMatriz, posicaoLinha, posicaoColuna)[i][j], end="" )
    print('')


mostrarMatriz(10, 7, 6)







