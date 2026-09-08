from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np

from ride_duration_mlops.model import RideDurationModel


ROOT_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = ROOT_DIR / "models"
MODEL_PATH = MODEL_DIR / "ride_duration_model.joblib"


def create_training_data() -> tuple[np.ndarray, np.ndarray]:
    """Create a small deterministic dataset for the project."""
    X = np.array(
        [
            [1.0, 1],
            [2.0, 1],
            [3.0, 1],
            [5.0, 1],
            [7.0, 1],
            [10.0, 1],
            [1.0, 2],
            [3.0, 2],
            [5.0, 2],
            [7.0, 2],
            [10.0, 2],
            [15.0, 2],
        ]
    )

    y = np.array(
        [
            6.0,
            9.0,
            12.0,
            18.0,
            24.0,
            33.0,
            8.0,
            14.0,
            20.0,
            27.0,
            36.0,
            51.0,
        ]
    )

    return X, y


def train_model() -> RideDurationModel:
    """Train and save the ride duration model."""
    X, y = create_training_data()

    model = RideDurationModel(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X, y)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")

    return model


if __name__ == "__main__":
    train_model()