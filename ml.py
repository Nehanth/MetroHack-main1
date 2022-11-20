import coremltools as ct
import PIL
import cv2
import numpy as np

from PIL import Image

def prediction(uf):
    image_input = ct.ImageType(name="image", shape=(1, 299, 299, 3,),)

    img = uf

    model = ct.models.MLModel('right.mlmodel')
    #example_image = Image.open(img).resize((299, 299))
    try:
        example_image = Image.open(img)
    except:
        print('error')


    try:
        example_image_RGB = example_image.convert("RGB")
    except:
        print('error')


    try:
        prediction = model.predict({'image':example_image_RGB})
        healthissue = prediction["classLabel"]
    except:
        print('error')


    try:
        a = 0;

        if healthissue == '1 - right':
            print('1')
            a = 1
        elif healthissue == '2 - right':
            print('2')
            a = 2
        elif healthissue == '3 - right':
            print('3')
            a = 3
        elif healthissue == '4 - right':
            print('4')
            a = 4
        elif healthissue == '5 - right':
            print('5')
            a = 5

        return a
    except:
        print('error')
