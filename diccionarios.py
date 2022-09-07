#Los diccionarios son variables especiales que me permiten almacenar multiples datos de diferente tipo 
#en una sola variable. *Atributos* dentro del diccionario se pueden tener listas

empleado = {
    'nombre':"Juan",
    'cedula': 1128454583,
    'cargo':"Analista de datos",
    'salario':8000000,
    'horasTrabajadas':40,
    'aplicaSubsidioTransporte':False,
    'deudas':[1500000,800000]
}
#print(empleado)
#print(empleado['deudas'][1])

#RECORRIENDO UN DICCIONARIO: Atributos y valores
for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)