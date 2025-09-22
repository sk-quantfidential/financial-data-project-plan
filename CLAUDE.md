# Project Configuration

## Project: Financial Data Platform

**Project Code**: FDP
**Type**: Multi-component
**Architecture**: Clean Architecture
**Created**: 2024-09-13
**Status**: Active
**From Template**: claude-defaults v1.0

## Configuration Files

This project follows the configuration defined in these files:

### Core Philosophy & Principles

- `.claude/.claude_principles.md` - Engineering philosophy and core beliefs
- `.claude/.claude_personal.md` - Personal/team preferences and style

### Architecture & Design

- `.claude/.claude_architecture.md` - Clean Architecture rules and layer definitions
- `.claude/.claude_solid.md` - SOLID principles and refactoring guidelines
- `.claude/.claude_code_style.md` - Architecture code conventions

### Development Process

- `.claude/.claude_workflow.md` - Git workflow, epic-milestone-behavior-task hierarchy
- `.claude/.claude_testing.md` - TDD approach and testing standards
- `.claude/.claude_todo.md` - TODO file structure and milestone tracking

### Repository & Structure

- `.claude/.claude_init.md` - Project initialization procedures
- `.claude/.claude_repository.md` - Repository structure standards
- `.claude/.claude_cross_component.md` - Multi-component development coordination
- `REPOSITORIES.md` - Component repository definitions and context

### Language-Specific Configurations

- `.claude/.claude_rust.md` - Rust standards (charting-api-gw-rust)
- `.claude/.claude_testing_rust.md` - Rust testing standards
- `.claude/.claude_typescript.md` - TypeScript standards (charting-app-js)
- `.claude/.claude_testing_typescript.md` - TypeScript testing standards
- `.claude/.claude_protobuf_schemas.md` - Protocol Buffers standards
- `.claude/.claude_testing_protobuf_schemas.md` - ProtoBuf testing standards
- `.claude/.claude_python.md` - Python standards (tooling/scripts)
- `.claude/.claude_testing_python.md` - Python testing standards

### Data Services & Infrastructure

- `.claude/.claude_postgresql.md` - PostgreSQL/TimescaleDB standards
- `.claude/.claude_testing_postgresql.md` - Database testing standards

## Project-Specific Configuration

### Project-Specific Rules

**Financial Data Accuracy Requirements:**
- All monetary calculations must use `rust_decimal::Decimal` type (Rust) or equivalent precision types
- No floating-point arithmetic for financial values
- All timestamps must include nanosecond precision for market data
- Currency codes must follow ISO 4217 standard

**Schema-First Development:**
- ProtoBuf schemas define canonical data models in `protobuf-schemas/` repository
- All API contracts derived from ProtoBuf definitions
- Schema evolution must maintain backward compatibility
- Field deprecation follows ProtoBuf best practices with reserved tags

**Regulatory Compliance:**
- All data ingestion must include audit trails with source metadata
- Data lineage tracking required for all transformations
- Retention policies must be configurable per data type
- All user actions must be logged for compliance auditing

**Performance Requirements:**
- Market data ingestion must support sub-millisecond latencies
- API responses must complete within 100ms for cached data
- Database queries must be optimized for time-series patterns
- Real-time data feeds require back-pressure handling

**Multi-Asset Support:**
- System must be extensible to new asset classes without schema breaking changes
- Instrument identification must support multiple identifier types
- Market microstructure differences must be abstracted in domain layer

### Project-Specific Overrides

**Branch Naming Convention:**
- Epic naming: `epic-FDP-XXXX` (where XXXX is four-digit number)
- All branches follow: `type/epic-FDP-XXXX-milestone-behavior-description`
- Examples:
  - `feature/epic-FDP-0001-market-data-l1-ingestion`
  - `feature/epic-FDP-0001-api-rest-endpoints`
  - `refactor/epic-FDP-0002-domain-value-objects`

**Component Coordination:**
- Master epic tracking in `project-plan/TODO-MASTER.md`
- Component-specific tasks in each repository's `TODO.md`
- Cross-component integration tests in dedicated test repository
- API contracts stored in `project-plan/contracts/`

## Component Repositories

See `REPOSITORIES.md` for detailed component information including:

- **protobuf-schemas**: Schema definitions for all financial data types
- **charting-api-gw-rust**: Rust-based API gateway and backend services
- **charting-app-js**: Next.js frontend application for data visualization

