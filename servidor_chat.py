from http import client
import socket

#Criação da porta do chat
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))

#Escutar as conexões
servidor.listen() 
cliente, end = servidor.accept()

#Chat em loop infinito
finalizado = False

while not finalizado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'm@':
        finalizado = True 
    else:
        print(msg)
    cliente.send(input('Mensagem: ').encode('utf-8'))
    
cliente.close()
servidor.close()
            