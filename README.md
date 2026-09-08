# MLOps Learning Journey

This repository contains my complete learning journey through the **MLOps** sessions with the **MLOps MENA Community**.

The goal of this repository is to keep everything related to the journey in one place: session notes, practical exercises, mini-projects, experiments, MLOps workflows, and the final project.

## Repository Structure

```text
MLOps/
├── Notes/
│   ├── session1 .excalidraw
│   └── Session 2.excalidraw
├── Session 1/
│   └── Production-ready ML API project
├── Session2/
│   └── Shipping to Production project
└── README.md
```

## Sessions

### Session 1 — ML Service Foundations

Session 1 focused on turning a machine learning model into a production-oriented API, including project packaging, API development, validation, Docker, logging, testing, and CI concepts.

The practical project is available in [`Session 1/`](./Session%201/).

### Session 2 — Shipping to Production

Session 2 focuses on the tooling and engineering practices needed to ship ML systems more reliably:

- MLflow experiment tracking and model registry
- Weights & Biases (W&B)
- DVC for data and model versioning
- Ruff, Black, and pre-commit
- Terraform and Infrastructure as Code
- GitHub Actions CI/CD
- Integration testing

The practical project is available in [`Session2/`](./Session2/), with its current implementation and progress documented in [`Session2/README.md`](./Session2/README.md).

The first Session 2 requirement is currently implemented: three MLflow runs are tracked, model artifacts are registered, and the best model is promoted to Staging.

## Learning Roadmap

The journey is focused on understanding how to move from machine learning development to reliable, reproducible, and production-ready ML systems.

```text
Machine Learning
      ↓
Project Structure & Packaging
      ↓
API & Model Serving
      ↓
Testing & Code Quality
      ↓
Docker & Containerization
      ↓
Experiment Tracking
      ↓
Data & Model Versioning
      ↓
Infrastructure as Code
      ↓
CI/CD
      ↓
Scale, Reliability & Production Operations
      ↓
Final MLOps Project
```

> The roadmap and project structure will continue to evolve as new sessions are completed.

## Community

This journey is part of the **MLOps MENA Community** learning experience.

A big thank you to everyone contributing to the community and to **Aya Nasser Salama** for the time, effort, explanations, and support throughout the sessions.
