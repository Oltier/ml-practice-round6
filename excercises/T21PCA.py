def compute_pca(Z, d):
    # Input: the N by D data matrix Z, the number of components d
    # Output: a d by D matrix W_pca, and all eigenvalues of Q

    ### STUDENT TASK ###

    # step1: compute the sample cov. matrix Q
    # YOUR CODE HERE
    raise NotImplementedError()

    #step2: compute the eigenvalues and eigenvectors (see introduction notebook)
    # YOUR CODE HERE
    raise NotImplementedError()

    #step3: Sort the eigenvectors by decreasing eigenvalues, choose the d largest eigenvalues, form W_pca
    # YOUR CODE HERE
    raise NotImplementedError()

    return W_pca.real,eigvalues