import socketserver
import socket
import threading
class myServer(socketserver.TCPServer):
    # construter parameters (server_address, RequestHandlerClass, bind_and_activate=True)
    allow_reuse_address = True  # Allow the server to reuse the address
    def __init__(self,address,handler,active):
        super().__init__(address, handler, active)#This uses the internet TCP protocol, which provides for continuous streams of data between the client and server.

class reqHandler(socketserver.BaseRequestHandler):

    def handle(self) :# this process handles incoming request from clients
        connected = True
        while connected:
            msg_length =self.request.recv(256).decode("utf-8")
            if msg_length:
                msg_length=int(msg_length)
                string = str(self.request.recv(msg_length).decode("utf-8"))
                # Do service
                my_string=string[1:]
                if string[0].lower()  == 'w':#count the number of words
                    words_list = my_string.split()

                    # Count the number of words
                    server_msg = str(len(words_list))
                elif string[0].lower()  == 'l':#count the number of lower case letters
                    server_msg = str(sum(1 for char in my_string if char.islower()))

                elif string[0].lower() == 'r':#count number of numbers in a string
                    server_msg =str(sum(1 for char in my_string if char.isdigit()))
                elif string[0].lower() == 't':#count number of characters in a string
                    server_msg=str(len(my_string)+1)
                elif string[0].upper() == 'U':#count the number upper case letters
                    print(my_string)
                    server_msg =str(sum(1 for char in my_string if char.isupper()))

                else:
                    #the string didnot start with a specified letter
                    server_msg=str(string)
                server_msg_length=len(server_msg)
                server_msg_length_str = f"{server_msg_length: <{64}}".encode('utf-8')#send a 16 byte string to the client containg the length of the message

                self.request.sendall((server_msg_length_str))#here the server sends the answer to the client
                self.request.sendall(server_msg.encode('utf-8'))

                if server_msg=='good bye':
                    connected = False

        self.request.close()


#create server
port=5111
serv=socket.gethostbyname(socket.gethostname())
print(serv)
ADDRESS=(serv,port)
Server=myServer(ADDRESS,reqHandler,True)#initialize my server
try:
        print("Server is running...")
        Server.serve_forever()#start serving
except KeyboardInterrupt:
        print("Server is shutting down...")
        Server.shutdown()#close the server
        Server.server_close()
