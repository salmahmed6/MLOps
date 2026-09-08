# MLOps Session 2 — Shipping to Production

This directory contains my notes, implementation, experiments, and project work for **Session 2** of the MLOps journey with the **MLOps MENA Community**.

The focus of this session is moving an ML project closer to production by adding experiment tracking, model management, data versioning, code-quality automation, infrastructure as code, CI/CD, and integration testing.

## Session Topics

- **MLflow** — experiment tracking, metrics, artifacts, model registry, and model lifecycle
- **Weights & Biases (W&B)** — cloud experiment tracking, artifacts, and hyperparameter sweeps
- **DVC** — dataset/model versioning and reproducible ML pipelines
- **Ruff, Black, and pre-commit** — code quality and automated checks
- **Terraform** — Infrastructure as Code
- **GitHub Actions** — CI/CD automation
- **Integration testing** — testing the complete API request/response flow

## Project

The practical project continues the **Ride Duration ML** project from Session 1.

The current project uses Python 3.11, scikit-learn, NumPy, pandas, Litestar, MLflow, Weights & Biases, DVC, boto3, pytest, Ruff, Black, and pre-commit.

```text
Session2/
├── models/
│   └── ride_duration_model.joblib
├── src/
│   └── ride_duration_mlops/
│       ├── __init__.py
│       ├── model.py
│       ├── train.py
│       ├── mlflow_train.py
│       └── promote_model.py
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yaml
├── dvc.yaml
├── dockerfile
├── pyproject.toml
└── README.md
```

The remaining Session 2 components will be added as they are implemented and validated.

## MLflow — Current Implementation

The first Session 2 requirement has been implemented with MLflow.

The training script creates the `ride-duration-training` experiment and executes three runs with different Random Forest configurations.

| Run | `n_estimators` | MAE | Registered Model |
|---|---:|---:|---|
| 1 | 50 | **3.8867** | `RideDurationModel` v1 ⭐ |
| 2 | 100 | 3.9767 | `RideDurationModel` v2 |
| 3 | 150 | 3.9822 | `RideDurationModel` v3 |

Each run records training parameters, MAE, a trained model artifact, and a registered model version.

The best result was **50 estimators with MAE 3.8867**. `RideDurationModel` version 1 was promoted to **Staging** in the MLflow Model Registry.

### Run the MLflow experiment

From the `Session2` directory with the virtual environment activated:

```bash
python -m ride_duration_mlops.mlflow_train
```

### Promote the best model

```bash
python -m ride_duration_mlops.promote_model
```

### Open the local MLflow UI

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000
```

Then open `http://127.0.0.1:5000` in a browser.

## Code Quality

The project is configured to use Ruff and Black with an 88-character line length. The MLflow implementation has been checked with Ruff and formatted with Black.

```bash
ruff check src/ride_duration_mlops/
black src/ride_duration_mlops/
```

The full pre-commit configuration will be completed as part of the code-quality requirement.

## Session 2 Roadmap

- [x] MLflow — 3 tracked runs, metrics, artifacts, model registration, and Staging promotion
- [ ] W&B — reproduce the experiment and compare MLflow vs W&B
- [ ] DVC — `prepare → train → evaluate` pipeline and remote storage
- [ ] Ruff + Black + pre-commit — complete repository-wide checks
- [ ] Terraform — provision the required infrastructure and capture the plan
- [ ] GitHub Actions — CI/CD pipeline for linting, tests, Docker build/push, and deployment workflow
- [ ] Integration tests — API success, health check, validation errors, and response schema

## Relation to Session 1

Session 2 builds on the Ride Duration service created in Session 1. The goal is to evolve the project from a working ML service into a more reproducible and production-oriented MLOps workflow.

```text
Session 1
    ↓
ML project + API + Docker + tests
    ↓
Session 2
    ↓
Experiment Tracking
    ↓
Data & Model Versioning
    ↓
Code Quality Automation
    ↓
Infrastructure as Code
    ↓
CI/CD
    ↓
Integration Testing
```

## References

- Session 2 notes: `../Notes/Session 2.excalidraw`
- Session 1 project: `../Session 1/`

## Learning Goal

The main goal of this session is not only to make the model work, but to understand how the surrounding engineering practices make ML systems **trackable, reproducible, testable, automatable, and ready to ship**.
