# Financial Data Platform — Agents Guide

This file provides shared guidance for agents contributing across this multi-repo project. It clarifies sources of truth, cross-repo coordination, and safety practices.

## Scope & Precedence
- Scope: Applies to the entire project root and all subdirectories.
- Precedence: If a subdirectory contains its own AGENTS.md, that file takes precedence for that subtree. Direct user/developer instructions override this file.
- Planning anchors: `project-plan/TODO-MASTER.md` is the master backlog; each repo maintains its own `TODO.md` and docs for local tasks.

## Repository Map
- `protobuf-schemas` (PBS): Canonical Protocol Buffers schemas and generation scripts.
- `project-plan` (FDP): Central plan, labels, epics, milestones, and GitHub sync workflow/scripts.
- `client-gw-core-py` (GWC): Shared Python core for websocket/HTTP plumbing, auth, and resilience used by gateway clients.
- `deribit-client-gw-py` (DBD): Deribit gateway built on client-gw-core; reference structure for exchange gateways; includes data collection notebooks/scripts.
- `okx-client-gw-py` (OKX): OKX gateway (new) modeled on deribit-client-gw-py and reusing client-gw-core; keep docs/samples/tests in step with the Deribit implementation.
- `coinbase-api-gw-py` (CBD): Coinbase gateway in Python; align patterns with other gateways; see README/TODO for scope.
- `charting-api-gw-rust` (CAG): Rust API gateway (Clean Architecture scaffold, tests present).
- `charting-app-js` (CAP): Next.js/TypeScript charting frontend (scaffold WIP).
- `orchestrator-docker` (FDO): Docker-based orchestration to run the full stack.
- `viewer-ai-js` (FDV): Placeholder AI/visualization UI scaffold (currently empty).
- `data`: Captured Deribit market data/logs for local analysis; avoid committing additional large data unless explicitly required.
- `dotenv`: Local environment file; never print or commit contents.
- `okx-api-code`: Upstream OKX reference code (`python-okx`, `okx-sample-market-maker`, `samples`) for instruction only; not part of the product stack.
- Root: Not a git repo; houses this AGENTS.md and local-only helpers.

## Source of Truth
- Schemas: `protobuf-schemas` is the single source of truth for all `.proto` files.
- Submodules: `charting-api-gw-rust/proto` and `charting-app-js/proto` are git submodules pointing to `protobuf-schemas`.
- Gateway core: Shared behaviors for exchange gateways belong in `client-gw-core-py`; keep exchange-specific repos thin where possible.
- Update Flow:
  1. Make and validate schema changes in `protobuf-schemas`.
  2. Tag/release in `protobuf-schemas` as needed.
  3. In consumer repos, update the `proto` submodule to the target commit/tag via PR.
  4. Regenerate code/artifacts in the consumer as needed (see Codegen).

## Gateway Work (Deribit -> OKX)
- Use `deribit-client-gw-py` as the reference for implementing `okx-client-gw-py`.
- Reuse `client-gw-core-py` for websocket and HTTP connections; prefer extending the core over duplicating logic.
- Consult `okx-api-code` for official OKX examples only; do not vendor it or commit sample credentials.
- Keep docs, samples, and tests in `okx-client-gw-py` aligned with the Deribit gateway patterns.

## Code Generation
- Tooling: Buf CLI (`buf.yaml`, `buf.gen.yaml`) in `protobuf-schemas` is the primary entry point.
- Scripts: Use `protobuf-schemas/scripts/*` to lint, validate breaking changes, generate language bindings (Go, Rust prost/tonic, Python), produce OpenAPI, and build docs.
- Typical sequence (run in `protobuf-schemas`):
  - Lint/validate: `scripts/lint-schemas.sh`, `scripts/validate-all-schemas.sh`
  - Breaking changes: `scripts/check-compatibility.sh`
  - Generate: `buf generate` or `scripts/generate-*.sh`
  - Docs: `scripts/generate-docs.sh` (see `generated/docs`)
- Consumers:
  - Rust gateway: Import prost/tonic outputs as needed and wire into `src/`.
  - JS app: Consume OpenAPI output or use gRPC-web approach per frontend choice.

## Local Tooling & Environments
- Languages: Rust stable (cargo, rustfmt, clippy), Node.js LTS + pnpm/npm.
- Containerization: Docker and Docker Compose for local orchestration.
- Infra (optional for dev): Kafka, PostgreSQL/TimescaleDB, Prometheus, Grafana.
- Buf CLI: Required for schema build/validation.
- Secrets: Use local `.env` files for development; never commit secrets.

## Branching, PRs, and Conventions
- Branch names: `feature/epic-<CODE>-NNNN-description`, `refactor/epic-<CODE>-NNNN-description`, `fix/epic-<CODE>-NNNN-description`, `test/epic-<CODE>-NNNN-description`, `docs/epic-<CODE>-NNNN-description` where `<CODE>` is the repo's three-letter code; codes: PBS, FDP, GWC, DBD, OKX, CBD, CAG, CAP, FDO, FDV.
- One logical change per repo per PR; link cross-repo changes via issues/milestones in `project-plan`.
- Commit messages: Conventional style, e.g., `feat(api): add candle endpoint`, `fix(proto): reserve field 12`.
- Tests: Extend/add tests when changing behavior or contracts.
- Submodule bumps: PRs should state which schema tag/commit is targeted and why.

## Security & Compliance
- Do not commit secrets (tokens, passwords, API keys). Use repo/org Secrets for automation.
- Rotate any exposed credentials immediately and purge from history if discovered.
- Enforce schema compatibility checks to reduce breaking downstream consumers.
- Respect dependency licenses and maintain required attributions.

## Agent Operating Guidelines
- Scope control: Avoid changing multiple repos in one patch unless explicitly requested.
- Minimal diffs: Keep changes focused; avoid unrelated refactors or renames.
- Safety: Avoid network access, builds, or destructive operations unless requested. Do not print or log contents of `.env` files.
- Confirmation: In restricted environments, confirm with the user before writing files or running long commands.
