# Master TODO List - Financial Data Platform

## Current Epic: epic-FDP-0001
**Title**: Create Initial charting-api-gw in Rust (Local Storage + Pre-Generated Data)
**Goal**: Build a Rust-based REST API gateway that serves static financial data from local storage.
**Target**: September 15, 2025
**Status**: In Progress (7/16 behaviors complete)
**Components Involved**: API Gateway, ProtoBuf Schemas

### ✅ Completed (Cross-Component)
| Branch | Component | Description | PR | Date |
|--------|-----------|-------------|-----|------|
| `feature/epic-FDP-0001-define-l1-market-schema` | ProtoBuf Schemas | Define L1 market data schema | Pending | 2025-09-22 |
| `feature/epic-FDP-0001-define-l2-market-schema` | ProtoBuf Schemas | Define L2 market data schema | Pending | 2025-09-22 |
| `feature/epic-FDP-0001-define-candle-schema` | ProtoBuf Schemas | Define candle aggregated data schema | Pending | 2025-09-22 |
| `feature/epic-FDP-0001-define-metadata-schema` | ProtoBuf Schemas | Define metadata schema | Pending | 2025-09-22 |
| `feature/epic-FDP-0001-define-rate-value-schema` | ProtoBuf Schemas | Define rate value schema | Pending | 2025-09-23 |
| `feature/epic-FDP-0001-define-index-value-schema` | ProtoBuf Schemas | Define index value schema | Pending | 2025-09-23 |
| `feature/epic-FDP-0001-define-economic-indicator-schema` | ProtoBuf Schemas | Define economic indicator schema | Pending | 2025-09-23 |

### 🚧 In Progress
| Branch | Component | Description | Assignee | Status |
|--------|-----------|-------------|----------|---------|
| `feature/epic-FDP-0001-setup-project-configuration` | Project Plan | Setup Claude configuration, repositories mapping, and enhanced documentation | Claude | Ready for review |

### 📋 Ready to Start (Priority Order)
| Branch | Component | Description | Dependencies | Estimate |
|--------|-----------|-------------|--------------|----------|
| `feature/epic-FDP-0001-define-securities-info-schema` | ProtoBuf Schemas | Define securities info schema | - | 1 day |
| `feature/epic-FDP-0001-define-corporate-actions-schema` | ProtoBuf Schemas | Define corporate actions schema | - | 1 day |
| `feature/epic-FDP-0001-validate-schemas-protoc` | ProtoBuf Schemas | Validate schemas with protoc | All schemas | 0.5 days |
| `feature/epic-FDP-0001-scaffold-rust-axum` | API Gateway | Scaffold Rust project using axum | Core schemas | 1 day |
| `feature/epic-FDP-0001-define-rust-data-structures` | API Gateway | Define initial data structures (candle, L1/L2) | ProtoBuf schemas | 1 day |
| `feature/epic-FDP-0001-load-local-financial-data` | API Gateway | Load pre-generated financial data from local files | Data structures | 2 days |
| `feature/epic-FDP-0001-implement-rest-endpoints` | API Gateway | Implement REST endpoints to serve charting data | Data loading | 2 days |
| `feature/epic-FDP-0001-add-error-handling-logging` | API Gateway | Add basic error handling and logging | REST endpoints | 1 day |
| `feature/epic-FDP-0001-dockerize-api-service` | API Gateway | Dockerize the service | Basic API complete | 0.5 days |

### 🔴 Blocked
| Branch | Component | Description | Blocker | Action Needed |
|--------|-----------|-------------|---------|---------------|
| (none yet) | - | - | - | - |

## Next Epic: epic-FDP-0002
**Title**: Create Initial charting-app in JS to Render Available Data
**Goal**: Build a Next.js frontend that fetches and visualizes financial data from the API gateway.
**Target**: September 20, 2025
**Status**: Planning (0/6 behaviors complete)
**Components Involved**: Frontend

### 📋 Ready to Start (Priority Order)
| Branch | Component | Description | Dependencies | Estimate |
|--------|-----------|-------------|--------------|----------|
| `feature/epic-FDP-0002-scaffold-nextjs-project` | Frontend | Scaffold Next.js project | - | 0.5 days |
| `feature/epic-FDP-0002-implement-charting-component` | Frontend | Implement charting component using react-chartjs-2 | Next.js scaffold | 2 days |
| `feature/epic-FDP-0002-fetch-api-render-charts` | Frontend | Fetch data from REST API and render charts | API endpoints + charting | 2 days |
| `feature/epic-FDP-0002-add-ui-layout-navigation` | Frontend | Add basic UI layout and navigation | Basic charting | 1 day |
| `feature/epic-FDP-0002-handle-loading-error-states` | Frontend | Handle loading and error states | UI layout | 1 day |
| `feature/epic-FDP-0002-dockerize-frontend` | Frontend | Dockerize frontend for deployment | Frontend complete | 0.5 days |

