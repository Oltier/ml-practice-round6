import matplotlib.pyplot as plt
import numpy as np

from excercises.T1TheData import get_data_matrix_and_set
from excercises.T21PCA import compute_pca


def plot_scatter(PCA, Z):
    # get x for d=2
    X_2d = np.matmul(PCA[:2, :], Z[:, :, None])[:, :, 0]

    plt.scatter(X_2d[:15, 0], X_2d[:15, 1], c='r', marker='o', label='Apple')
    plt.scatter(X_2d[15:, 0], X_2d[15:, 1], c='y', marker='^', label='Banana')
    plt.legend()
    plt.xlabel('First principal component')
    plt.ylabel('Second principal component')
    plt.show()


datamatrix, dataset = get_data_matrix_and_set()
PCA, eigvalues = compute_pca(datamatrix / 255., 50)

plot_scatter(PCA, datamatrix)
