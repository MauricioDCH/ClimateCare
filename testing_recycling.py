import re
import os
import random
import numpy as np
import pandas as pd
from PIL import Image
# from time import sleep
import time
import tensorflow as tf
from tensorflow import keras
import keras.applications.xception as xception
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Desactiva warnings de tensorflow por GPU
import sys

json_config_file = sys.argv[1]
weights_path = sys.argv[2]
file_path = sys.argv[3]

# print(json_config_file)

# with open('C:/Users/MDCH/Documents/00._Importantes_desde_15.12.2022/01. Universidad/01. Materias/PI1/2023/Proyecto/IA/model_config.json') as json_file:
with open(json_config_file) as json_file:
  json_config = json_file.read()
  
model = keras.models.model_from_json(json_config)
# model.load_weights('C:/Users/MDCH/Documents/00._Importantes_desde_15.12.2022/01. Universidad/01. Materias/PI1/2023/Proyecto/IA/recycling_xception_transferlearning.h5')
model.load_weights(weights_path)

base_path = 'C:/Users/MDCH/Documents/00._Importantes_desde_15.12.2022/01. Universidad/01. Materias/PI1/2023/Proyecto/IA/garbage_classificationCompleta/'

categories = {0: 'paper',       1: 'cardboard',     2: 'plastic', 
              3: 'metal',       4: 'trash',         5: 'battery',
              6: 'shoes',       7: 'clothes',       8: 'green-glass',
              9: 'brown-glass', 10: 'white-glass',  11: 'biological'}

# Añade el prefijo del nombre de la clase al nombre del archivo. Así por ejemplo "/papel104.jpg" se convierte en "papel/papel104.jpg
def add_class_name_prefix(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: x[:re.search("\d",x).start()] + '/' + x)
    return df

# Lista con todos los nombres de archivos del conjunto de datos
filenames_list = []

# Lista para almacenar la categoría correspondiente, tenga en cuenta que cada carpeta del conjunto de datos tiene una clase de datos
categories_list = []

for category in categories:
    filenames       = os.listdir(base_path  + categories[category])
    filenames_list  = filenames_list        + filenames
    categories_list = categories_list       + [category] * len(filenames)
    
df = pd.DataFrame({'Nombre de Imagen': filenames_list, 'N° de Categoría': categories_list})

df = add_class_name_prefix(df, 'Nombre de Imagen')

# Shuffle the dataframe
df = df.sample(frac=1).reset_index(drop=True)

# Ver imagen de ejemplo, puede ejecutar la misma celda de nuevo para obtener una imagen diferente
random_row  = random.randint(0, len(df) - 1)
sample      = df.iloc[random_row]
# randomimage = Image.open(base_path + sample['Nombre de Imagen'])
randomimage = Image.open(file_path)
randomimage.show()

# file_path   = base_path + sample['Nombre de Imagen']
image       = tf.keras.preprocessing.image.load_img(file_path, target_size=(320, 320, 3))
input_arr   = tf.keras.preprocessing.image.img_to_array(image)
input_arr   = np.array([input_arr]) # Convert single image to a batch

categories = ['baterías',           'biológicos',   'vidrio café',
              'cartón',             'vestimentas',  'vidrio verde', 
              'metal',              'papel',        'plástico', 
              'tenis o zapatos',    'basura común', 'vidrio blanco o transparente']

# Obtener las probabilidades de las categorías
probs = model.predict(input_arr)[0]

# Obtener la posición de la categoría con mayor probabilidad
pos = np.argmax(probs)

# Obtener el nombre de la categoría correspondiente
category = categories[pos]
# Imprimir el resultado
print('\n#########################################################')
print(f'La basura es {category} con una probabilidad del {probs[pos]*100:.2f}%')
print('#########################################################')