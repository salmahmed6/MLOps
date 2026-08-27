from abc import ABC, abstractmethod
from typing import Any


class ModelBase(ABC):
    """Base interface for ML models."""

    @abstractmethod
    def predict(self, X: list[float]) -> float:
        """Return a prediction for the given features."""
        ...


class RideDurationModel(ModelBase):
    """Model wrapper for ride-duration prediction."""

    def __init__(self, model: Any = None):
        self._model = model

    def predict(self, X: list[float]) -> float:
        if self._model is None:
            raise RuntimeError("Model is not loaded")

        prediction = self._model.predict([X])

        return float(prediction[0])