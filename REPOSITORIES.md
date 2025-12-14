# Component Repositories

## Project: Financial Data Platform (FDP)

This document defines the component repositories that make up the Financial Data Platform multi-component project.

## Repository Structure

```text
Financial Data Platform
├── project-plan/              # Master coordination repository
├── protobuf-schemas/          # Protocol Buffer schema definitions
│
├── charting-api-gw-rust/      # Rust API gateway and backend services
├── client-gw-core-py/         # Python async WebSocket gateway core library
├── deribit-client-gw-py/      # Python Deribit exchange WebSocket gateway
│
├── charting-app-js/           # Next.js frontend application for charting
│
└── orchestrator-docker/       # Docker Compose orchestration for deployment
```

## Component Repository Definitions

### 1. Project Plan Repository

**Repository**: `financial-data/project-plan/`
**Type**: Project Coordination
**Status**: Active

**Purpose**: Master coordination repository for the Financial Data Platform project.

**Responsibilities**:
- Epic and milestone planning across all components
- Cross-component coordination via TODO-MASTER.md
- API contract definitions and version management
- Master Claude configuration in `.claude/`
- Integration test coordination
- Documentation and architecture decisions

**Key Files**:
- `CLAUDE.md` - Master project configuration
- `REPOSITORIES.md` - This file
- `TODO-MASTER.md` - Cross-component milestone tracking
- `contracts/` - API contract definitions
- `.claude/` - Master Claude configuration

### 2. ProtoBuf Schemas Repository

**Repository**: `financial-data/protobuf-schemas/`
**Type**: Schema Definition
**Technology**: Protocol Buffers v3
**Status**: Active

**Purpose**: Canonical source of truth for all financial data type definitions using Protocol Buffers.

**Responsibilities**:
- Define all financial data message types (L1/L2 market data, candles, rates, indices)
- Maintain schema versioning and evolution
- Generate language bindings for Rust and TypeScript
- Provide schema validation and compatibility testing
- Document field semantics and usage patterns

**Key Files**:
- `schemas/` - ProtoBuf schema definitions (.proto files)
- `generated/` - Generated language bindings
- `docs/` - Schema documentation
- `TODO.md` - Component milestone tracking

**Claude Configuration**:
- `.claude/`
  - `.claude_protobuf_schemas.md` - ProtoBuf-specific standards
  - `.claude_testing_protobuf_schemas.md` - Schema testing standards

**Integration Points**:
- **charting-api-gw-rust**: Imports generated Rust bindings
- **charting-app-js**: Imports generated TypeScript definitions
- **Kafka**: Schema Registry integration for message validation

### 3. Charting API Gateway (Rust)

**Repository**: `financial-data/charting-api-gw-rust/`
**Type**: Backend Service
**Technology**: Rust (axum, tokio, sqlx)
**Status**: Active

**Purpose**: High-performance API gateway and backend services for financial data ingestion, processing, and serving.

**Responsibilities**:
- Real-time market data ingestion (L1/L2)
- Data aggregation and candle generation
- REST API endpoints for frontend consumption
- TimescaleDB integration for time-series data
- Kafka message processing and publishing
- Authentication and authorization (OAuth2)
- Rate limiting and API throttling

**Key Files**:
- `src/` - Rust source code
  - `domain/` - Clean Architecture domain layer
  - `application/` - Use cases and business logic
  - `infrastructure/` - External service integrations
  - `presentation/` - HTTP controllers and middleware
- `migrations/` - Database schema migrations
- `tests/` - Unit, integration, and performance tests
- `TODO.md` - Component milestone tracking

**Claude Configuration**:
- `.claude/`
  - `.claude_rust.md` - Rust-specific development standards
  - `.claude_testing_rust.md` - Rust testing patterns

**Integration Points**:
- **protobuf-schemas**: Imports ProtoBuf message definitions
- **charting-app-js**: Provides REST API endpoints
- **TimescaleDB**: Persistent storage for market data
- **Kafka**: Message streaming for real-time data
- **OAuth2 Provider**: Authentication integration

