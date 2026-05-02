# Git Workflow

## Principle

Use real, periodic commits that match actual development progress. The goal is not to create a perfect-looking history, but a believable working history for an Informatiker HF student: small steps, occasional fixes, clear messages, and regular pushes.

Avoid fake backdated commits. A reviewer will learn more from honest progress than from a polished but artificial timeline.

## Branch Model

- `main`: stable, runnable state
- `codex/setup-project`: initial structure and documentation
- `codex/backend-api`: backend domain, database, and REST API
- `codex/frontend-ui`: Angular screens and API integration
- `codex/prediction-service`: Python category and spending prediction
- `codex/infra-deployment`: Docker Compose and Kubernetes manifests

Feature branches should be merged into `main` after tests pass and the feature is demonstrable.

## Commit Cadence

Recommended rhythm:

- Commit after every focused work block of 45 to 90 minutes
- Push at least once per workday
- Push immediately after finishing a milestone or before switching machines
- Keep commits small enough that each one can be explained in one sentence

This creates a realistic pattern: several commits on active project days, no commits on busy school/work days, and occasional follow-up fixes.

## Example Timeline

### Week 1: Foundation

Push 1:

```text
docs: add project vision and feature scope
chore: create initial repository structure
docs: document planned git workflow
```

Push 2:

```text
chore: scaffold spring boot backend
chore: scaffold angular frontend
chore: add python prediction service placeholder
```

### Week 2: Backend Basics

Push 3:

```text
feat(backend): add transaction and category entities
feat(backend): configure postgres persistence
test(backend): add repository tests for transactions
```

Push 4:

```text
feat(backend): expose transaction crud endpoints
docs(api): add openapi configuration
fix(backend): validate negative transaction amounts
```

### Week 3: CSV Import

Push 5:

```text
feat(backend): parse transaction csv uploads
feat(backend): store import jobs and validation errors
test(backend): cover csv import edge cases
```

Push 6:

```text
fix(backend): handle duplicate csv rows during import
docs: add sample csv import format
```

### Week 4: Frontend Transactions

Push 7:

```text
feat(frontend): add transaction list page
feat(frontend): add csv import form
feat(frontend): connect transaction api client
```

Push 8:

```text
fix(frontend): show import validation errors
test(frontend): add transaction service tests
```

### Week 5: Budgets and Alerts

Push 9:

```text
feat(backend): add monthly budgets
feat(backend): calculate budget warning thresholds
test(backend): cover budget warning service
```

Push 10:

```text
feat(frontend): show budget warnings on dashboard
feat(backend): schedule daily budget checks
```

### Week 6: Subscriptions and Charts

Push 11:

```text
feat(backend): detect recurring subscription payments
feat(frontend): add subscription review screen
test(backend): cover subscription detection rules
```

Push 12:

```text
feat(frontend): add monthly spending charts
feat(backend): add monthly report endpoint
```

### Week 7: Prediction and External APIs

Push 13:

```text
feat(prediction): suggest categories from merchant names
feat(backend): call prediction service for imports
test(prediction): add category rule tests
```

Push 14:

```text
feat(backend): add exchange rate client
feat(backend): integrate mock banking api
test(backend): mock external api responses
```

### Week 8: Deployment and Polish

Push 15:

```text
chore(infra): add docker compose development stack
chore(infra): add kubernetes manifests
docs: document local development setup
```

Push 16:

```text
test: add final integration test coverage
docs: add demo script and screenshots
chore: prepare final presentation version
```

## Commit Message Style

Use a simple conventional format:

```text
type(scope): short action in present tense
```

Good examples:

```text
feat(backend): add budget warning endpoint
fix(frontend): keep chart labels readable on mobile
test(backend): cover duplicate csv imports
docs: explain docker compose setup
chore(infra): add postgres service
```

Useful types:

- `feat`: new user-visible functionality
- `fix`: bug fix
- `test`: test-only change
- `docs`: documentation
- `chore`: project setup, tooling, infrastructure
- `refactor`: code restructuring without behavior change

## What Looks Realistic

Realistic student history usually has:

- Small commits with clear intent
- A few fix commits after testing
- Documentation updated near the feature it describes
- Tests added gradually, not only at the end
- Pushes grouped by work sessions
- Branch names that match the milestone being worked on

Less realistic history usually has:

- One huge commit containing the full project
- Dozens of tiny commits made within a few minutes
- Perfectly even commit timing every day
- No fixes, tests, or documentation changes
- Commit messages that do not explain the work

