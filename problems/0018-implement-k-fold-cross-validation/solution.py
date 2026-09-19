import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    samples = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(samples)
    train_test = []
    for i in range(k):
        first_fold_l = -(-n_samples // k)
        other_fold_l = n_samples // k

        test = list(samples[(i-1)*other_fold_l+first_fold_l:i*other_fold_l+first_fold_l])

        train = [x for x in samples if x not in test]
        train_test.append((train, test))
    return train_test
