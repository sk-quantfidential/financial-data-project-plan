# Financial Data Platform - Claude Code Startup Instructions

## Project Root Configuration

**Multi-Repo Project Root**: `/home/skingham/Projects/Quantfidential/financial-data`

## Startup Sequence

When Claude Code starts in this directory, execute the following sequence:

### 1. Load Project Configuration
- **Primary Config**: Read `.claude/settings.local.json` for project permissions and structure
- **Project Plan Configs**: Read file `./project-plan/CLAUDE.md` for project configuration (if exists)
- **Supporting Configs**: Read all files in `./project-plan/.claude/` for supporting configuration files (if exists)

### 2. Load Project Status
- **Master TODO**: Read `./project-plan/TODO-MASTER.md`
- **Report Current Status**: Provide a comprehensive project status summary including:
  - Current epic progress
  - Completed milestones
  - Next priority tasks
  - Overall project health

### 3. Expected Output Format
Provide a concise but complete status report covering:
- **Project Overview**: Name, type, architecture, current phase
- **Epic Progress**: Current epic with milestone completion status
- **Completed Work**: Key achievements and delivered components
- **Current Priority**: What should be worked on next
- **Key Metrics**: Test coverage, component status, infrastructure readiness

## Configuration File Locations

Based on the actual project structure:
- **Project Root**: `/home/skingham/Projects/Quantfidential/financial-data/`
- **Master Configuration**: `.claude/settings.local.json`, `./project-plan/.claude`
- **Project Plan**: `./project-plan/` directory
- **Master TODO**: `./project-plan/TODO-MASTER.md`
- **Project Documentation**: `./project-plan/CLAUDE.md`, `./project-plan/REPOSITORIES.md`

## Error Handling

If any configuration files are missing:
- **Don't assume paths**: Use actual directory exploration to find correct paths
- **Report actual structure**: Show what files/directories actually exist
- **Graceful degradation**: Provide status based on available information

## Multi-Component Context

This is a **multi-component project** with 7 separate git repositories:

### Backend Services
- **charting-api-gw-rust**: Rust-based API gateway and backend services (axum, tokio, sqlx)
- **client-gw-core-py**: Python async WebSocket gateway core library (framework-agnostic)
- **deribit-client-gw-py**: Python Deribit exchange WebSocket gateway implementation

### Frontend Applications
- **charting-app-js**: Next.js frontend application for data visualization

### Infrastructure & Configuration
- **protobuf-schemas**: Protocol Buffer schema definitions for all financial data types
- **orchestrator-docker**: Docker Compose orchestration for multi-service deployment
- **project-plan**: Master project coordination, epic tracking, and shared configuration

### Component Configuration Hierarchy

Each component may have its own configuration that overrides the master project configuration:

1. **Component-specific** (highest priority):
   - `.claude_component_context.md` - Links back to project plan
   - `.claude/` directory - Component-specific overrides
   - Component root `.claude*.md` files

2. **Shared project standards** (in `project-plan/.claude/`):
   - Engineering principles
   - Git quality standards
   - Testing standards
   - Workflow standards

3. **Root configuration** (this file) - Base project setup

## Development Environment

- **Python Environment**: 3.13+ (`py313_financial_data_dev` conda environment)
- **Rust Version**: 1.87+
- **Node Version**: 22.18+
- **Container Platform**: Docker Compose for orchestration
- **Testing**: TDD approach with comprehensive coverage requirements

## Startup Command Pattern

When starting in this directory, Claude Code should automatically:
1. Detect this is the financial-data multi-repo project root
2. Load all relevant configuration files
3. Present current project status from TODO-MASTER.md
4. Be ready to work on the current priority tasks

This behavior should be consistent across all future Claude Code sessions in this directory.
