#功能：服务端

import socket
import threading


print("socket server")

is_created = True
is_bind = True
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    is_created = False
    print(f"An error occurred: {e}")

if is_created == True:
    
    try:
        s.bind(('127.0.0.1',9999))
        s.listen(5)
    except Exception as e:
        is_bind = False
        print(f"Bind or listen failed: {e}")

print('Waiting for connection...')

def tcplink(new_socket, addr):
    is_connected = True
    print('Accept new connection from %s:%s...' % addr)
    new_socket.send(b'Welcome!')
    while True:
        data = new_socket.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        new_socket.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    new_socket.close()
    print('Connection from %s:%s closed.' % addr)

if is_created and is_bind:
    try:
        while True:
            print('开始accept')

            # 接受一个新连接:
            new_socket, addr = s.accept()
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=tcplink, args=(new_socket, addr))
            t.start()
    except Exception as e:
        print(f"An error occurred: {e}")
