recomendaciones = {
    "Eficiencia energética en el hogar":
    [
        "Reduce el consumo de energía en el hogar",
        "Instala bombillas LED de bajo consumo.",
        "Utiliza electrodomésticos eficientes energéticamente"
        "Aprovecha la luz natural en lugar de encender luces durante el día.",
        "Ajusta la temperatura del termostato para reducir el uso de calefacción y aire acondicionado.",
        "Mejora el aislamiento de tu hogar.",
        "Utiliza el lavavajillas y la lavadora con carga completa.",
        "Desconecta los aparatos electrónicos cuando no los estés usando.",
    ],
    "Transporte sostenible":
    [
        "Conduce menos y utiliza el transporte público, camina o utiliza la bicicleta cuando sea posible.",
        "Comparte coche con otros para reducir el número de vehículos en la carretera.",
        "Elige vehículos con bajas emisiones de carbono, como los vehículos eléctricos.",
        "Mantén tu coche en buenas condiciones para que funcione de manera eficiente.",
        "Evita conducir a altas velocidades y acelerar y frenar bruscamente.",
        "Evita el uso de aviones para viajes cortos."
    ],
    "Reducción de desechos y reciclaje":
    [
        "Evita el uso de productos desechables y opta por alternativas reutilizables.",
        "Recicla tanto como sea posible.",
        "Reduce el consumo de papel.",
        "Utiliza bolsas reutilizables en lugar de bolsas de plástico desechables.",
        "Aprovecha el compostaje.",
        "Alimentación sostenible: 15. Reduce el consumo de carne y lácteos.",
        "Compra alimentos locales y de temporada.",
        "Evita el desperdicio de alimentos."
    ],
        "Consumo consciente":
    [
            "Apoya a empresas y marcas sostenibles.",
            "Compra productos usados o de segunda mano.",
            "Evita el uso de productos químicos dañinos en el hogar y el jardín.",
            "Reduce el consumo de productos empaquetados en plástico.",
    ],
    "Conservación del agua:":
    [ 
        "Ahorra agua reduciendo el tiempo de ducha y recogiendo agua de lluvia.",
        "Arregla las fugas de agua y utiliza sistemas eficientes en tu hogar.",
        "Evita el uso de agua embotellada y utiliza un filtro de agua.",
        "Utiliza electrodomésticos eficientes energéticamente.",
        "Utiliza el lavavajillas y la lavadora con carga completa.",
        "No utilices el inodoro como papelera.",
        "No dejes el grifo abierto mientras te lavas los dientes o te afeitas."
    ],
    "Protección del medio ambiente":
    [
        "Planta árboles en tu comunidad.",
        "Apoya la conservación de la energía en el trabajo.",
        "Participa en programas de reforestación.",
        "Utiliza sistemas de captación de agua de lluvia.",
        "Promueve la educación y sensibilización ambiental en tu comunidad.",
        "Participa en programas de reciclaje.",
        "Participa en programas de limpieza de playas y ríos.",
        "Participa en programas de conservación de la biodiversidad.",
        "Participa en programas de conservación de los océanos.",
        "Participa en programas de conservación de los bosques.",
        "Participa en programas de conservación de los humedales."
    ],
    "Reducción de emisiones en el hogar": 
    [
        "Reduce el consumo de energía en el hogar.",
        "Apaga completamente los dispositivos electrónicos.",
        "Desconecta los cargadores de dispositivos electrónicos cuando no los uses.",
        "Utiliza sistemas de energía renovable en el hogar, como paneles solares.",
        "Utiliza electrodomésticos eficientes energéticamente.",
        "Aprovecha la luz natural en lugar de encender luces durante el día."
    ],
    "Estilo de vida sostenible": 
    [
        "Evita el uso excesivo de aire acondicionado y calefacción.",
        "Evita el uso de aerosoles.",
        "Reduce el consumo de agua embotellada.",
        "Minimiza el uso de aparatos de climatización y utiliza métodos naturales para mantener frescos o cálidos los espacios.",
        "Promueve el teletrabajo siempre que sea posible."
    ],
    "Gestión adecuada de residuos":
    [
        "Recupera y reutiliza el agua en el hogar.",
        "Participa en programas de intercambio y donación de ropa y otros artículos.",
        "Evita el despilfarro de alimentos.",
        "Utiliza papel reciclado y configura la impresora para imprimir a doble cara.",
        "Recicla y desecha correctamente los productos electrónicos y otros residuos peligrosos.",
        "Recicla y desecha correctamente los residuos orgánicos."
    ],
    "Promoción de prácticas sostenibles":
    [
        "Infórmate sobre el impacto ambiental de las empresas y marcas antes de realizar compras.",
        "Apoya iniciativas de conservación marina y evita el consumo de productos marinos en peligro de extinción o capturados de manera insostenible.",
        "Apoya la investigación y desarrollo de tecnologías limpias y sostenibles.",
        "Únete a grupos comunitarios y organizaciones medioambientales para trabajar en proyectos de acción climática y sensibilización."
    ],
    "Educación y concienciación":
    [
        "Educa a otros sobre la importancia de la reducción de la huella de carbono.",
        "Comparte información y recursos sobre prácticas sostenibles en tu comunidad.",
        "Participa en eventos y actividades relacionadas con el medio ambiente.",
        "Promueve la educación ambiental en escuelas y comunidades."
    ],
    "Energía renovable y eficiencia energética":[
        "Utiliza sistemas de energía renovable en el hogar, como paneles solares.",
        "Utiliza sistemas de energía solar pasiva.",
        "Utiliza sistemas de captación de agua de lluvia.",
        "Utiliza electrodomésticos eficientes energéticamente."
    ],
    "Movilización y acción colectiva": [
        "Únete a grupos de acción climática y sostenibilidad en tu comunidad.",
        "Participa en manifestaciones y actividades relacionadas con el cambio climático.",
        "Apoya políticas y medidas que promuevan una transición hacia una economía baja en carbono.",
        "Vota por líderes y políticas que respalden la sostenibilidad y la reducción de emisiones."
    ]
}


import random

# Concatenar todas las listas de recomendaciones en una lista única
recomendaciones_totales = [recomendacion for lista in recomendaciones.values() for recomendacion in lista]

# Verificar si el total de recomendaciones es mayor a 25
if len(recomendaciones_totales) > 25:
    recomendaciones_totales = random.sample(recomendaciones_totales, 25)

# print(recomendaciones_totales)


for value in recomendaciones_totales:
    print(value)