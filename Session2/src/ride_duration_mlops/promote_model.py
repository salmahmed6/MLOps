from __future__ import annotations

from pathlib import Path

import mlflow
from mlflow import MlflowClient

ROOT_DIR = Path(__file__).resolve().parents[2]
MLFLOW_DB = ROOT_DIR / "mlflow.db"
MLFLOW_TRACKING_URI = f"sqlite:///{MLFLOW_DB}"

MODEL_NAME = "RideDurationModel"
BEST_VERSION = 1


def main() -> None:
    """Promote the best registered model version to Staging."""

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    client = MlflowClient()

    client.transition_model_version_stage(
        name=MODEL_NAME,
        version=BEST_VERSION,
        stage="Staging",
    )

    model_version = client.get_model_version(
        name=MODEL_NAME,
        version=BEST_VERSION,
    )

    print(f"Model: {model_version.name}")
    print(f"Version: {model_version.version}")
    print(f"Stage: {model_version.current_stage}")


if __name__ == "__main__":
    main()