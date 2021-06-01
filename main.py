from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import noise
import stretch


np.set_printoptions(threshold=1000000)


def show_image(image):
    plt.imshow(image)
    plt.show()


def main():
    image = Image.open('data/9_0.png')
    image_resized = image.resize((28, 28))
    image_resized_gray = image_resized.convert('L')
    image_array = np.array(image_resized_gray)
    image__array_binary = ((image_array > 128) * 255).astype('u1')
    image_binary = Image.fromarray(image__array_binary)
    image_binary.save('out/binary.png')

    for i in range(10):
        image_randomized = noise.noise_image(image_binary)
        image_stretched = stretch.stretch(image_randomized, 0.7, 0.9)
        image_stretched.save(f'out/{i}.png')


if __name__ == '__main__':
    main()
