import requests
import json
import numpy as np

url = "https://api.covid19api.com/country/brazil/status/deaths/live?from=2020-12-05T00:00:00Z&to=2021-05-05T00:00:00Z "


response = requests.get(url)
storage = response.json()


#414399-401186

##for sublista in storage:
##    print(sublista['Cases'][-1::7])
lst = []
for sublista in storage[-1:0:-6]:
    casos = sublista['Cases']
    lst.append(casos)  
for i in range(len(lst[0:2])):
    y = ((lst[i]-lst[i+1])/7)
    print(y)





#sublista = storage[-1:0:-6]
#lst = []
#for i in sublista:
#    casos = i['Cases']    
#    x = casos
#    lst.append(x)
#    for j in range(len(lst)):
#        print(lst[j:j+2])
#
        




    



#####for sublista in storage:
#####    casos = sublista['Cases']
#####    for casos in sublista:
#####        numDeMortes = sublista['Cases']
#####        x = sum(numDeMortes for data in sublista)        
#####        print(x)
##for sublista in storage:
##    pais = sublista['Country']
##    numeroDeMortesConfirmadas = sublista['Deaths']
##    print(pais + " tem " + str(numeroDeMortesConfirmadas))
####total = 0
####for sublista in storage:
####    data = sublista['Date']
####    if data == data:
####        total += sublista['Deaths']
####        print(total)


##total = 0
##for sublista in storage:
##    pais = sublista['Country']
##    if(pais == "Brazil"):
##        total += sublista['Deaths']
##    print("Numero total de mortes confirmados no Brasil: " + str(total))
    

## esse ta dando certo ##
###for i in range(len(storage)):
###    j = ['Cases']
#####    for j in range(len(storage[i])):
###    x = (j['Cases'] for j in storage[-1::7])
###    print(x)
        
###        
###for i in range(len(storage)):
###    x = sum(j['Deaths'] for j in storage [0:7])
###    print(x)
###        
###        
        
        
        
#    x = sum(j['Deaths'] for j in storage[i:i+6])
#print(storage[0]['Deaths'])




#print [sum(item['Deaths'][i:i+7]) for item in range(0, len(storage), 6)]
#print(x)


    
    
    
##    mortes = (storage[i]['Deaths'])
##    x = sum(j['Deaths']) for j in storage[i:i+6])
##    print(x)

##for i in range(len(storage)):
##    for j in range(len(storage[i])):
##        print(storage[i][j])


#    mortes = (storage[i]['Deaths'])
#    print(sum(mortes[i:i+5]) for mortes in range(0, len(storage), 5))
#    x = sum(j['Deaths'] for j in storage[i:i+6])
#    y = x/7
#    print(x)

##for i in range(len(storage)-1):
##    mortes = (storage[i]['Deaths'])
###    x = sum(mortes for mortes in storage[i:i+6])
##    print(sum(mortes for i in range(len(storage)) [0:6 7]))

#for i in range(len(storage)-1):
#    mortes = (storage[i]['Deaths'])
##lista = (52246,46612,20711)
#

#lista4 = (18429,5324,5990,14491,7018,5634,25901)
#c = sum(lista4)
#print(c)

#a = sum(lista1)
#b = sum(lista2)
#c = sum(lista3)
#print(a)

##############
#teste de validacao de dados
###print(storage[0]['Deaths'])
###print(storage[1]['Deaths'])
###print(storage[2]['Deaths'])
###print(storage[3]['Deaths'])
###print(storage[4]['Deaths'])
###print(storage[5]['Deaths'])
###print(storage[6]['Deaths'])
###lista = (4588,10209,27441,9946,5448,991,1976)
###print sum(lista)


###############
#teste de tipos e separar os valores
#storage[0]['Deaths']

#print(type(storage))
#print(len(storage))
#print(storage[0])
#print(type(storage[0]))
#print(storage[0]['Deaths'])
#print(type(storage[0]['Deaths']))
#print(storage[0]['Deaths'])
#print(type(storage[0]['Deaths']))
#print(storage[0]['Deaths'])
#for item in range(len(storage)):
#    mortes = (storage[item]['Deaths'])
#    res = [int(x) for x in str(mortes)]
#    dicionario = dict.fromkeys(res,"number")
#    print(mortes[0])