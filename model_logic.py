import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the brain once when the script starts
MODEL_PATH = 'model/cat_dog_classifier.keras'
model = tf.keras.models.load_model(MODEL_PATH)

def process_and_predict(image_file):
    """
    Modular function to handle image processing and prediction
    """
    #Resize to match our training (150x150)
    img = load_img(image_file, target_size=(150, 150))
    #Convert to numbers
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) # Make it a "Batch of 1"
    #Ask the Brain
    prediction = model.predict(img_array)
    #Interpret the result
    if prediction[0] > 0.5:
        label = "DOG"
        confidence = float(prediction[0][0])
    else:
        label = "CAT"
        confidence = float(1 - prediction[0][0])
        
    return label, confidence
