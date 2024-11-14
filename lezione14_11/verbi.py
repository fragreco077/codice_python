import http.client
#from urlib.parse import urlparse
host = input("Inserisci host/Ip del sitema target:")
port = input("Insert la porta del sistema target (default:80): ")
path = input("inserisci il percorso (default:'/')")

if(port == ""):port = 80
if(path==""):path = '/'
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS','/')
    response = connection.getresponse()
    if(response.status>=200 and response.status<=299 and response.getheader("Allow")!=None):
      print("I metodi abilitati sono : ",response.getheader("Allow"))
    else:
       print("usa un metodo alternativo",response.status,"\n")  
    connection.close()   
except ConnectionError:
    print("connessione fallita",ConnectionError.strerror)    