### 4. Charting Application (Next.js)

**Repository**: `financial-data/charting-app-js/`
**Type**: Frontend Application
**Technology**: Next.js, TypeScript, React
**Status**: Active

**Purpose**: Modern web application for financial data visualization, charting, and user interaction.

**Responsibilities**:
- Interactive financial charts and visualizations
- Real-time data display with WebSocket connections
- User authentication and session management
- Responsive design for desktop and mobile
- Data export and reporting features
- User preference and portfolio management

**Key Files**:
- `src/` - TypeScript source code
  - `components/` - React components
  - `pages/` - Next.js pages and API routes
  - `hooks/` - Custom React hooks
  - `utils/` - Utility functions and helpers
  - `types/` - TypeScript type definitions
- `public/` - Static assets
- `tests/` - Component and integration tests
- `TODO.md` - Component milestone tracking

**Claude Configuration**:
- `.claude/`
  - `.claude_typescript.md` - TypeScript development standards
  - `.claude_testing_typescript.md` - Frontend testing patterns

**Integration Points**:
- **protobuf-schemas**: Imports TypeScript type definitions
- **charting-api-gw-rust**: Consumes REST API endpoints
- **WebSocket**: Real-time data streaming from backend
- **OAuth2**: User authentication flow

### 5. Client Gateway Core Library (Python)

**Repository**: `financial-data/client-gw-core-py/`
**Type**: Shared Library
**Technology**: Python 3.13+ (asyncio, Pydantic)
**Status**: Active

**Purpose**: Generic async Python library providing reusable components for building WebSocket gateway services following Clean Architecture principles.

**Responsibilities**:
- Framework-agnostic WebSocket gateway patterns
- Production-ready resilience patterns (circuit breakers, exponential backoff)
- Caching implementations (LRU, TTL)
- Connection state management
- Graceful shutdown coordination
- Observability abstractions (logging, metrics, tracing)

**Key Files**:
- `src/client_gw_core/` - Python package
  - `domain/` - Pure business logic (cache, resilience, exceptions)
  - `ports/` - Interface definitions (Protocol classes)
  - `adapters/` - Concrete implementations (observability)
  - `config/` - Configuration management
- `tests/unit/` - Unit tests
- `TODO.md` - Component milestone tracking
- `CLAUDE.md` - Component-specific instructions

**Claude Configuration**:
- `.claude/` - Component-specific overrides
- `CLAUDE.md` - Python conventions and architecture guidelines

**Integration Points**:
- **deribit-client-gw-py**: Consumed as a library dependency
- **Future exchange gateways**: Reusable for any exchange implementation

**Design Principles**:
- Zero exchange-specific dependencies
- Clean Architecture with strict layer separation
- Comprehensive test coverage (target: 95%)
- Type-safe with Python type hints

### 6. Deribit Client Gateway (Python)

**Repository**: `financial-data/deribit-client-gw-py/`
**Type**: Backend Service
**Technology**: Python 3.13+ (asyncio, websockets)
**Status**: Active

**Purpose**: Deribit exchange-specific WebSocket gateway implementation using the client-gw-core-py library.

**Responsibilities**:
- WebSocket connection to Deribit exchange
- Market data subscription and streaming
- Order book management and updates
- Trade data ingestion
- Deribit-specific message parsing
- Kafka publishing for downstream consumers

**Key Files**:
- `src/deribit_ws_gw/` - Python package
  - `domain/` - Deribit-specific domain logic
  - `adapters/` - Deribit API client, message parsers
  - `config/` - Deribit configuration (endpoints, auth)
- `tests/` - Unit and integration tests
- `TODO.md` - Component milestone tracking
- `CLAUDE.md` - Component-specific instructions

**Claude Configuration**:
- `.claude/` - Component-specific overrides
- `CLAUDE.md` - Deribit integration guidelines

**Integration Points**:
- **client-gw-core-py**: Imports core library components
- **protobuf-schemas**: Uses schemas for data serialization
- **Kafka**: Publishes market data messages
- **Deribit Exchange**: WebSocket connection for live data

