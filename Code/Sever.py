import socket

# 1.创建一个套接字，
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.使用bind()函数将套接字与服务器地址关联
sock.bind(('localhost', 7897))
# 3.调用listen()函数将套接字设置为服务器模式
sock.listen(1)

while True:
    # 4.调用accept()等待客户端的消息连接
    # 如果有客户端进行连接，那么accept()函数会返回一个打开的连接与客户端地址
    connection, client_address = sock.accept()
    print("连接客户端地址：", client_address)
    try:
        # 5.指明一个缓冲区，该缓冲区用来存放recv函数接收到的数据
        data = connection.recv(1024)
        print(data)
        if data:
            # 6.通过sendall()进行回传客户端数据。
            connection.sendall("已接受到数据".encode())
        else:
            print("客户端没有发送数据，不需要传送数据")
    finally:
        #7.需要使用close()进行关闭清理
        connection.close()
