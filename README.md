# Container Workload Security Lab

A hands-on, intentionally vulnerable Docker Compose application for learning container workload security.

**Stack:** Nginx reverse proxy, Flask API, MySQL 8.4, Docker Compose, Trivy, GitHub Actions. Falco is an optional Linux-host demonstration.

> Use this lab only on your own machine or an isolated training environment. The baseline intentionally includes weak security settings and demo credentials. Do not expose it to the internet or reuse its credentials.

## Learning outcomes

By the end, learners should be able to:

- inspect containers, images, processes, ports, networks and mounts;
- scan container images and interpret Trivy findings;
- harden a container using a non-root user, dropped capabilities, read-only filesystem, `no-new-privileges` and resource limits;
- move credentials out of source-controlled configuration and explain the limits of `.env` files;
- segment container networks and avoid publishing the database port;
- explain the difference between image scanning and runtime detection;
- add an image vulnerability scan to GitHub Actions.

## Prerequisites

- Docker Desktop (Windows with WSL2 backend, macOS, or Linux Docker Engine)
- Git
- A GitHub account for Exercise 7
- Internet access to pull images and vulnerability databases
- At least 5 GB free disk space (10 GB recommended)

No separate Python or MySQL installation is required. The application runs in containers.

## Quick start

1. Copy `.env.example` to `.env`.
2. Start the intentionally insecure baseline:

   ```bash
   docker compose -f compose.baseline.yaml up --build -d
   ```

3. Open <http://localhost:8080>.
4. Check the API directly at <http://localhost:8080/api/>.
5. Inspect the deployment:

   ```bash
   docker compose -f compose.baseline.yaml ps
   docker compose -f compose.baseline.yaml logs --tail=100
   ```

The demo API stores a simple message in MySQL. It is deliberately small so the focus stays on workload security rather than application development.

## Repository map

```text
.
├── api/                         # Flask application and Dockerfile
├── db/                          # MySQL initialization
├── nginx/                       # Reverse-proxy configuration
├── .github/workflows/           # CI image scan
├── compose.baseline.yaml        # Intentionally insecure starting point
├── compose.student.yaml         # Your working copy for incremental exercises
├── compose.hardened.yaml        # Instructor reference / completed example
├── .env.example                 # Demo-only values; copy to .env
├── .gitignore
├── exercises/                   # Student exercise sheets

```

## Important Compose-file note

The lab has **two Compose files** so learners can compare states:

- `compose.baseline.yaml`: insecure starting point.
- `compose.hardened.yaml`: reference end state.

All three use the same application source and `api/Dockerfile`. Before Exercise 3, copy `compose.baseline.yaml` to `compose.student.yaml` and make your incremental changes in `compose.student.yaml`. Exercise 3 changes `api/Dockerfile` and the `api` service in that student working copy. `compose.hardened.yaml` is provided as a completed reference; try not to inspect it until you have attempted the exercises. Do not run both stacks simultaneously because they publish the same host port and use the same named volume.

To run the hardened reference:

```bash
docker compose -f compose.hardened.yaml up --build -d
```

To stop either stack:

```bash
docker compose -f compose.baseline.yaml down
# or
docker compose -f compose.hardened.yaml down
```

To remove the database volume too (destructive; deletes lab data):

```bash
docker compose -f compose.baseline.yaml down -v
```

## Exercise sequence

1. Attack-surface discovery
2. Image vulnerability scanning with Trivy
3. Container hardening
4. Secrets handling
5. Network segmentation
6. Runtime security concepts and optional Falco demonstration
7. CI/CD image scanning with GitHub Actions

See `exercises/` for student instructions.

## Troubleshooting

- **Docker daemon unavailable:** start Docker Desktop and wait until it reports that the engine is running.
- **Port 8080 already in use:** change the host side of `8080:80` in the selected Compose file.
- **Image pull/build fails:** check internet connectivity and retry `docker compose ... build`.
- **API cannot reach MySQL:** inspect `docker compose ... logs db api`; the API uses the service DNS name `db`, not `localhost`.
- **Hardened API cannot write:** the application is designed to write only to `/tmp`; check that the `tmpfs` mount exists.
- **MySQL data persists between runs:** expected; remove the named volume only when you intentionally want a clean database.

## Cleanup

```bash
docker compose -f compose.baseline.yaml down
docker compose -f compose.hardened.yaml down
```

Remove images only if you no longer need them:

```bash
docker image prune
```
