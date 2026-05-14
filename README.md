# core_api

Python-based utility service used for CVE remediation and SBOM validation testing.

## Features

- Dockerized Python application
- Config-driven execution
- Report generation support
- Test coverage
- Security scanning validation

## Project Structure

```text
app/        Application modules
config/     YAML configuration files
data/       Sample input data
scripts/    Helper scripts
tests/      Unit tests
```

## Vulnerable Dependency

| Package | Version | CVE |
|----------|----------|------|
| onnx | 1.20.0 | CVE-2026-34447 |

## Build Image

```bash
docker build -t core_api .
```

## Run Container

```bash
docker run -p 8080:8080 core_api
```

## API Endpoint

```bash
GET /health
```

## Security Notes

This repository intentionally includes a vulnerable dependency for:
- CVE remediation workflows
- SBOM testing
- Security scan validation
- Automated upgrade demonstrations

Recommended remediation:
```bash
onnx >= 1.21.0
```
