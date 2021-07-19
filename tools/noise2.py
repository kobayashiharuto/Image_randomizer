from skimage.transform import ProjectiveTransform
from PIL import Image
import numpy as np
from skimage.transform import warp
from skimage import data

image = Image.open('out/gene.png')
matrix = np.array([[1, 0, 0], [0, 1, -1000], [0, 0, 1]])
image = np.asanyarray(image)
warped = warp(image, matrix)
warped = warp(image, ProjectiveTransform(matrix=matrix))
im = Image.fromarray((warped * 255).astype(np.uint8))
im.show()
