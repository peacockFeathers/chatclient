from socket import *
import sys

def start_up(server_number):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('',server_port))
    server_socket.listen(1)
    print('The server is ready to receive.')
    connection_socket, addr = server_socket.accept()
    return connection_socket

def send_message(connection_socket):
    # http://nedbatchelder.com/text/unipain.html
    # In Python3, Unicode issues necessitate the use of encode() and decode().
    sentence = (input('Input message:')).encode() #raw_input() was replaced by input() in 3, too.
    connection_socket.send(sentence)

def receive_message(connection_socket):
    sentence = connection_socket.recv(1024)
    print(sentence.decode())

if __name__ == '__main__':
    server_port = 1888
    
    if len(sys.argv) == 2:
        #sys.argv[0] is the name of our program
        server_port = int(sys.argv[1]) # we're bringing this in as a string, so we have to typecast it

    my_socket = start_up(server_port)

    while 1:
        receive_message(my_socket)
        send_message(my_socket)
        
    my_socket.close()
