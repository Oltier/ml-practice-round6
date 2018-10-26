import warnings

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

warnings.filterwarnings("ignore")

from excercises.T1TheData import get_data_matrix_and_set
from excercises.T21PCA import compute_pca

datamatrix, dataset = get_data_matrix_and_set()

PCA, eigvalues = compute_pca(datamatrix / 255., 50)


def plot_error(eigvalues, max_d):
    x = range(1, max_d + 1)
    errors = [sum(eigvalues[d:]) for d in x]
    plt.plot(x, errors)
    plt.xlabel('Number of principal components $d$')
    plt.ylabel('Reconstruction error $\mathcal{E}$')
    plt.title('Number of principal components vs the reconstruction error')
    plt.show()


# plot the number of principal components vs the reconstruction error
plot_error(eigvalues, 30)


def plot_princ_comp(PCA):
    fig, ax = plt.subplots(1, 5, figsize=(15, 15))
    # select the principal components we are plotting
    # You can change these to see what other components look like
    plot_pd = [0, 4, 9, 14, 19]

    for i in range(len(plot_pd)):
        ax[i].imshow(np.reshape(PCA[plot_pd[i]] * 255, (50, 50)), cmap='gray')
        ax[i].set_title("Principal Direction %d" % (plot_pd[i] + 1))
    plt.show()


# plot_princ_comp(PCA)
#
#
# ### Input:
# ##  X: Dataset
# ##  d: number of dimensions
# ##  n_pics: number of pics per class (Apple, Banana). Min 1, Max 15
# def plot_reconstruct(X, d, n_pics=5):
#     # x=w*z
#     X_pca = np.matmul(PCA[:d, :], X[:, :, None])
#     # x_reversed=r*x
#     X_reversed = np.matmul(PCA[:d, :].T, X_pca)[:, :, 0]
#
#     # Setup Figure size that scales with number of images
#     fig = plt.figure(figsize=(4, max(8 * np.log(n_pics), 5)))
#
#     # Setup a (n_pics,2) grid of plots (images)
#     gs = gridspec.GridSpec(n_pics, 2)
#     gs.update(wspace=0.0, hspace=0.0)
#     for i in range(n_pics):
#         for j in range(0, 2):
#             # Add a new subplot
#             ax = plt.subplot(gs[i, j])
#
#             # Insert image data into the subplot
#             ax.imshow(np.reshape(X_reversed[i + (15 * j)], (50, 50)), cmap='gray', interpolation='nearest')
#
#             # Remove x- and y-axis from each plot
#             ax.set_axis_off()
#
#     # Setup a visual divider between Apples and Bananas (i.e. a black line between plots)
#     transFigure = fig.transFigure.inverted()
#     column_divider = Line2D((0.5, 0.5), (0.13, 0.91), color='black', transform=fig.transFigure)
#     fig.lines.extend([column_divider])
#
#     # Setup column title for Apples and Bananas.
#     plt.subplot(gs[0, 0]).set_title('Apples', size='large', y=1.08)
#     plt.subplot(gs[0, 1]).set_title('Bananas', size='large', y=1.08)
#
#     # Render the plot
#     plt.show()
#
#
# num_com = [1, 5, 50]
# for d in num_com:
#     print("Reconstructed image using %d principal components:" % (d))
#     plot_reconstruct(datamatrix, d, n_pics=5)
