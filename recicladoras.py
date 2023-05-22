recicladoras = {
    "Baterías":["Recopila","American in sap","Lito"],
    "Biológicos":["Emvarias","Centro de Acopio N° 1","Centro de Acopio N° 3"],
    "Vidrio café":["Intermediaria de reciclaje","Centro de Acopio N° 1","Reciclarte"],
    "Cartón":["Recickar Ecoplanet","Intermediaria de reciclaje","Centro de Acopio N° 1"],
    "Vestimentas":["Retos innovacion Medellin","Comfama","Riochevi."],
    "Vidrio verde":["Intermediaria de reciclaje","Centro de Acopio N° 1","Reciclarte"],
    "Metal":["Recickar Ecoplanet","Intermediaria de reciclaje","Centro de Acopio N° 1"],
    "Papel":["Recickar Ecoplanet","Centro de Acopio N° 1","Reciclar Ecoplanet"],
    "Plástico":["Recickar Ecoplanet","Intermediaria de reciclaje","Reciclarte"],
    "Tenis o zapatos":["Retos innovacion Medellin","Comfama","Riochevi."],
    "Basura común":["Emvarias","Centro de Acopio N° 1","Centro de Acopio N° 2"],
    "Vidrio blanco o transparente":["Intermediaria de reciclaje","Centro de Acopio N° 1","Emvarias"]
}

categories = ['baterías', 'biológicos', 'vidrio café', 'cartón', 'vestimentas', 'vidrio verde',
'metal', 'papel', 'plástico', 'tenis o zapatos', 'basura común', 'vidrio blanco o transparente']

pos = int(input("Ingrese la posición del elemento a buscar: "))
category = categories[pos]

listasEmpresas = []

if category == 'baterías':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'biológicos':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'vidrio café':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'cartón':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'vestimentas':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'vidrio verde':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'metal':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'papel':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'plástico':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'tenis o zapatos':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'basura común':
    listasEmpresas.extend(recicladoras[category.capitalize()])
elif category == 'vidrio blanco o transparente':
    listasEmpresas.extend(recicladoras[category.capitalize()])

print(listasEmpresas)