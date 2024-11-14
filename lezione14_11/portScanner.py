import socket as so 

target = input("inserisci l'inidirizzo da scansire: ")
portrange = input("inserisci porta minima\n e porta massima nel formato min-max es[5-200]")
lport = int(portrange.split('-')[0])
hport = int(portrange.split('-')[1])

print("scansione in corso da",target ,"dalla porta ",lport,"alla porta",hport)
chiuse = ""
for port in range(lport,hport+1):
    s=so.socket(so.AF_INET,so.SOCK_STREAM)
    status = s.connect_ex((target,port))
    
    if(status == 0 ):
        print('*** Port',port, '- APERTA ***')
    else:
        chiuse.append(port)
        
    if(len(chiuse)>0):
        yesno = input(f"trovate {len(chiuse)}aperte ,le vuoi visual (s/n)")
        if(yesno.lower().startswith("s")) :   
          print(f"porte chiuse :{chiuse}")
s.close()


