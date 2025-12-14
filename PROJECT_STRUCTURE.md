# Financial Data Platform - Project Structure Overview

## 🎯 Quick Start

When starting a new Claude Code session in this multi-repo project:

1. **Location**: `/home/skingham/Projects/Quantfidential/financial-data/`
2. **Read first**: `CLAUDE.md` (project startup instructions)
3. **Check status**: `project-plan/TODO-MASTER.md` (current epic progress)
4. **Review config**: `project-plan/.claude/` (shared standards)

## 📦 Repository Architecture

This is a **multi-repository monolith** with 7 separate git repositories organized in a single parent directory:

```text
financial-data/                          # Parent directory (NOT a git repo)
│
├── 📋 Coordination & Configuration
│   └── project-plan/                   # Master coordination repository
│
├── 📜 Schemas & Contracts
│   └── protobuf-schemas/               # Data schema definitions
│
├── 🔧 Backend Services
│   ├── charting-api-gw-rust/          # Rust API gateway
│   ├── client-gw-core-py/             # Python WebSocket core library
│   └── deribit-client-gw-py/          # Python Deribit gateway
│
├── 🎨 Frontend Applications
│   └── charting-app-js/               # Next.js charting app
│
└── 🐳 Infrastructure
    └── orchestrator-docker/           # Docker Compose orchestration
```

## 🏗️ Component Relationships

### Data Flow

```text
External Exchange (Deribit)
          ↓ WebSocket
    deribit-client-gw-py
          ↓ Kafka
          ├──> charting-api-gw-rust ←─ TimescaleDB
          │           ↓ REST API
          │    charting-app-js
          │
          └──> (Future: other consumers)
```

### Build Dependencies

```text
protobuf-schemas ──generates──> Rust/Python/TypeScript bindings
                                         ↓
client-gw-core-py ──library──> deribit-client-gw-py
                                         ↓
                               All services use generated types
```

### Epic Coordination

```text
project-plan/TODO-MASTER.md (Master)
          ├──> protobuf-schemas/TODO.md
          ├──> charting-api-gw-rust/TODO.md
          ├──> client-gw-core-py/TODO.md
          ├──> deribit-client-gw-py/TODO.md
          └──> charting-app-js/TODO.md
```

## 📚 Configuration Hierarchy

### Loading Order (Highest to Lowest Priority)

1. **Component-specific configuration** (in each repo):
   ```
   component/.claude/settings.local.json     # Permissions
   component/.claude/*.md                    # Component overrides
   component/CLAUDE.md                       # Component instructions
   component/.claude_component_context.md    # Links to project-plan
   ```

2. **Shared project standards** (in project-plan):
   ```
   project-plan/.claude/
   ├── .claude_principles.md           # Engineering principles
   ├── .claude_git_standards.md        # Git quality standards
   ├── .claude_project_structure.md    # Project organization
   ├── .claude_testing.md              # Testing standards
   └── .claude_workflow.md             # Development workflow
   ```

3. **Root configuration**:
   ```
   CLAUDE.md                           # Startup instructions
   .claude/settings.local.json         # Project-wide permissions
   ```

## 🔍 Navigation Guide

### When You Start in Root Directory

```bash
# 1. Check overall project status
cat project-plan/TODO-MASTER.md

# 2. See all components
cat project-plan/REPOSITORIES.md

# 3. Load shared standards
ls project-plan/.claude/

# 4. Navigate to specific component
cd charting-api-gw-rust
```

### When You Start in a Component Directory

```bash
# 1. Find component context
cat .claude_component_context.md

# 2. Check component status
cat TODO.md

# 3. See component-specific config
cat CLAUDE.md
ls .claude/

# 4. Find master plan
cd ../project-plan
cat TODO-MASTER.md
```

## 🧩 Component Details

### 1. Project Plan (`project-plan/`)

**Purpose**: Master coordination
**Technology**: Markdown documentation
**Key Files**:
- `CLAUDE.md` - Project configuration
- `REPOSITORIES.md` - Component definitions
- `TODO-MASTER.md` - Cross-component epic tracking
- `.claude/` - Shared configuration standards

**When to work here**:
- Epic planning spanning multiple components
- API contract definition and evolution
- Cross-component coordination
- Documentation updates

### 2. ProtoBuf Schemas (`protobuf-schemas/`)

**Purpose**: Data type definitions
**Technology**: Protocol Buffers v3
**Key Files**:
- `market/v1/*.proto` - Market data schemas
- `reference/v1/*.proto` - Reference data schemas
- `generated/` - Language bindings

