from PIL import Image
import numpy as np


def binary_convert(image, resize, threshold):
    image_resized = image.resize((resize, resize))
    image_resized_gray = image_resized.convert('L')
    image_array = np.array(image_resized_gray)
    image__array_binary = ((image_array > threshold) * 255).astype('u1')
    image_binary = Image.fromarray(image__array_binary)
    return image_binary
