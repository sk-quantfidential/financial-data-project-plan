# Project Plan — Agents Guide

## Purpose
- Central source-of-truth for epics, milestones, labels, and repo mappings.
- Automates syncing to target repos via GitHub workflow and script.

## Structure
- `project-config/epics.yml` — High-level epics.
- `project-config/milestones/*.yml` — Per-repo milestones.
- `project-config/labels.yml` — Shared labels.
- `project-config/repos.yml` — Target repositories + mappings.
- `.github/workflows/sync-projects.yml` + `.github/scripts/sync_projects.py` — Sync automation.

## Sync Workflow
- Trigger via workflow dispatch or on push; uses `GH_TOKEN` secret.
- Capabilities: create/update labels, milestones, and issues across repos.

## Secrets
- Use repo/org secret `GH_TOKEN` with minimal scopes (e.g., `repo`).
- Never commit tokens or secrets; rotate immediately if exposure is suspected.

## Change Process
- Propose changes to YAML configs via PR.
- Validate YAML structure and cross-repo mappings before merge.
- Link related implementation PRs across repos for traceability.

## Safety & Conventions
- Keep automation idempotent; avoid destructive changes.
- Document any manual steps needed for org-level changes.
- Conventional commits and descriptive PRs referencing epics/milestones.

