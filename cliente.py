import socket

host , port = 'localhost',8080
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect((host,port))

cmd = 'GET http://localhost:8080 HTTP/1.1\r\n\r\n'.encode()
cliSock.send(cmd)
imagen = b""
while True:
    datos = cliSock.recv(5120)
    if( len(datos) < 1):
        break 
    imagen = imagen + datos
cliSock.close()
print(imagen.decode('utf-8'))
pos = imagen.find(b"\r\n\r\n")
print("HEADER")
#print(imagen[:pos].decode())

