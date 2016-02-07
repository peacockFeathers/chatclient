from socket import * # for socket API
import sys # for parsing command-line arguments

def initiate_contact(server_name, server_port):
    chat_socket = socket(AF_INET, SOCK_STREAM)
    chat_socket.connect((server_name, server_port))
    return chat_socket
    
def send_message(handle):
    # http://nedbatchelder.com/text/unipain.html
    # In Python3, Unicode issues necessitate the use of encode() and decode().
    sentence = ('From ' + handle + ': ' + input('Input message:')).encode() #raw_input() was replaced by input() in 3, too.
    client_socket.send(sentence)
    print('Waiting for reply from server...')

def receive_message():
    modified_sentence = client_socket.recv(1024)
    print('From Server:', modified_sentence.decode())

if __name__ == '__main__':
    server_name = '127.0.0.1'
    server_port = 1888
    
    if len(sys.argv) == 3:
        #sys.argv[0] is the name of our program
        server_name = sys.argv[1]
        server_port = int(sys.argv[2]) # we're bringing this in as a string, so we have to typecast it
    
    client_socket = initiate_contact(server_name, server_port)
    
    #prompt for handle after we've established the connection, otherwise we're wasting our user's time if the connection fails
    handle = input('Handle for future messages:')
    while 1:
        send_message(handle)
        receive_message()
