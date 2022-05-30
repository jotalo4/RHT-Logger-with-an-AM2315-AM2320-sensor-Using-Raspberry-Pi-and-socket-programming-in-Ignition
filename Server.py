
# Python Socket Client Server
import socketserver
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.71.142.114', 8080))
server.listen(5)
while True:
    
    conn, addr = server.accept()
    print ('Got connection from', addr)
    
    output = 'Thank you for your connecting'
    conn.sendall(output.encode('utf-8'))
    conn.close()


#output = 'Thank you for connecting'
#c.sendall(output.encode('utf-8')) 

#receive.decode('utf_8')