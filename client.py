import socket
header=256
port=6000
SERVER=socket.gethostbyname(socket.gethostname())
ENCODING='utf-8'
Disconnect_msg="good bye kambora"
ADDRESS=(SERVER,port)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDRESS)#client tries to connect to server
def recieve():
    msg_len=client.recv(16).decode(ENCODING)
    msg_len= int(msg_len)
    msg=client.recv(msg_len).decode(ENCODING)
    return msg
def send(string):
    msg=string.encode(ENCODING)
    msg_length=len(msg)
    msg_length_str = f"{msg_length: <{header}}".encode(ENCODING)
    client.send(msg_length_str)
    client.send(msg)
    print(recieve())

send('r999lawdddaa 8nshuu')

send(Disconnect_msg)