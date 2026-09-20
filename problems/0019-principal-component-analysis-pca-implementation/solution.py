import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    data_std = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    data_cov = np.cov(data_std.T)

    eig_val, eig_vec = np.linalg.eigh(data_cov)

    order = np.argsort(eig_val)[::-1]
    eig_vec = eig_vec[:, order]
    
    for i in range(eig_vec.shape[1]):
        vec = eig_vec[:,i]
        first_non_zero = np.argmax(np.abs(vec) > 1e-10)
        if vec[first_non_zero] < 0:
            eig_vec[:, i] = -vec

    p_components = eig_vec[:, :k]
    return np.round(p_components, 4)

