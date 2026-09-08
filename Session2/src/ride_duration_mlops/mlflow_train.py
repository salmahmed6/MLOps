from __future__ import annotations

from pathlib import Path

import mlflow
import mlflow.sklearn
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from ride_duration_mlops.model import RideDurationModel
from ride_duration_mlops.train import create_training_data

ROOT_DIR = Path(__file__).resolve().parents[2]

MLFLOW_DB = ROOT_DIR / "mlflow.db"
MLFLOW_TRACKING_URI = f"sqlite:///{MLFLOW_DB}"

EXPERIMENT_NAME = "ride-duration-training"
MODEL_NAME = "RideDurationModel"


def train_and_log_run(
    n_estimators: int,
    random_state: int,
) -> float:
    """Train one model and log the run to MLflow."""

    X, y = create_training_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
    )

    model = RideDurationModel(
        n_estimators=n_estimators,
        random_state=random_state,
    )

    with mlflow.start_run() as run:
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)

        mlflow.log_params(
            {
                "n_estimators": n_estimators,
                "random_state": random_state,
            }
        )

        mlflow.log_metric("mae", mae)

        mlflow.sklearn.log_model(
            model.model,
            artifact_path="model",
            registered_model_name=MODEL_NAME,
        )

        print(f"Run ID: {run.info.run_id}")
        print(f"n_estimators: {n_estimators}")
        print(f"MAE: {mae:.4f}")

    return mae


def main() -> None:
    """Run three MLflow experiments."""

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    mlflow.set_experiment(EXPERIMENT_NAME)

    experiments = [
        {"n_estimators": 50, "random_state": 42},
        {"n_estimators": 100, "random_state": 42},
        {"n_estimators": 150, "random_state": 42},
    ]

    results: list[tuple[float, str]] = []

    for config in experiments:
        mae = train_and_log_run(
            n_estimators=config["n_estimators"],
            random_state=config["random_state"],
        )

        results.append((mae, f"n_estimators={config['n_estimators']}"))

    best_mae, best_config = min(results, key=lambda item: item[0])

    print("\nBest run:")
    print(f"{best_config}")
    print(f"MAE: {best_mae:.4f}")


if __name__ == "__main__":
    main()
