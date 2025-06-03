import numpy as np
from fastapi import FastAPI, File, UploadFile
import uvicorn
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

app = FastAPI()

MODEL = tf.keras.models.load_model('../models/1')
CLASS_NAMES = [
                'Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold', 'Septoria Leaf Spot',
                'Two spotted spider mite', 'Target Spot', 'Yellow Leaf Curl Virus', 'Mosaic Virus',
                'Healthy'
               ]


@app.get('/hello')
async def hello():
    return 'Hello this is Fast API server'

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return  image

@app.post('/predict')
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image, 0)

    predictions = MODEL.predict(image_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)