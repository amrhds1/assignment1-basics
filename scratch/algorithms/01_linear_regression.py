# %%
# Linear regression from scratch, fit by gradient descent.
#
# Goal: given X (n_samples, n_features) and y (n_samples,), learn weights w and
# bias b such that X @ w + b ~= y.
#
# TODO: implement `predict`
# TODO: implement `mse_loss`
# TODO: implement `fit` (gradient descent loop)

import numpy as np


def predict(X: np.ndarray, w: np.ndarray, b: float) -> np.ndarray:
    raise NotImplementedError


def mse_loss(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    raise NotImplementedError


def fit(X: np.ndarray, y: np.ndarray, lr: float = 0.01, n_steps: int = 1000):
    """Return (w, b) fit by gradient descent on MSE loss."""
    raise NotImplementedError


# %%
if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n_samples, n_features = 200, 3
    true_w = np.array([2.0, -1.0, 0.5])
    true_b = 4.0

    X = rng.normal(size=(n_samples, n_features))
    y = X @ true_w + true_b + rng.normal(scale=0.1, size=n_samples)

    w, b = fit(X, y)
    print("learned w:", w, "true w:", true_w)
    print("learned b:", b, "true b:", true_b)