**Dependencies**:
- Requires `client-gw-core-py` as a library
- Requires Kafka for message publishing
- Optional: TimescaleDB for historical data storage

### 7. Docker Orchestration (Infrastructure)

**Repository**: `financial-data/orchestrator-docker/`
**Type**: Infrastructure
**Technology**: Docker Compose
**Status**: Active

**Purpose**: Multi-service deployment orchestration for local development and testing environments.

**Responsibilities**:
- Docker Compose configuration for all services
- Service dependency management
- Volume and network configuration
- Environment-specific overrides (dev, test, staging)
- Service health checks and restart policies

**Key Files**:
- `docker-compose.yml` - Base service definitions
- `docker-compose.dev.yml` - Development overrides
- `docker-compose.test.yml` - Test environment overrides
- `docker-compose.prod.yml` - Production-like configuration
- `configs/` - Service-specific configuration files
- `scripts/` - Helper scripts (startup, teardown, logs)

**Services Managed**:
- **TimescaleDB**: PostgreSQL with TimescaleDB extension
- **Kafka + Zookeeper**: Message streaming infrastructure
- **Schema Registry**: ProtoBuf schema management
- **charting-api-gw-rust**: Rust API gateway service
- **deribit-client-gw-py**: Deribit WebSocket gateway
- **charting-app-js**: Next.js frontend application
- **Prometheus**: Metrics collection (future)
- **Grafana**: Observability dashboards (future)

**Usage Examples**:
```bash
# Start all services for development
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

# Start test environment
docker-compose -f docker-compose.test.yml up -d

# View logs for specific service
docker-compose logs -f charting-api-gw-rust

# Stop all services
docker-compose down
```

**Integration Points**:
- **All backend services**: Provides runtime environment
- **Databases and queues**: Provisions infrastructure dependencies
- **Development workflow**: Enables local multi-service testing

## Component Context Files

Each component repository contains a `.claude_component_context.md` file that links back to this project plan:

### Required Component Context Template

```markdown
# Component Context

**Project Name**: Financial Data Platform
**Component Name**: [component-name]
**Project Plan Repository**: ../project-plan (relative path)
**Component Type**: [Schema|Backend|Frontend|Tool]
**Technology**: [Primary technology stack]

## Master Configuration Location

Shared Claude configuration is in the project plan repository:
- **Path**: `../project-plan/.claude/`
- **TODO Master**: `../project-plan/TODO-MASTER.md`
- **Repositories**: `../project-plan/REPOSITORIES.md`

## Component-Specific Configuration

This component overrides master configuration with:
- `.claude/` directory with component-specific config files
- Component root `.claude*.md` files (if any)

### Loading Priority (highest to lowest)
1. Component `.claude/` directory files
2. Component root `.claude*.md` files
3. Project plan repository `.claude/` files
4. Project plan repository `CLAUDE.md`
```

## Development Workflow Across Components

### Epic and Milestone Coordination

1. **Epic Planning**: Epics are defined in project-plan repository with cross-component milestones
2. **Milestone Distribution**: Each milestone contains behaviors spanning multiple components
3. **Branch Creation**: Each component gets feature branches per behavior
4. **Task Coordination**: TODO-MASTER.md tracks progress across all components

### Example Cross-Component Epic

```text
epic-FDP-0001: Market Data Ingestion MVP

Milestone: Core Data Ingestion
├── protobuf-schemas/
│   └── feature/epic-FDP-0001-schemas-market-data-l1
├── charting-api-gw-rust/
│   ├── feature/epic-FDP-0001-ingestion-kafka-consumer
│   └── feature/epic-FDP-0001-storage-timescale-writer
└── charting-app-js/
    └── feature/epic-FDP-0001-ui-real-time-display
```

### Integration Testing

**Integration Test Repository** (Future):
```text
financial-data-integration-tests/
├── tests/
│   ├── end-to-end/        # Full system tests
│   ├── api-contracts/     # Contract testing
│   └── performance/       # Load and stress tests
├── docker-compose.yml     # Test environment setup
└── README.md
```