## Next Epic: epic-FDP-0003
**Title**: Create Persistent TimescaleDB Service for charting-api-gw
**Goal**: Integrate TimescaleDB (PostgreSQL extension) for time-series data persistence.
**Target**: Q4 2025
**Status**: Planning

### 🔧 Planned Features (Cross-Component)
| Branch | Components | Description | Trigger |
|--------|------------|-------------|---------|
| `feature/epic-FDP-0003-setup-timescaledb` | API Gateway | Set up TimescaleDB instance | MVP API complete |
| `feature/epic-FDP-0003-define-db-schema` | API Gateway | Define schema for candle, L1/L2, and metadata | TimescaleDB setup |
| `feature/epic-FDP-0003-connect-rust-timescaledb` | API Gateway | Connect Rust API to TimescaleDB using sqlx | DB schema |
| `feature/epic-FDP-0003-implement-data-ingestion` | API Gateway | Implement data ingestion and query logic | DB connection |
| `feature/epic-FDP-0003-migrate-test-data` | API Gateway | Migrate pre-generated data into TimescaleDB | Ingestion logic |
| `feature/epic-FDP-0003-add-db-health-check` | API Gateway | Add health check endpoint for DB connectivity | Data migration |

## Future Epics (Roadmap)

### epic-FDP-0004: Create Data Uploader for US Federal SOFR Data
**Title**: Create Data Uploader for US Federal SOFR Data
**Goal**: Build a Rust service to fetch, parse, and upload SOFR data into TimescaleDB.
**Components**: API Gateway
**Target**: Q1 2026

- Identify SOFR data source (e.g., FRED, Treasury.gov)
- Implement data fetcher with retry logic
- Parse and normalize SOFR data
- Define ProtoBuf schema for rate values
- Insert SOFR data into TimescaleDB
- Schedule periodic updates (e.g., daily)

### epic-FDP-0005: Implement Observability Backbone with Prometheus
**Title**: Implement Observability Backbone with Prometheus
**Goal**: Add metrics collection to all services using Prometheus.
**Components**: API Gateway
**Target**: Q2 2026
**Milestone**: Observability Backbone (Due: September 25, 2025)

#### 📋 Planned Tasks
| Task | Component | Description |
|------|-----------|-------------|
| Integrate Prometheus client into Rust API | API Gateway | Add prometheus crate integration |
| Expose /metrics endpoint | API Gateway | Create metrics endpoint |
| Track request latency, error rates, and DB query times | API Gateway | Implement key metrics |
| Add Prometheus client to SOFR uploader | API Gateway | Metrics for data ingestion |
| Configure Prometheus scrape targets | Infrastructure | Set up scrape configuration |

### epic-FDP-0006: Implement Grafana Observability Front-End
**Title**: Implement Grafana Observability Front-End
**Goal**: Visualize system metrics using Grafana dashboards.
**Components**: Frontend, Infrastructure
**Target**: Q2 2026

#### 📋 Planned Tasks
| Task | Component | Description |
|------|-----------|-------------|
| Set up Grafana instance | Infrastructure | Deploy Grafana service |
| Connect Grafana to Prometheus | Infrastructure | Configure data source |
| Create dashboards for API latency and ingestion success | Frontend | Build monitoring dashboards |
| Add alerting rules | Infrastructure | Configure alerts |

### epic-FDP-0007: Perform Info-Sec Security Audit of Initial Code
**Title**: Perform Info-Sec Security Audit of Initial Code
**Goal**: Ensure secure coding practices and identify vulnerabilities.
**Components**: All services
**Target**: Q3 2026
**Milestone**: Initial Info-Sec Audit (Due: September 30, 2025)

#### 📋 Planned Tasks
| Task | Component | Description |
|------|-----------|-------------|
| Run static analysis tools (cargo-audit, npm audit) | All | Security scanning |
| Review OAuth2 implementation for token handling | API Gateway | Authentication security |
| Validate input sanitization and error handling | All | Input validation review |
| Check for exposed secrets or credentials | All | Secrets scanning |
| Document security posture and remediation plan | All | Security documentation |
| Schedule periodic security reviews | All | Ongoing security process |

