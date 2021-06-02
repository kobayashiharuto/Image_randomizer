from PIL import Image
from controller import randomized_image_generate
import glob


def get_file_paths(path: str):
    files = glob.glob(path + '/*')
    return files


def main():
    paths = get_file_paths('data/origin_images')

    for path in paths:
        image = Image.open(path)
        randmized_images = randomized_image_generate(
            image, resize=200, count=5)

        name = path.split('\\')[-1].split('.')[0]
        for index, image in enumerate(randmized_images):
            image.save(f'out/train_data1/{name}_{index}.png')


if __name__ == '__main__':
    main()
