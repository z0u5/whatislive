import socket

host = socket.gethostbyname(socket.gethostname())

s = socket.socket()
s.bind((host,5000))
s.listen(10)
con, addr = s.accept()
con.send("666 is good")
s.close()
