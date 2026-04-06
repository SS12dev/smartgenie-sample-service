# `smartgenie-sample-service`

A small SmartGenie-style **multi-service application repo** for validating monorepo CI/CD and GitOps patterns.

## Repo layout
```text
smartgenie-sample-service/
├── services/
│   ├── agent-assistant/
│   └── agent-analytics/
├── .github/workflows/
├── requirements-dev.txt
└── pyproject.toml
```

## Included services
### `agent-assistant`
- conversation-facing sample agent
- endpoints: `/`, `/health`, `/respond`

### `agent-analytics`
- analytics/insights sample agent
- endpoints: `/`, `/health`, `/metrics`

## Dependency model
- root `requirements-dev.txt` -> shared dev/test tooling
- `services/*/requirements.txt` -> runtime dependencies for each service container

## Local run examples
```powershell
python .\services\agent-assistant\app.py
python .\services\agent-analytics\app.py
```

## Local Docker build examples
```powershell
docker build -t smartgenie-agent-assistant:local .\services\agent-assistant
docker build -t smartgenie-agent-analytics:local .\services\agent-analytics
```

## CI/CD intent
- run quality gates for pull requests
- validate Docker builds for each service independently
- publish environment-specific images for each service from the same repo

This structure better reflects the SmartGenie pattern where multiple related service containers can live in one repo.