**When to work here**:
- Adding new data types
- Evolving existing schemas
- Regenerating language bindings
- Schema validation

### 3. Charting API Gateway - Rust (`charting-api-gw-rust/`)

**Purpose**: REST API and backend services
**Technology**: Rust (axum, tokio, sqlx)
**Architecture**: Clean Architecture
**Key Directories**:
- `src/domain/` - Business entities
- `src/application/` - Use cases
- `src/infrastructure/` - External integrations
- `src/presentation/` - HTTP controllers

**When to work here**:
- REST API endpoint development
- Database integration (TimescaleDB)
- Business logic implementation
- Performance optimization

### 4. Client Gateway Core - Python (`client-gw-core-py/`)

**Purpose**: Reusable WebSocket gateway library
**Technology**: Python 3.13+ (asyncio)
**Architecture**: Clean Architecture (Domain/Ports/Adapters)
**Key Directories**:
- `src/client_gw_core/domain/` - Core logic
- `src/client_gw_core/ports/` - Interfaces
- `src/client_gw_core/adapters/` - Implementations

**When to work here**:
- Adding resilience patterns
- Cache implementations
- Framework-agnostic gateway components
- Shared library features

### 5. Deribit Gateway - Python (`deribit-client-gw-py/`)

**Purpose**: Deribit exchange WebSocket client
**Technology**: Python 3.13+ (asyncio, websockets)
**Dependencies**: client-gw-core-py
**Key Directories**:
- `src/deribit_ws_gw/domain/` - Deribit-specific logic
- `src/deribit_ws_gw/adapters/` - API client, parsers

**When to work here**:
- Deribit API integration
- Market data ingestion
- WebSocket connection management
- Exchange-specific features

### 6. Charting App - Next.js (`charting-app-js/`)

**Purpose**: Web UI for data visualization
**Technology**: Next.js, TypeScript, React
**Key Directories**:
- `src/components/` - React components
- `src/pages/` - Next.js pages
- `src/hooks/` - Custom hooks
- `src/types/` - TypeScript types

**When to work here**:
- UI/UX development
- Chart components
- API client integration
- Frontend features

### 7. Docker Orchestration (`orchestrator-docker/`)

**Purpose**: Multi-service deployment
**Technology**: Docker Compose
**Key Files**:
- `docker-compose.yml` - Base configuration
- `docker-compose.dev.yml` - Development overrides
- `docker-compose.test.yml` - Testing environment

**When to work here**:
- Service orchestration
- Local development environment
- Integration testing setup
- Infrastructure configuration

## 🚀 Development Workflows

### Working on a Single Component

```bash
# 1. Navigate to component
cd charting-api-gw-rust

# 2. Check current work
cat TODO.md

# 3. Create behavior branch
git checkout -b feature/epic-FDP-0001-rest-endpoints

# 4. TDD: Write test first
# 5. Implement feature
# 6. Commit and push
# 7. Create PR
# 8. Update TODO.md after merge
```

### Working Across Multiple Components

```bash
# 1. Start in project-plan
cd project-plan
cat TODO-MASTER.md

# 2. Update API contract
# Edit contracts/api-frontend/openapi.yaml

# 3. Implement in backend
cd ../charting-api-gw-rust
git checkout -b feature/epic-FDP-0001-api-update

# 4. Update frontend
cd ../charting-app-js
git checkout -b feature/epic-FDP-0001-api-update

# 5. Coordinate PRs and update TODO-MASTER.md
```

### Adding a New Schema

```bash
# 1. Define schema
cd protobuf-schemas
# Edit market/v1/new_schema.proto

# 2. Generate bindings
./scripts/generate-bindings.sh

# 3. Update consumers
cd ../charting-api-gw-rust
# Import new generated types

cd ../charting-app-js
# Import new TypeScript types

# 4. Update TODO-MASTER.md with cross-component progress
```

## 🧪 Testing Strategy

### Test Pyramid Distribution

- **Unit Tests**: 70% (fast, isolated)
- **Integration Tests**: 20% (real dependencies in containers)
- **E2E Tests**: 10% (full system)

### Running Tests by Component

```bash
# Rust
cd charting-api-gw-rust
cargo test

# Python
cd client-gw-core-py
PYTHONPATH=src pytest

# TypeScript
cd charting-app-js
npm test
```

## 📊 Epic Tracking System

### Hierarchy

```
Epic (1-3 months)
  └── Milestone (1-2 weeks)
      └── Behavior (1-3 days)
          └── Task (hours)
```

