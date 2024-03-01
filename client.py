import socket
import time

header=256
port=5111
SERVER=socket.gethostbyname(socket.gethostname())
ENCODING='utf-8'
Disconnect_msg="good bye"
ADDRESS=(SERVER,port)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDRESS)#client tries to connect to server
def recieve():
    msg_len=client.recv(64).decode(ENCODING)
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

send('Wpython Socket Server')
send('LpythonSocketServer')
send('UPYTHONSOCKETSERVER')
send('R1234567890')
send('TpythonSocketServer123')
send('pythonSocketServer123')
send(Disconnect_msg)
client.close()