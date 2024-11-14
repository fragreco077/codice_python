import socket as so #IMPORTATO LA LIBRERIA SOCKET

SRV_ADDR = "" #mac adress
SRV_PORT = 4444 #la porta da dove ascolta

s = so.socket(so.AF_INET, so.SOCK_STREAM) #La s diventa istanza di classe
s.bind((SRV_ADDR,SRV_PORT)) #abbiamo chiesto di riservare una porta
s.listen(1)
print("sto attendendo una connessione")
connection ,adress= s.accept()
print("ho stabilito una connessione con :", adress)
while True:
    connection.sendall(b"$")
    data = connection.recv(1024)
    if not data: break 
    connection.sendall(b"ho ricevuto il messaggio \n") #b perchè in binario
    print(data.decode('utf-8'))
connection.close()    