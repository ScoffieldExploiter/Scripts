import socket # Lib usada para fazer a conexao
import platform # Lib usada para executar os comandos do atacante
import os # Lib usada para executar o backdoor em background

def calculadora(opcao,a,b):
  if opcao == "soma":
    c = a + b
    print("Soma de %.2f + %.2f: %.2f"  %(a,b,c))
  elif opcao == "sub":
    c = a - b
    print("Subtração de %.2f - %.2f: %.2f"  %(a,b,c))
  elif opcao == "div":
    c = a/b
    print("Divisão de %.2f / %.2f: %.2f"  %(a,b,c))
  elif opcao == "mult":
    c = a*b
    print("Multiplicação de %.2f * %.2f: %.2f" %(a,b,c))
  else:
    print("Opção Inválida")

opcão = input("Escolha uma opção(Soma,Sub,Div e Mult): ").lower()
numero = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

calculadora(opcão,numero,numero2)
