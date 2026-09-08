from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.ensemble import RandomForestRegressor


@dataclass
class RideDurationModel:
    """Random forest model for predicting ride duration."""

    n_estimators: int = 100
    random_state: int = 42

    def __post_init__(self) -> None:
        self.model = RandomForestRegressor(
            n_estimators=self.n_estimators,
            random_state=self.random_state,
        )

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """Train the model."""
        self.model.fit(X, y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict ride duration."""
        return self.model.predict(X)