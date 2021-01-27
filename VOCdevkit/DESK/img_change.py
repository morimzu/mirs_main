import random 
import numpy as np
import os
import glob
import skimage

def augmentation_rotation(img):
    r = np.random.rand(1)

    if r > 0.50:
        random_degree = random.uniform(-5, 5)
        img = skimage.transform.rotate(img, random_degree, resize=True, cval=0)

    return img

def augmentation_flip(img):
    r = np.random.rand(1)

    if r < 1/3:
        img = img[:, ::-1, :]
    elif r < 2/3:
        img = img[::-1, :, :]

    return img

def augmentation_noise(img):
    r = np.random.rand(1)

    if r < 0.15:
        img = skimage.util.random_noise(img, mode='localvar')
    elif r < 0.30:
        img = skimage.util.random_noise(img, mode='salt')
    elif r < 0.45:
        img = skimage.util.random_noise(img, mode='s&p')
    elif r < 0.60:
        img = skimage.util.random_noise(img, mode='speckle', var=0.01)
    elif r < 0.75:
        img = skimage.util.random_noise(img, mode='poisson')
    elif r < 0.95:
        img = skimage.util.random_noise(img, mode='gaussian', var=0.01)

    img = img * 255
    img = img.astype(np.uint8)

    return img

def augmentation(image_path=None, output_dirpath=None, n=100, output_prefix='deskImage'):

    img = skimage.io.imread(image_path)

    i = 299
    while i < n:
        i = i + 1

        img_ag = augmentation_rotation(img)
        img_ag = augmentation_flip(img_ag)
        img_ag = augmentation_noise(img_ag)

        new_file_path = os.path.join(output_dirpath, output_prefix + '_' + ('0000' + str(i))[-5:] + '.jpg')
        skimage.io.imsave(new_file_path, img_ag)

if __name__ == '__main__':
    images = glob.glob('./JPEGImages/*')
    print(images)
    for image in images:
        print(image)
        augmentation(image_path='./JPEGImages/'+ image, output_dirpath='./changedImages/')