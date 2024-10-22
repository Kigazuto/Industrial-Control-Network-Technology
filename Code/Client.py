import socket
# 获取匹配开头字符串的所有属性值
def getConstants(prefix):
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }


ipproto_str = getConstants("IPPROTO_")
family_str = getConstants("AF_")
type_str = getConstants("SOCK_")

sock = socket.create_connection(('127.0.0.1', 7897))
print(ipproto_str[sock.proto])
print(family_str[sock.family])
print(type_str[sock.type])

try:
    msg = b"Are you there?"
    sock.sendall(msg)
    data = sock.recv(1024)
    print(data.decode())
finally:
    sock.close()
