import socket

#domain:5001

# Subject info
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET = IPv4 / SOCK_STREAM = TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #setsockopt = Set Socket Options / SOL = Socket level / SO_REUSEADDR = Reuse socket
server_socket.bind(('localhost', 5001)) #Domain / Port(socket)
server_socket.listen() #Begin listening for connections

while True:
    print('Before .accept()')
    client_socket, addr = server_socket.accept() # .accept() - check for connections
    print('Connection from', addr)               # if yes --> (client socket, address)

    while True:
        print('Before .recv()')            # .recv() is blocking process
        request = client_socket.recv(4096) # .recv(i) - wait for request
                                           # i - size of req buffer
        print(request)
        if not request:
            break
        else:
            response = 'Hello world\n'.encode() # .encode() - str --> bytes
            client_socket.send(response) # Server answer to clients request

    print('Outside inner while loop')
    client_socket.close()