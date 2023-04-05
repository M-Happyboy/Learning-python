import network
import time
import socket 
wifi = 'Ming'
password = 'meetingkic'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(1)

def send_data(data):
    serverip = '172.20.10.2'
    port = 9000
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server: ', data_server )
    server.close()
    
send_data('Hello World')
