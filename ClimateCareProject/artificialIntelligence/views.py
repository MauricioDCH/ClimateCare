from django.shortcuts import render
# from django.http import HttpResponse
from .models import matchingLearningModels
# import os
# import numpy as np
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# import json
# import tensorflow as tf
# from tensorflow import keras
# import sys

##############################################################
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

from keras.models import model_from_json

from keras.models import Sequential
from keras.layers import Dense, Activation, Lambda

##############################################################

# Create your views here.

def home(request):
    return render(request, 'homePage.html')

def garbageClassification(request):
    classification = matchingLearningModels.objects.filter(priority=1)[0]
    json_config_file = classification.architecture.path
    weights_path = classification.weights.path
    print(json_config_file)
    
    with open(json_config_file) as json_file:
        json_config = json_file.read()
        
    model = keras.models.model_from_json(json_config)
    # model.load_weights(weights_path)
    
    
    
    
    
    
    
    
    
    
    
    
    # petClassifierFiles = matchingLearningModels.objects.filter(priority=1)[0]
    # path_arch = petClassifierFiles.architecture.path
    # path_weights = petClassifierFiles.weights.path

    # with open(path_arch) as json_file:
    #     json_config = json_file.read()

    # model = tf.keras.models.model_from_json(json_config)
    # model.load_weights(path_weights)

    # if request.method == 'POST':
    #     handle_uploaded_file(request.FILES['sentFile'])

    #     image = tf.keras.preprocessing.image.load_img('static/test.jpg', target_size=(320,320,3))
    #     input_arr = tf.keras.preprocessing.image.img_to_array(image)
    #     input_arr = np.array([input_arr]) # Convert single image to a batch



    # garbageClassificationFiles = matchingLearningModels.objects.filter(priority=1)[0]
    # pathArchitecture = garbageClassificationFiles.architecture.path
    # pathWeights = garbageClassificationFiles.weights.path
    
    # with open(pathArchitecture) as json_file:
    #     json_config = json_file.read()
    
    # model = tf.keras.models.model_from_json(json_config)
    # model.load_weights(pathWeights)
    
    # categories = ['baterías',           'biológicos',   'vidrio café',
    #               'cartón',             'vestimentas',  'vidrio verde', 
    #               'metal',              'papel',        'plástico', 
    #               'tenis o zapatos',    'basura común', 'vidrio blanco o transparente']
    
    # if request.method == 'POST':
    #     handle_uploaded_file(request.FILES['sendFile'])
    #     image       = tf.keras.preprocessing.image.load_img('static/test.jpg', target_size=(320, 320, 3))
    #     input_arr   = tf.keras.preprocessing.image.img_to_array(image)
    #     probs = model.predict(input_arr)[0]
    #     pos = np.argmax(probs)
    #     category = categories[pos]
    # #     caption = f'La basura es {category} con una probabilidad del {probs[pos]*100:.2f}%'
    # # return render(request, 'garbageClassification.html', {'caption': caption})
    return render(request, 'garbageClassification.html')

def handle_uploaded_file(file):
    with open('static/test.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)