# Component Repositories

## Project: Financial Data Platform (FDP)

This document defines the component repositories that make up the Financial Data Platform multi-component project.

## Repository Structure

```text
Financial Data Platform
├── project-plan/              # This repository - master coordination
├── protobuf-schemas/          # Protocol Buffer schema definitions
├── charting-api-gw-rust/      # Rust API gateway and backend services
└── charting-app-js/           # Next.js frontend application
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
protobuf-schemas (generates bindings)
    ↓
charting-api-gw-rust (consumes Rust bindings)
    ↓
charting-app-js (consumes TypeScript types + API)
```

### Runtime Dependencies

```text
TimescaleDB ← charting-api-gw-rust ← charting-app-js
     ↑               ↑
   Kafka      OAuth2 Provider
```

## Deployment Coordination

### Environment Promotion

1. **Development**: Individual component development branches
2. **Integration**: Feature branches deployed to integration environment
3. **Staging**: Release branches with coordinated component versions
4. **Production**: Tagged releases with version compatibility matrix

### Version Compatibility Matrix

| protobuf-schemas | charting-api-gw-rust | charting-app-js | Status |
|------------------|---------------------|-----------------|---------|
| v1.0.0           | v1.0.0              | v1.0.0          | ✅ Stable |
| v1.1.0           | v1.0.1              | v1.0.1          | 🧪 Testing |
| v1.2.0           | v1.1.0              | v1.1.0          | 📋 Planned |

## Health Checks

Each component repository should maintain:

- [ ] `.claude_component_context.md` with correct project plan reference
- [ ] `TODO.md` with current milestone progress
- [ ] Component-specific `.claude/` configuration (if needed)
- [ ] Integration with master epic tracking
- [ ] Compatible versions with other components
- [ ] Passing integration tests with dependent components