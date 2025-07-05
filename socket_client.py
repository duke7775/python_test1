#功能：客户端
import socket 

print("socket client")
is_created = True
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    is_created = False
    print(f"An error occurred: {e}")


# 建立连接:
is_connected = True
try:
    s.connect(('127.0.0.1', 9999))
except Exception as e:
    is_connected = False
    print(f"An error occurred while connecting: {e}")

if is_connected == True:
    # 接收消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()