# Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

###
x[1][0] = 15
print(x)
###
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)
###
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)
###
z[0]['y'] = 30
print(z)

print('---------------')
# Iterar a través de una lista de diccionarios
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for x in range(len(list)):
        print(f"first_name - {estudiantes[x]['first_name']}, last_name - {estudiantes[x]['last_name']}")
        

iterateDictionary(estudiantes)

print('---------------')
# Obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

print('---------------')
# Iterar a través de un diccionarios con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    llaves = list(dict.keys())
    for x in range(len(dict)):
        print(f"{len(dict[str(llaves[x])])} {str(llaves[x]).upper()}")
        for i in range(len(dict[str(llaves[x])])):
            print(dict[str(llaves[x])][i])
        print("")

printInfo(dojo)