Each component repository contains:
- `.claude_component_context.md` - Links back to this project plan
- `.claude/` directory - Component-specific configuration overrides
- `TODO.md` - Component milestone and task tracking

## Quick Start for Claude Code

When starting work:

1. **In Project Plan Repository** (this repository):
   ```bash
   cd project-plan
   claude-code "Review epic-FDP-0001 milestone progress and plan next behaviors"
   ```

2. **In Component Repository**:
   ```bash
   cd charting-api-gw-rust
   claude-code "Implement L1 market data ingestion for Core Data milestone in epic-FDP-0001"
   ```

3. **Cross-Component Work**:
   ```bash
   cd project-plan
   claude-code "Coordinate API contract changes across charting-api-gw-rust and charting-app-js for epic-FDP-0001"
   ```

## Configuration Precedence

When rules conflict:

1. **Project-specific overrides** (this file) - highest priority
2. **Component-specific configuration** (`.claude/` in component repos)
3. **Language-specific configuration** (`.claude_rust.md`, `.claude_typescript.md`, etc.)
4. **Architecture configuration** (`.claude_architecture.md`, `.claude_solid.md`)
5. **Personal/team preferences** (`.claude_personal.md`)
6. **Core principles** (`.claude_principles.md`) - lowest priority (but rarely overridden)

## Project Root Detection

### Multi-Component Project Structure

**When in Project Plan Repository:**
```text
financial-data/project-plan/
├── .claude/           # Master configuration
├── CLAUDE.md          # This file
├── REPOSITORIES.md    # Component definitions
├── TODO-MASTER.md     # Cross-component milestone tracking
└── contracts/         # API contract definitions
```

**When in Component Repository:**
```text
financial-data/charting-api-gw-rust/
├── .claude_component_context.md  # Required: Links to project plan
├── .claude/                      # Optional: Component-specific overrides
│   ├── .claude_rust.md          # Component Rust standards override
│   └── .claude_deployment.md    # Deployment-specific rules
├── src/
├── tests/
└── TODO.md                       # Component milestone tracking
```

**Configuration Discovery Rules:**

1. **Project Plan Repository Detection**:
   - ✅ Scan: `CLAUDE.md` + `REPOSITORIES.md` + `.claude/`
   - ✅ Load: All `.claude/*.md` configuration files
   - ❌ Never scan: `.claude-defaults/` (templates only)

2. **Component Repository Detection**:
   - ✅ Required: `.claude_component_context.md` (component marker)
   - ✅ Load: Project plan configuration from linked path
   - ✅ Override: Component `.claude/` files (if present)
   - ✅ Override: Component root `.claude*.md` files

## Technology Stack Integration

**Backend Services (Rust):**
- Use `tokio` for async runtime
- `axum` for HTTP routing
- `sqlx` for database interactions
- `serde` + `prost` for ProtoBuf serialization
- `rust_decimal` for financial calculations

**Frontend Application (Next.js/TypeScript):**
- React 18+ with TypeScript 5+
- TanStack Query for API state management
- Tailwind CSS for styling
- Chart.js or D3.js for financial visualizations

**Data Layer (PostgreSQL/TimescaleDB):**
- TimescaleDB extension for time-series optimization
- Connection pooling with pgBouncer
- Schema migrations via `sqlx-cli`
- Backup strategies for financial data compliance

**Message Streaming (Kafka):**
- Schema Registry integration with ProtoBuf schemas
- Dead letter queues for error handling
- Partitioning strategy for market data distribution
- Consumer group management for scalability

## Health Checks

Before starting work, verify:

- [ ] Current epic and milestone identified (TODO-MASTER.md or component TODO.md)
- [ ] Component context understood (if working in component repo)
- [ ] Branch follows epic naming convention
- [ ] ProtoBuf schemas are up-to-date
- [ ] Database migrations are current
- [ ] Tests passing on main branch
- [ ] API contracts are synchronized across components

## Development Workflow

1. **Epic Planning**: Break features into milestones spanning components
2. **Milestone Coordination**: Plan behaviors across component repositories
3. **Component Implementation**: Create behavior branches in each relevant component
4. **API Contract Management**: Update contracts in project-plan before implementation
5. **Integration Testing**: Verify cross-component functionality
6. **Documentation**: Update component README files and API documentation