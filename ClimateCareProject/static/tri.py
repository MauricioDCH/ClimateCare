import tensorflow as tf
model = tf.keras.models.load_model('static/model_config.json')
print(model.summary())
