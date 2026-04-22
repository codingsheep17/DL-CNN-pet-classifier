import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the brain once
MODEL_PATH = 'model/cat_dog_classifier.keras'
model = tf.keras.models.load_model(MODEL_PATH)

def process_and_predict(image_file):
    # 1. Resize
    img = load_img(image_file, target_size=(150, 150))
    
    # 2. Convert to numbers
    img_array = img_to_array(img)
    
    # 🌟 THE FIX: Normalization (Matches how the model was trained)
    img_array = img_array / 255.0 
    
    # 3. Expand dimensions
    img_array = np.expand_dims(img_array, axis=0) 
    
    # 4. Predict
    prediction = model.predict(img_array)
    
    # 5. Extract the single score
    # prediction[0][0] is the standard way to get the float value
    score = float(prediction[0][0])
    
    # 6. Interpret (Assuming 0 = Cat, 1 = Dog)
    if score > 0.5:
        label = "DOG"
        confidence = score
    else:
        label = "CAT"
        confidence = 1 - score
        
    return label, confidence
