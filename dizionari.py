dizionario = {"nome":"greta","cognome":"levi,","eta":23}
print(dizionario)
print(dizionario["nome"])
print(dizionario["cognome"])
print(dizionario["eta"])

dizionario["eta"]=24
print(dizionario)
del dizionario["eta"]
print(dizionario)
dizionario["eta"]=24
print(dizionario)
dizionario.pop("eta") #uguale deleta
print(dizionario)
print(dizionario.values())
print(dizionario.keys())