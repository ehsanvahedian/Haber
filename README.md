```markdown
<div align="center">

<img src="docs/images/banner.png" alt="Personal Planner Banner" width="100%">

# Personal Planner

### A Modern Personal Productivity Platform Built with Python & Domain-Driven Design

<p>
Personal Planner is an extensible productivity platform designed around <strong>Domain-Driven Design (DDD)</strong>, Clean Architecture principles, and modern development practices. The goal of this project is to provide a robust backend that can evolve into a complete productivity ecosystem with a powerful CLI, React frontend, plugin architecture, and automated project scaffolding.
</p>

<p>
<img src="https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/Alembic-Migrations-orange">
<img src="https://img.shields.io/badge/Architecture-DDD-success">
<img src="https://img.shields.io/badge/Status-Work%20In%20Progress-yellow">
<img src="https://img.shields.io/badge/License-MIT-blue">
</p>

</div>

---

# About

Personal Planner is much more than a simple task manager.

It is an experimental productivity platform that focuses on building a scalable and maintainable architecture capable of supporting multiple productivity modules under a single ecosystem.

Instead of tightly coupling business logic with frameworks, the project follows Domain-Driven Design to keep the domain independent, testable, and future-proof.

Current modules include task management and financial transaction management, while many additional capabilities are planned for future releases.

---

# Features

## Current

- Domain-Driven Design (DDD)
- Clean Architecture
- Repository Pattern
- Value Objects
- Task Management
- Transaction Management
- PostgreSQL Support
- Alembic Database Migrations
- Docker Support
- Dependency Injection Ready
- Modular Architecture
- Scalable Project Structure

---

# Project Preview

## Dashboard

<img src="docs/images/dashboard.png">

---

## Architecture

<img src="docs/images/architecture.png">

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migration | Alembic |
| Container | Docker |
| Architecture | Domain Driven Design |
| Pattern | Repository Pattern |
| Version Control | Git |

---

# Project Structure

```

Personal_Planner/

├── Domain/
│   ├── Entities
│   ├── ValueObjects
│   ├── Repositories
│   └── Services
│
├── Application/
│   ├── Commands
│   ├── Queries
│   ├── DTOs
│   └── UseCases
│
├── Infrastructure/
│   ├── Database
│   ├── ORM
│   ├── Repository
│   └── Configuration
│
├── Presentation/
│
├── migrations/
│
├── docker/
│
└── main.py

````

---

# Why Domain Driven Design?

The project is intentionally designed around Domain-Driven Design because business rules should remain independent from frameworks and infrastructure.

This architecture provides:

- Better maintainability
- Easier testing
- Clear separation of concerns
- High scalability
- Replaceable infrastructure
- Framework independence

---

# Getting Started

Clone the repository

```bash
git clone https://github.com/ehsanvahedian/personal_planner_app.git

cd personal_planner_app
````

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Docker

Run the complete development environment

```bash
docker compose up --build
```

Stop containers

```bash
docker compose down
```

---

# Database Migration

Create migration

```bash
alembic revision --autogenerate -m "Initial"
```

Run migrations

```bash
alembic upgrade head
```

---

# Future Vision

Personal Planner is being developed as a complete productivity ecosystem.

The roadmap currently includes:

* React Frontend Adapter
* Interactive CLI Application
* Project Package Manager
* Plugin System
* Authentication
* Notification Center
* Calendar Integration
* Scheduler
* Configuration Wizard
* Multiple Database Providers
* SQLite Support
* Redis Support
* REST API
* GraphQL API
* AI Assistant
* Cloud Synchronization
* Desktop Application
* Mobile Companion
* Theme Support
* Backup & Restore
* Import / Export
* Dashboard Analytics

---

# Planned CLI

```bash
planner init

planner setup

planner doctor

planner task add

planner task list

planner task complete

planner finance add

planner finance report

planner config

planner migrate

planner plugin install

planner update
```

---

# Planned React Frontend

A dedicated React frontend will be added to provide a modern user experience.

Planned technologies include:

* React
* TypeScript
* React Router
* TailwindCSS
* React Query
* Zustand
* Recharts

---

# Planned Package Manager

One of the primary goals of this project is creating a package manager capable of configuring the project automatically after cloning.

Example commands:

```bash
planner create

planner install

planner configure

planner add postgres

planner add sqlite

planner add react

planner add redis

planner add auth

planner add docker

planner add nginx

planner plugin search

planner plugin install
```

This installer will allow developers to customize their project without manually editing configuration files.

---

# Roadmap

* [x] Project Foundation
* [x] Domain Layer
* [x] Repository Pattern
* [x] Docker Environment
* [x] PostgreSQL Integration
* [x] Alembic Support
* [ ] Interactive CLI
* [ ] React Frontend
* [ ] Package Manager
* [ ] Plugin Marketplace
* [ ] REST API
* [ ] GraphQL
* [ ] Authentication
* [ ] AI Integration
* [ ] Cloud Sync
* [ ] Desktop Client
* [ ] Mobile Application

---

# Contributing

Contributions are always welcome.

If you have ideas, improvements, or bug fixes, feel free to open an Issue or submit a Pull Request.

---

# License

This project is released under the MIT License.

---

# Author

**Ehsan Vahedian**

GitHub

https://github.com/ehsanvahedian

---

<div align="center">

### Build • Organize • Automate

⭐ If you find this project useful, consider giving it a star.

</div>
```
