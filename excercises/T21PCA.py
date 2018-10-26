import numpy as np


def compute_pca(Z, d):
    # Input: the N by D data matrix Z, the number of components d
    # Output: a d by D matrix W_pca, and all eigenvalues of Q

    ### STUDENT TASK ###

    # step1: compute the sample cov. matrix Q
    # YOUR CODE HERE
    N = Z.shape[0]
    Q = Z.T.dot(Z) / N

    # step2: compute the eigenvalues and eigenvectors (see introduction notebook)
    # YOUR CODE HERE
    eigvalues, eigvectors = np.linalg.eig(Q)
    eigvalues = eigvalues.real
    eigvectors = eigvectors.real
    # step3: Sort the eigenvectors by decreasing eigenvalues, choose the d largest eigenvalues, form W_pca
    # YOUR CODE HERE
    idx = eigvalues.argsort()[::-1]
    eigvalues = eigvalues[idx]
    eigvectors = eigvectors[:, idx]
    W_pca = eigvectors[:, :d].T

    return W_pca, eigvalues