## API Contract Management

### Contract Storage Location

API contracts are stored in the project-plan repository:

```text
project-plan/
├── contracts/
│   ├── api-frontend/
│   │   ├── openapi.yaml         # REST API specification
│   │   └── websocket-events.md  # Real-time events
│   ├── kafka-messages/
│   │   └── market-data.proto    # Kafka message schemas
│   └── database/
│       └── schema-versions/     # Database schema evolution
```

### Contract Evolution Process

1. **Schema Changes**: Start in protobuf-schemas repository
2. **API Updates**: Update OpenAPI specification in project-plan/contracts/
3. **Implementation**: Update backend (Rust) and frontend (TypeScript) simultaneously
4. **Testing**: Verify contract compatibility with integration tests
5. **Deployment**: Coordinate deployment across all components

## Component Dependencies

### Build Order Dependencies

```text
1. protobuf-schemas (generates bindings for all languages)
      ├──[Rust]──────> charting-api-gw-rust
      ├──[Python]────> deribit-client-gw-py
      └──[TypeScript]> charting-app-js

2. client-gw-core-py (shared library)
      └──[imports]───> deribit-client-gw-py

3. Backend services provide APIs
      charting-api-gw-rust ──[REST API]──> charting-app-js
      deribit-client-gw-py ──[Kafka]────> charting-api-gw-rust
```

### Runtime Dependencies

```text
Infrastructure Layer:
  ┌─────────────┐  ┌──────────┐  ┌────────────────┐
  │ TimescaleDB │  │  Kafka   │  │ Deribit Exchange│
  └──────┬──────┘  └────┬─────┘  └────────┬───────┘
         │              │                   │
Backend Services:      │                   │
  ┌─────▼──────────────▼─────┐     ┌──────▼──────────┐
  │ charting-api-gw-rust     │     │ deribit-client- │
  │ (REST API + Kafka)       │◄────│ gw-py (WebSocket│
  └──────────────┬───────────┘     │ + Kafka pub)    │
                 │                  └─────────────────┘
                 │                           │
Frontend:        │                           │
  ┌──────────────▼───────────┐               │
  │ charting-app-js          │               │
  │ (Next.js + Charts)       │               │
  └──────────────────────────┘               │
                                              │
Orchestration:                                │
  ┌──────────────────────────────────────────▼─┐
  │ orchestrator-docker (Docker Compose)       │
  │ Manages all services + infrastructure      │
  └────────────────────────────────────────────┘
```

## Deployment Coordination

### Environment Promotion

1. **Development**: Individual component development branches
2. **Integration**: Feature branches deployed to integration environment
3. **Staging**: Release branches with coordinated component versions
4. **Production**: Tagged releases with version compatibility matrix

### Version Compatibility Matrix

| Schemas | Core Lib | API GW (Rust) | Deribit GW | Frontend | Status |
|---------|----------|---------------|------------|----------|---------|
| v1.0.0  | v0.1.0   | v1.0.0        | v0.1.0     | v1.0.0   | ✅ Stable |
| v1.1.0  | v0.1.1   | v1.0.1        | v0.1.1     | v1.0.1   | 🧪 Testing |
| v1.2.0  | v0.2.0   | v1.1.0        | v0.2.0     | v1.1.0   | 📋 Planned |

**Component Abbreviations:**
- **Schemas**: `protobuf-schemas`
- **Core Lib**: `client-gw-core-py`
- **API GW (Rust)**: `charting-api-gw-rust`
- **Deribit GW**: `deribit-client-gw-py`
- **Frontend**: `charting-app-js`
- **Orchestrator**: `orchestrator-docker` (version tracks docker-compose spec version)

## Health Checks

Each component repository should maintain:

- [ ] `.claude_component_context.md` with correct project plan reference
- [ ] `TODO.md` with current milestone progress
- [ ] Component-specific `.claude/` configuration (if needed)
- [ ] Integration with master epic tracking
- [ ] Compatible versions with other components
- [ ] Passing integration tests with dependent components