### epic-FDP-0008: Implement Advanced Integration Features
**Title**: Implement Advanced Integration Features
**Goal**: Add gRPC endpoints, batch job orchestration, and internal messaging capabilities.
**Components**: API Gateway, Infrastructure
**Target**: Q2 2026

#### 📋 Planned Tasks
| Task | Component | Description |
|------|-----------|-------------|
| Add gRPC endpoints to backend for tightly coupled workflows | API Gateway | gRPC service implementation |
| Build batch job runner using Tokio tasks (daily summary, cleanup) | API Gateway | Batch processing orchestration |
| Add NATS-based internal PUB/SUB for cache invalidation | Infrastructure | Internal messaging system |
| Implement ProtoBuf-to-REST tooling (grpc-gateway or custom) | API Gateway | REST/ProtoBuf integration |
| Add GraphQL endpoint for advanced filtering (optional) | API Gateway | Advanced query capabilities |
| Begin AI-assisted migration tooling (schema diff + SQL generation) | Infrastructure | Schema evolution automation |

### epic-FDP-0009: Implement System Resilience and Reconciliation
**Title**: Implement System Resilience and Reconciliation
**Goal**: Harden the system with resilience patterns and prepare for external data reconciliation.
**Components**: All services
**Target**: Q3 2026

#### 📋 Planned Tasks
| Task | Component | Description |
|------|-----------|-------------|
| Add retry, circuit breaker, and timeout logic to async workflows | API Gateway | Resilience patterns |
| Implement schema versioning and compatibility checks | ProtoBuf Schemas | Schema evolution safety |
| Build reconciliation service skeleton (external vs. internal data) | API Gateway | Data integrity service |
| Add comprehensive alerting rules (ingestion lag, auth failures) | Infrastructure | Advanced monitoring |
| Document schema evolution and API contracts | All | Technical documentation |
| Add automated compatibility testing across schema versions | ProtoBuf Schemas | Regression prevention |

## Component-Specific Backlogs

### ProtoBuf Schemas (`protobuf-schemas`)
See: [protobuf-schemas/TODO.md](../protobuf-schemas/TODO.md)
- Current focus: Define core financial data schemas (epic-FDP-0001)
- Next priority: Schema validation and testing
- Tech debt: Need versioning strategy

### API Gateway (`charting-api-gw-rust`)
See: [charting-api-gw-rust/TODO.md](../charting-api-gw-rust/TODO.md)
- Current focus: Rust project scaffold and data structures (epic-FDP-0001)
- Next priority: TimescaleDB integration (epic-FDP-0003)
- Tech debt: Need proper error handling patterns

### Frontend (`charting-app-js`)
See: [charting-app-js/TODO.md](../charting-app-js/TODO.md)
- Current focus: Next.js setup and charting components (epic-FDP-0002)
- Next priority: Advanced UI features
- Tech debt: Component architecture and state management

## Cross-Component Integration Points 🔌

### Currently Planned
| From | To | Type | Description | Status |
|------|----|------|-------------|--------|
| ProtoBuf | API Gateway | Code Gen | Generate Rust structs from schemas | 📋 Planned |
| ProtoBuf | Frontend | Code Gen | Generate TypeScript types from schemas | 📋 Planned |
| Frontend | API Gateway | REST | HTTP API communication | 📋 Planned |

### Future Integrations
| From | To | Type | Description | Epic |
|------|----|------|-------------|------|
| API Gateway | TimescaleDB | SQL | Time-series data persistence | epic-FDP-0003 |
| API Gateway | Prometheus | HTTP | Metrics collection | epic-FDP-0005 |
| Frontend | Grafana | HTTP | Observability dashboards | epic-FDP-0006 |

## System-Wide Issues 🐛

### High Priority
(None identified yet)

### Medium Priority
(None identified yet)

## Technical Debt (System-Wide) 💳

### Architecture
- [ ] No service discovery mechanism planned
- [ ] No API versioning strategy defined
- [ ] No centralized configuration management
- [ ] No inter-service communication standards

### Schema & Integration
- [ ] **ProtoBuf-to-REST tooling strategy**: Need reliable way to generate RESTful JSON from ProtoBuf schemas (grpc-gateway or custom wrappers)
- [ ] **Schema evolution strategy**: Need versioning strategy for ProtoBuf schemas to avoid breaking changes across services
- [ ] **GraphQL integration approach**: Consider using specific Rust GraphQL tools if advanced filtering is needed
- [ ] **AI-assisted migrations**: Custom scripting needed for Prisma/sqlc integration with schema evolution

