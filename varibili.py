# variabili
# devono iniziare per a-z o A-Z o _
A2382 = "pippo"
art231 = "pippo2"
_var  = "pippo"

print(_var)
#non usare parole chiavi con if,else ,for, print
#quindi if= "ciao" ,non funziona
#convenzioni delle variabili
# le variabili per convenzione sono sempre composte da lettere maiscole, minuscole e underscore
variabile_uno = 1
#le classi sono espresse con lettere maiuscole  inizialei e in camelCase
#LaMiaClasse
#tipi di variabili
x = 10  #intero
y = 3.14  #float
nome = "Alice" #stringa
attivo = True #booleano
lista = [1,2,3,"ciao"] #lista
lista[3]=4
print(lista)
coordinate = (10 ,20) #non posso sovrrascrive come un array ,le coordinate 
coordinate = (30,10,20)# occoree sovrascrivere la dupla per modificare
coordinate[1]=30 

utente = {"nome ":"alice","età":35,"altezza":"170cm"}
print(utente["nome"])