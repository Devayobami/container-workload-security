# Exercise 1 — Discover the container attack surface

## Objective
Inspect the baseline deployment and identify its exposed interfaces, privileges, processes, networks, mounts and sensitive configuration.

## Start
```bash
cp .env.example .env
docker compose -f compose.baseline.yaml up --build -d
```

Browse to `http://localhost:8080` and `http://localhost:8080/api/db`.

## Tasks
1. List running containers and published ports:
   ```bash
   docker compose -f compose.baseline.yaml ps
   docker ps --format "table {{.Names}}\t{{.Ports}}"
   ```
2. Inspect the API and database:
   ```bash
   docker inspect <container_name>
   docker top <container_name>
   docker logs --tail=50 <container_name>
   ```
3. Inspect networks and mounts:
   ```bash
   docker network ls
   docker network inspect <network_name>
   docker inspect <container_name> --format '{{json .Mounts}}'
   ```
4. Record which services are reachable from the host and which should be internal.

## Questions
- Why is publishing MySQL port 3306 unnecessary for this application?
- Which user runs the API process?
- Which credentials or configuration values could be exposed to someone with Docker daemon access?
- If the API is compromised, what other resources can it reach?

## Deliverable
A short attack-surface table with finding, evidence, impact and recommended mitigation.
