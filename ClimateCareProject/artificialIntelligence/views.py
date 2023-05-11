import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from django.conf import settings
from django.shortcuts import render
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Desactiva warnings de tensorflow por GPU
from keras.models import model_from_json
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def garbageClassification(request):
    json_config_file =os.path.join(settings.STATICFILES_DIRS[0], 'model_config_Final.json')
    weights_path = os.path.join(settings.STATICFILES_DIRS[0], 'recycling_xception_transferlearning_Final.h5')

    with open(json_config_file) as json_file:
        json_config = json_file.read()
        
    model = keras.models.model_from_json(json_config)
    model.load_weights(weights_path)

    if request.method == 'POST':
        handle_uploaded_file(request.FILES['sentFile'])

        image = tf.keras.preprocessing.image.load_img('static/test.jpg', target_size=(320,320,3))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])

        categories =['baterías',           'biológicos',   'vidrio café',
                    'cartón',             'vestimentas',  'vidrio verde', 
                    'metal',              'papel',        'plástico', 
                    'tenis o zapatos',    'basura común', 'vidrio blanco o transparente']
        
        probs = model.predict(input_arr)[0]
        pos = np.argmax(probs)
        category = categories[pos]
        caption = f'La imagen que subiste es de la categoría: {category}, y tiene una probabilidad del {probs[pos]*100:.2f}% de que lo sea.'
        return render(request, 'garbageClassificationOutput.html', {'caption': caption})
    else:
        return render(request, 'garbageClassificationInput.html')

def handle_uploaded_file(file):
    with open('static/test.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)