### Development
- [ ] No shared development environment setup
- [ ] No unified testing strategy across components
- [ ] No automated dependency management
- [ ] No code generation pipeline from ProtoBuf schemas

### Resilience & Operations
- [ ] **Retry logic and circuit breakers**: Need timeout logic for async workflows
- [ ] **Schema compatibility checks**: Automated validation for schema evolution
- [ ] **External data reconciliation**: Service skeleton for external vs. internal data integrity
- [ ] **Comprehensive alerting rules**: Beyond basic metrics (ingestion lag, auth failures, schema validation)

### Documentation
- [ ] No API contract documentation
- [ ] No deployment procedures documented
- [ ] No monitoring and alerting runbooks

## Metrics & Progress 📊

### epic-FDP-0001 Progress
- Started: TBD
- Target: September 15, 2025
- Components: 2 active (API Gateway, ProtoBuf Schemas)
- Behaviors: 0/16 complete (0%)
- Velocity: TBD (project just starting)

### epic-FDP-0002 Progress
- Started: TBD
- Target: September 20, 2025
- Components: 1 active (Frontend)
- Behaviors: 0/6 complete (0%)
- Dependencies: epic-FDP-0001 API endpoints

### Component Progress
| Component | Epic | Behaviors | Complete | In Progress | Blocked |
|-----------|------|-----------|----------|-------------|---------|
| ProtoBuf Schemas | epic-FDP-0001 | 10 | 6 (60%) | 0 | 0 |
| API Gateway | epic-FDP-0001 | 6 | 0 (0%) | 0 | 0 |
| Frontend | epic-FDP-0002 | 6 | 0 (0%) | 0 | 0 |

### Integration Milestones
- 📋 ProtoBuf schemas defined and validated (epic-FDP-0001)
- 📋 Basic API serving static data (epic-FDP-0001)
- 📋 Frontend displaying charts from API (epic-FDP-0002)
- 📋 End-to-end dockerized deployment (epic-FDP-0001, epic-FDP-0002)
- 📋 TimescaleDB integration (epic-FDP-0003)
- 📋 Observability stack (epic-FDP-0005, epic-FDP-0006)
- 📋 Security audit complete (epic-FDP-0007)

## Coordination Notes 📝

### Project Kickoff Notes
- Decision: ProtoBuf schemas must be completed first to enable parallel development
- All monetary values will use appropriate decimal precision types
- Market data must include both event time and ingestion time
- Focus on financial accuracy over performance optimization initially

### Epic Dependencies
- **epic-FDP-0002** depends on **epic-FDP-0001**: Frontend needs API endpoints
- **epic-FDP-0003** depends on **epic-FDP-0001**: TimescaleDB integration needs basic API
- **epic-FDP-0004** depends on **epic-FDP-0003**: SOFR uploader needs database persistence
- **epic-FDP-0005** depends on **epic-FDP-0001**: Prometheus metrics need running services
- **epic-FDP-0006** depends on **epic-FDP-0005**: Grafana needs Prometheus data
- **epic-FDP-0007** depends on **epic-FDP-0001, epic-FDP-0002**: Security audit needs code to review
- **epic-FDP-0008** depends on **epic-FDP-0001**: Advanced integration needs basic services
- **epic-FDP-0009** depends on **epic-FDP-0001, epic-FDP-0003**: Resilience needs services and persistence

## Review & Sync Schedule 📅

### Daily
- **Stand-up**: 9am - Component leads sync on blockers

### Weekly
- **Integration Review**: Thursdays 2pm - Test cross-component flows
- **Progress Update**: Fridays 4pm - Update TODO-MASTER.md

### Bi-weekly
- **Architecture Review**: Every other Tuesday - Cross-component design decisions
- **Backlog Grooming**: Every other Monday - Prioritize cross-component work

### Monthly
- **Epic Planning**: First Wednesday - Review epic goals and timeline
- **Retrospective**: Last Friday - Cross-team learnings

## Quick Links

### Repositories
- [Project Plan](https://github.com/yourorg/financial-data-project-plan)
- [API Gateway](https://github.com/yourorg/charting-api-gw-rust)
- [Frontend](https://github.com/yourorg/charting-app-js)
- [ProtoBuf Schemas](https://github.com/yourorg/protobuf-schemas)

### Dashboards
- CI/CD Pipeline: TBD
- Monitoring: TBD (after epic-FDP-0005)
- Error Tracking: TBD (after epic-FDP-0005)