import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8888)) 

finalizado = False
print('Digite m@ para encerrar o chat')

while not finalizado:
    cliente.send(input('Mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'm@':
        finalizado = True
    else:
        print(msg)
        
cliente.close() 
        
            