from ISR.models import RDN
from PIL import Image
import numpy as np
import os
import time
from app import rdn



def transform(image_name):
    print(image_name)
    file_name = os.path.join(os.path.dirname(__file__), f'images/{image_name}')
    print(file_name)
    img = Image.open(file_name)
    lr_img = np.array(img)
    sr_img = rdn.predict(lr_img)
    result = Image.fromarray(sr_img)
    output_name = os.path.join(os.path.dirname(__file__), f'upscale_images/transformed_{image_name}')
    result.save(output_name)
    with open(output_name, 'rb') as f:
        return f.read()
