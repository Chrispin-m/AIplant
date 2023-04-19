import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from io import BytesIO
from PIL import Image


def preprocess_image(image):
    # Resize the image to 256x256 pixels
    image = Image.open(image)
    image = image.resize((224, 224))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize the pixel values
    image_array = image_array / 255.0


    # Add an extra dimension to the array
    image_array = np.expand_dims(image_array, axis=0)

    return image_array
def predict(img):
    imag= preprocess_image(img)
    # Load the trained model
    model = keras.models.load_model('maize_leaf_disease_classifier.h5')
    # Load an image to make predictions on
    img_array = imag
    # Use the model to make predictions on the image
    predictions = model.predict(img_array)
    print(predictions)
    # Get the class with the highest prediction probability
    predicted_class = max(predictions[0])
    numclass = list(predictions[0]).index(predicted_class)
    if numclass == 0:
        numclass = 2
    print(numclass)
    # Get the name of the class
    class_names = { "1": "Blight", "2": "Cercospora", "3": "Cercospora leaf spot", "4": "Common rust", "5": "Common smut", "6": "Downy Mildew disease", "7": "Fallarmyworm", "8": "Giberrella ear rot", "9": "healthy", "10": "herbicideburn", "11": "Northern Leaf Blight", "12": "rust", "13": "zincdeficiency",}

    # Print the prediction result
    print("The plant is predicted to have the decease:", class_names[str(numclass)])
    return class_names[str(numclass)]
