🧱 Starting Epics & Milestones
🟦 Epic 1: Create Initial charting-api-gw in Rust (Local Storage + Pre-Generated Data)
Goal: Build a Rust-based REST API gateway that serves static financial data from local storage.
🎯 Milestones
- [ ] Scaffold Rust project using axum or actix-web
- [ ] Define initial data structures (e.g., candle, L1/L2) in Rust
- [ ] Load pre-generated financial data from local JSON/CSV files
- [ ] Implement REST endpoints to serve charting data
- [ ] Add basic error handling and logging
- [ ] Dockerize the service for local deployment

🟦 Epic 2: Create Initial charting-app in JS to Render Available Data
Goal: Build a Next.js frontend that fetches and visualizes financial data from the API gateway.
🎯 Milestones
- [ ] Scaffold Next.js project
- [ ] Implement charting component using react-chartjs-2 or d3.js
- [ ] Fetch data from REST API and render charts
- [ ] Add basic UI layout and navigation
- [ ] Handle loading and error states
- [ ] Dockerize frontend for deployment

🟦 Epic 3: Create Persistent TimescaleDB Service for charting-api-gw
Goal: Integrate TimescaleDB (PostgreSQL extension) for time-series data persistence.
🎯 Milestones
- [ ] Set up TimescaleDB instance (Docker or cloud)
- [ ] Define schema for candle, L1/L2, and metadata
- [ ] Connect Rust API to TimescaleDB using sqlx or diesel
- [ ] Implement data ingestion and query logic
- [ ] Migrate pre-generated data into TimescaleDB
- [ ] Add health check endpoint for DB connectivity

🟦 Epic 4: Create Data Uploader for US Federal SOFR Data
Goal: Build a Rust service to fetch, parse, and upload SOFR data into TimescaleDB.
🎯 Milestones
- [ ] Identify SOFR data source (e.g., FRED, Treasury.gov)
- [ ] Implement data fetcher with retry logic
- [ ] Parse and normalize SOFR data
- [ ] Define ProtoBuf schema for rate values
- [ ] Insert SOFR data into TimescaleDB
- [ ] Schedule periodic updates (e.g., daily)

🟦 Epic 5: Implement Observability Backbone with Prometheus
Goal: Add metrics collection to all services using Prometheus.
🎯 Milestones
- [ ] Integrate Prometheus client into Rust API (prometheus crate)
- [ ] Expose /metrics endpoint
- [ ] Track request latency, error rates, and DB query times
- [ ] Add Prometheus client to SOFR uploader
- [ ] Configure Prometheus scrape targets
- [ ] Validate metrics collection locally

🟦 Epic 6: Implement Grafana Observability Front-End
Goal: Visualize system metrics using Grafana dashboards.
🎯 Milestones
- [ ] Set up Grafana instance (Docker or cloud)
- [ ] Connect Grafana to Prometheus
- [ ] Create dashboards for API latency, ingestion success, DB health
- [ ] Add alerting rules (e.g., ingestion failure, high latency)
- [ ] Share dashboard templates for team use

🟦 Epic 7: Perform Info-Sec Security Audit of Initial Code
Goal: Ensure secure coding practices and identify vulnerabilities.
🎯 Milestones
- [ ] Run static analysis tools (e.g., cargo-audit, npm audit)
- [ ] Review OAuth2 implementation for token handling
- [ ] Validate input sanitization and error handling
- [ ] Check for exposed secrets or credentials
- [ ] Document security posture and remediation plan
- [ ] Schedule periodic security reviews

🧱 Strategy: Centralized Project Configuration with financial-data-project-plan.git
✅ Yes—you can absolutely use a dedicated repo like financial-data-project-plan.git to:
- Store all project planning artifacts (YAML/JSON configs, templates, diagrams)
- Drive automation across multiple repos via GitHub Actions or external CI/CD tools
- Maintain a single source of truth for your roadmap, epics, milestones, and labels

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



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

🧠 Benefits of This Approach
| Feature | Benefit | 
| Centralized Planning | One repo to rule them all—easy to audit, version, and collaborate | 
| Multi-Repo Sync | Push updates to all related repos from one place | 
| AI-Friendly | Easy for AI tools to generate/update YAML configs | 
| CI/CD Compatible | Integrates with GitHub Actions, Argo, Jenkins, etc. | 
| Scalable | Add new repos or milestones without changing code logic | 



🧩 Alternative Approaches
If you prefer not to use a dedicated repo, you could:
- Store configs in a mono-repo (if all code lives together)
- Use GitHub Projects (Beta) with cross-repo views—but this is UI-driven, not config-driven
- Use external orchestration tools (e.g., Terraform + GitHub provider) for infra-as-code style management
