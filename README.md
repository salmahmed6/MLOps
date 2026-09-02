# MLOps Learning Journey

This repository contains my complete learning journey through the **MLOps** sessions with the **MLOps MENA Community**.

The goal of this repository is to keep everything related to the journey in one place: my session notes, practical exercises, mini-projects, experiments, and the final project.

## What This Repository Will Contain

As the journey continues, this repository will be updated session by session with:

- Notes and summaries for every MLOps session
- Important concepts, commands, and examples
- Practical exercises and experiments
- Session-related mini-projects
- Code and configuration files used during the sessions
- MLOps tools and workflows learned throughout the program
- The final project and everything built around it

The repository will grow over time as I complete each session.

## Planned Structure

The exact structure may evolve as the sessions progress, but the repository will generally follow this organization:

```text
MLOps/
│
├── Session 1/
│   ├── notes/
│   └── project/
│
├── Session 2/
│   ├── notes/
│   └── project/
│
├── Session 3/
│   ├── notes/
│   └── project/
│
├── ...
│
├── Final Project/
│   ├── docs/
│   ├── src/
│   ├── tests/
│   └── ...
│
└── README.md
```

The folder names and contents may change depending on the topics and projects covered in each session.

## Learning Roadmap

The journey is focused on understanding how to move from machine learning development to reliable, reproducible, and production-ready ML systems.

The repository is expected to cover topics such as:

```text
Machine Learning
      ↓
Project Structure & Packaging
      ↓
FastAPI & Model Serving
      ↓
Testing & Code Quality
      ↓
Docker & Containerization
      ↓
CI/CD
      ↓
Experiment Tracking
      ↓
Data & Model Versioning
      ↓
Infrastructure & Deployment
      ↓
Continuous Training
      ↓
Final MLOps Project
```

> The roadmap will be updated as new sessions and topics are completed.

## Session 1

Session 1 introduced the foundations of productionizing an ML service.

The related work includes topics such as:

- MLOps maturity and production thinking
- Python project structure and packaging
- FastAPI model serving
- Pydantic validation
- Model abstraction and serialization concepts
- Docker and Docker Compose
- Structured logging
- Unit and API testing with Pytest
- Test coverage
- Code quality with Ruff and Black

### Session 1 Mini-Project

The first practical project is a **Ride Duration ML Service**.

The project turns a machine learning prediction workflow into a small production-oriented API with:

- `GET /health`
- `POST /predict`
- `POST /feedback`
- Pydantic request/response validation
- Structured JSON logging
- Request IDs and latency logging
- Automated tests
- Coverage checks
- Docker support

More details for the project will be available inside the Session 1 project folder.

## Session 2 and Beyond

The next sessions will continue building on the first project and introduce more MLOps practices and tools.

As each session is completed, this repository will include:

1. My notes and explanations from the session.
2. Practical exercises and examples.
3. The related project or implementation.
4. Any configuration, workflows, or infrastructure files needed.
5. A clear record of what I learned and built.

This will make the repository both a learning record and a reference that I can return to later for revision.

## Final Project

At the end of the journey, the repository will contain the **final MLOps project**, bringing together the concepts learned across the sessions.

The final project will be developed step by step during the program rather than being treated as a separate task at the end.

Its final scope and technologies will be based on the topics, requirements, and project work covered throughout the sessions.

## Why I Created This Repository

I created this repository to:

- Keep all MLOps learning materials organized
- Track my progress from session to session
- Practice the concepts through real projects
- Make revision easier later
- Build a public record of the work I am doing during the journey
- Bring everything together in the final project

## Progress

- [x] Repository created
- [x] Session 1 notes
- [x] Session 1 mini-project
- [ ] Session 2 notes
- [ ] Session 2 project
- [ ] Remaining sessions
- [ ] Final project

The checklist will be updated as the journey continues.

## Community

This journey is part of the **MLOps MENA Community** learning experience.

A big thank you to everyone contributing to the community and to **Aya Nasser Salama** for the time, effort, explanations, and support throughout the sessions.

## Author

**Salma Ahmed**

GitHub: https://github.com/salmahmed6
