import operator
import stats

diccionario={"madrid":12.5,"sevilla":24.9,"lugo":8.75,"valencia":25.8,"córdoba":31.8}
print(diccionario.items())

diccionariomed=stats.mean(diccionario.values())
print(diccionariomed)

diccionario["zaragoza"]=20.7
print(diccionario.items())
diccionario.pop("lugo")
print(diccionario.items())

diccionariomed=stats.mean(diccionario.values())
print(diccionariomed)

sortedDict = sorted(diccionario.items(), key=operator.itemgetter(1),reverse=True)
print(sortedDict)