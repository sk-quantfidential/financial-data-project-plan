# Financial Data Platform

## Overview

This project is a modern, resilient, asynchronous financial data platform designed to ingest, process, and serve various types of financial data. It uses Protocol Buffers (ProtoBuf) as the primary schema definition language for inter-service communication and data modeling. The MVP exposes a RESTful API for the frontend, with ProtoBuf schemas serving as the canonical source for both internal and external data formats.

**Tech Stack:**
- **Backend Services**: Rust (axum/actix-web framework)
- **Database**: PostgreSQL with TimescaleDB extension for time-series optimization
- **Messaging**: Kafka for asynchronous processing (Tokio + rdkafka)
- **Frontend**: Next.js with TypeScript and react-chartjs-2 for charting
- **Schemas**: Protocol Buffers v3 for canonical data definitions
- **Authentication**: OAuth2 (oauth2 crate or Auth0 integration)
- **Containerization**: Docker with auto-generated containers via CI/CD
- **CI/CD**: GitHub Actions with Docker build/push automation
- **Observability**: Prometheus metrics collection + Grafana dashboards
- **Async Runtime**: Rust + Tokio for orchestration and monitoring

## Core Features

- Real-time ingestion of market data (L1 and L2)
- Aggregation of candle data for charting
- Storage and retrieval of rate values, index values, and economic indicators
- Metadata tagging and schema evolution support
- REST API exposure based on ProtoBuf schema definitions
- Support for multiple financial instruments and asset classes

## 🧱 Architecture Overview

| Component      | Technology Choice                                                                 |
|----------------|----------------------------------------------------------------------------------|
| Frontend       | Next.js (REST API for MVP, optional GraphQL for advanced filtering)              |
| UI Backend     | Rust service, REST API (initial), optional gRPC/GraphQL, OAuth2 authentication   |
| Messaging      | ProtoBuf schemas for all services; gRPC for sync workflows; Kafka for async; NATS optional |
| Persistence    | PostgreSQL, schema derived from ProtoBuf; AI-assisted migrations                 |
| Batch & Async  | Rust + Tokio for orchestration and monitoring                                    |
| Containerization| Docker (auto-generated containers via CI/CD)                                    |
| CI/CD          | GitHub Actions / GitLab CI / similar, with Docker build/push                     |
| Observability  | Prometheus + Grafana                                                             |
| Authentication | OAuth2                                                                            |
| Reconciliation | Planned for future (external/internal data integrity checks)                     |

For more technical and schema details, see the [project-plan](./project-plan.md).

## Project Plan

🗂️ Recommended Structure for financial-data-project-plan.git
financial-data-project-plan.git/
├── .github/
│   └── workflows/
│       └── sync-projects.yml        # GitHub Action to sync issues/milestones
├── project-config/
│   ├── epics.yml                    # High-level epics across all repos
│   ├── milestones/
│   │   ├── charting-api-gw.yml
│   │   ├── charting-app.yml
│   │   └── protobuf-schemas.yml
│   ├── labels.yml                   # Shared label definitions
│   └── repos.yml                    # List of target repos and their mappings
└── README.md                        # Documentation for contributors

🔄 How It Works
1. Define Epics & Milestones in YAML
Each file contains structured definitions for issues, milestones, and labels.
2. Use GitHub Actions or External CI/CD
A GitHub Action in financial-data-project-plan.git can:
- Authenticate with GitHub using a PAT (Personal Access Token)
- Read YAML files
- Use the REST API to create issues/milestones across repos
- Optionally link issues to GitHub Projects or labels
3. Triggering
- Manual dispatch (via workflow_dispatch)
- On push to main
- On tag or milestone completion

### Github Sync



🔐 Setup Required
- Create a GitHub secret in financial-data-project-plan.git:
- Name: GH_TOKEN
- Value: A Personal Access Token with repo scope
- Push the workflow and script to your repo:
git add .github/workflows/sync-projects.yml .github/scripts/sync_projects.py
git commit -m "Add project sync workflow"
git push origin main
- Run the workflow manually from the GitHub Actions tab.

Would you like me to generate a sample Personal Access Token scope checklist or help you test this with a dry run mode?

GitHub secrets are the secure way to store sensitive credentials like Personal Access Tokens (PATs) for use in Actions workflows. Here’s how to create them, followed by a checklist of scopes your PAT should include.

🔐 How to Create GitHub Secrets
🧭 For a Repository-Level Secret
- Go to your repo (e.g., financial-data-project-plan.git)
- Click Settings → Secrets and variables → Actions
- Click New repository secret
- Enter:
- Name: GH_TOKEN
- Value: your GitHub Personal Access Token
- Click Add secret
✅ This secret will now be available to all GitHub Actions workflows in that repo.


🧾 Personal Access Token Scope Checklist
To allow the workflow to create issues, milestones, and labels across repos, your PAT should include the following scopes:
| Scope | Purpose | 
| repo | Full control of private repositories (required for issues, milestones, labels) | 
| workflow | Optional: allows managing workflows if needed later | 
| read:org | Optional: read access to organization metadata (if using org-level repos) | 
| write:repo_hook | Optional: if you plan to manage webhooks via API | 
| admin:repo_hook | Optional: for full webhook control (rarely needed) | 


✅ Minimum Required Scope:
repo


🔒 You can generate a PAT at GitHub Developer Settings → Personal Access Tokens


🧠 Pro Tip for Multi-Repo Automation
If you want to sync issues/milestones across multiple repos from one central repo:
- Use a fine-scoped PAT with access to only the relevant repos
- Consider using organization-level secrets if all repos are in the same GitHub org
Would you like help generating a scoped PAT description for your use case, or setting up org-level secrets if you’re working across multiple repos in a GitHub organization?

## Protobuf Schema Requirements

- All data types defined using Protocol Buffers v3 syntax
- Modular, versioned schemas for future evolution
- Each schema includes:
  - Unique identifiers
  - Timestamps (event and ingestion time)
  - Source metadata
  - Optional fields for extensibility
- Optimized for serialization efficiency and human readability
- Support for nested types and repeated fields
- Compatibility with Rust, PostgreSQL, and Kafka serialization/deserialization

## Design Guidelines

- Clear, descriptive naming conventions for message types and fields
- Logical package grouping (e.g., market, economic, instrument)
- Comments explaining field semantics
- Compatibility with RESTful JSON generation tools (e.g., grpc-gateway)
- Extensible design with optional fields and reserved tags
- Enums for standardized values (e.g., market status, instrument type)

## Enumerated Financial Data Types

- **L1 Market Data:** Bid/ask price and size, last traded price, market status
- **L2 Market Data:** Multiple levels of bid/ask prices and sizes, order timestamps and IDs, optional participant IDs
- **Candle Aggregated Data:** Open, high, low, close prices, volume, time interval
- **Rate Value:** Interest rates, FX rates, rate source and timestamp
- **Index Value:** Index level, constituent metadata, calculation timestamp
- **Economic Indicator:** Indicator name, value and revision history, release timestamp and source
- **Metadata:** Source system, region, category, report, data quality flags, ingestion timestamp, tags
- **Securities Info:** Instrument ID, name, type, exchange, currency, lifecycle dates
- **Additional Types:** Corporate actions, trade prints, settlement instructions, risk metrics, news sentiment

## Extensibility

The schema will evolve to include workflow requests and responses embedding these data types, supporting a web application similar to [YCharts](https://ycharts.com).
