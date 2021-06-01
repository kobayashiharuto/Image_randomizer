from PIL import Image
from controller import randomized_image_generate


def main():
    image = Image.open('data/9_0.png')
    randmized_images = randomized_image_generate(image)

    for index, image in enumerate(randmized_images):
        image.save(f'out/9_{index}.png')


if __name__ == '__main__':
    main()
