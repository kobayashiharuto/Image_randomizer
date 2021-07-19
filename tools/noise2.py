from scipy import ndimage as ndi
import cv2 as cv
from skimage.transform import ProjectiveTransform
from PIL import Image
import numpy as np
from skimage.transform import warp
from skimage import data
import matplotlib.pyplot as plt
import numpy as np


def noiser(size, image):
    # Simulate deformation field
    N = 500
    sh = (N, N)
    t = np.random.normal(size=sh)
    dx = ndi.gaussian_filter(t, 80, order=(0, 1))
    dy = ndi.gaussian_filter(t, 80, order=(1, 0))
    dx *= 50/dx.max()
    dy *= 50/dy.max()

    image = image.resize((500, 500))
    image = np.array(image).astype(np.float64) / 255

    yy, xx = np.indices(sh)
    xmap = (xx-dx).astype(np.float32)
    ymap = (yy-dy).astype(np.float32)
    warped = cv.remap(image, xmap, ymap, cv.INTER_LINEAR)
    im = Image.fromarray((warped * 255).astype(np.uint8)).resize((size, size))
    return im


image = Image.open('target/0_0.png')
for i in range(1, 100):
    new_image = noiser(28, image)
    new_image.save(f'out/test/rand_{i}.png')