### Example Epic Flow

```markdown
## Epic: epic-FDP-0001 - Initial API Gateway MVP

### Milestone 1: Schema Definition
- [x] Define L1 market data schema (protobuf-schemas)
- [x] Define candle data schema (protobuf-schemas)
- [x] Validate with protoc (protobuf-schemas)

### Milestone 2: API Implementation
- [ ] Load candle data from files (charting-api-gw-rust)
- [ ] REST endpoint for candles (charting-api-gw-rust)
- [ ] Error handling (charting-api-gw-rust)

### Milestone 3: Frontend Display
- [ ] Charting component (charting-app-js)
- [ ] API integration (charting-app-js)
- [ ] Real-time updates (charting-app-js)
```

## 🔧 Technology Stack Summary

| Component | Language | Framework | Database | Messaging |
|-----------|----------|-----------|----------|-----------|
| protobuf-schemas | ProtoBuf | - | - | - |
| charting-api-gw-rust | Rust | axum, tokio | TimescaleDB | Kafka |
| client-gw-core-py | Python 3.13+ | asyncio | - | - |
| deribit-client-gw-py | Python 3.13+ | asyncio, websockets | - | Kafka |
| charting-app-js | TypeScript | Next.js, React | - | WebSocket |
| orchestrator-docker | YAML | Docker Compose | All | All |

## 🎓 Key Principles

### Financial Data Accuracy
- ✅ Use `Decimal` types for money (never floats)
- ✅ Dual timestamps (event_time, ingestion_time)
- ✅ Nanosecond precision for market data
- ✅ ISO 4217 currency codes

### Clean Architecture
- ✅ Domain layer has no external dependencies
- ✅ Dependencies point inward
- ✅ Ports & Adapters pattern
- ✅ Immutable value objects

### Test-Driven Development
- ✅ Red-Green-Refactor cycle
- ✅ Write tests first
- ✅ Unit tests are fast (< 100ms)
- ✅ Integration tests use real dependencies

### Git Quality
- ✅ Branch naming: `type/epic-CODE-NNNN-description`
- ✅ Conventional commits
- ✅ Squash and merge PRs
- ✅ Keep PRs small (< 400 lines)

## 📖 Essential Reading

When starting work, read these in order:

1. **`/CLAUDE.md`** - Startup instructions
2. **`project-plan/TODO-MASTER.md`** - Current status
3. **`project-plan/REPOSITORIES.md`** - Component details
4. **`project-plan/.claude/.claude_principles.md`** - Engineering principles
5. **`project-plan/.claude/.claude_workflow.md`** - Development workflow
6. **Component-specific `CLAUDE.md`** - When working in a component

## 🆘 Common Scenarios

### "I need to add a new data type"
→ Start in `protobuf-schemas/`, define schema, generate bindings, update consumers

### "I need to add a new API endpoint"
→ Work in `charting-api-gw-rust/`, check API contract in `project-plan/contracts/`

### "I need to fix a cross-component bug"
→ Start in `project-plan/`, review TODO-MASTER.md, coordinate fixes across repos

### "I need to add a new feature to the UI"
→ Work in `charting-app-js/`, ensure API support in `charting-api-gw-rust/`

### "I need to test the full system locally"
→ Use `orchestrator-docker/`, run `docker-compose up -d`

## 🔍 Search Tips for Claude Code

### Finding specific code
```bash
# Use Grep across all components from root
grep -r "CandleData" --include="*.rs" --include="*.py" --include="*.ts"

# Use Glob to find files
find . -name "*candle*" -type f
```

### Understanding cross-component flow
1. Start with schema in `protobuf-schemas/`
2. Follow generated bindings to consumers
3. Check API contracts in `project-plan/contracts/`
4. Trace through backend → frontend

## ✅ Health Checks

Before starting significant work:

- [ ] All repos on main/master branch
- [ ] All branches up-to-date with origin
- [ ] TODO files reflect current status
- [ ] Tests passing locally
- [ ] Docker services can start successfully
- [ ] No unresolved merge conflicts

## 🎯 Next Steps

1. **If you're new**: Read `CLAUDE.md` and this file
2. **Starting work**: Check `project-plan/TODO-MASTER.md`
3. **Daily routine**: Update TODO files as you progress
4. **Cross-component work**: Coordinate via TODO-MASTER.md
5. **Questions**: Check `.claude_principles.md` for guidance

---

**Last Updated**: 2025-12-02
**Maintained By**: Development team
**Questions**: See individual component CLAUDE.md files
