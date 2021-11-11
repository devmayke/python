import os 
import time

def gerarMatriz(tamanhoMatriz, posicaoColuna,  posicaoLinha):
  matriz = []
  linha = []
  linhaStatus = False
  for i in range(tamanhoMatriz + 1):
    if i == posicaoColuna - 1 :
      for j in range(tamanhoMatriz):
        if j == posicaoLinha - 1:
          linha.append("[X]")
          linhaStatus = True
        else:
          linha.append("[ ]")      
    else:
      if linhaStatus:
        matriz.append(linha)      
      matriz.append( ["[ ]"] * tamanhoMatriz ) 
      linhaStatus = False 
  return matriz


def mostrarMatriz(tamanhoMatriz, posicaoLinha, posicaoColuna):
  for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):   
      print(" ", gerarMatriz(tamanhoMatriz, posicaoLinha, posicaoColuna)[i][j], end="" )
    print('')

for i in range(11):
  mostrarMatriz(11,1,i+1)
  time.sleep(0.05)
  os.system('cls')










