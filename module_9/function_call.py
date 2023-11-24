
# import tensorflow as tf

from io import BytesIO
from urllib import request
import numpy as np
import logging
import json
from PIL import Image


import tflite_runtime.interpreter as tflite

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

interpreter = tflite.Interpreter(model_path="bees-wasps-v2.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Print input and output indices
input_index = input_details[0]['index']
output_index = output_details[0]['index']

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img
# Load the model

def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(150, 150))

    x = np.array(img)
    X = np.array([x],dtype=np.float32)*1/255

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    return preds[0][0]


def lambda_handler(event,context):
    url=event['url']
    pred=predict(url)
    return pred