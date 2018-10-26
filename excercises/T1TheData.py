import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def get_data_matrix_and_set():
    samplesize = 30

    dataset = np.zeros((samplesize, 50, 50), dtype=np.uint8)

    for i in range(1, samplesize + 1):
        # with convert('L') we convert the images to grayscale
        img = Image.open('./fruits/%s.jpg' % (str(i))).convert('L')
        dataset[i - 1] = np.array(img, dtype=np.uint8)

    # Reshaping the images as vectors of length 2500 and store them in the rows of "datamatrix"
    datamatrix = np.reshape(dataset, (samplesize, -1))

    print("The shape of the datamatrix is", datamatrix.shape)

    return datamatrix, dataset


datamatrix, dataset = get_data_matrix_and_set()

fig, ax = plt.subplots(3, 2, figsize=(10, 10), gridspec_kw={'wspace': 0, 'hspace': 0})

for i in range(3):
    for j in range(2):
        ax[i, j].imshow(dataset[12 + i + j * 3], cmap='gray')
        ax[i, j].axis('off')
# plt.show()
