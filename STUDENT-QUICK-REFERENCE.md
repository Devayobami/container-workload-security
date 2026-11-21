# Student quick reference

## Start baseline
```bash
cp .env.example .env
docker compose -f compose.baseline.yaml up --build -d
```

## Check
- App: http://localhost:8080
- API: http://localhost:8080/api/
- Database check: http://localhost:8080/api/db

## Rebuild API after Dockerfile changes
```bash
docker compose -f compose.baseline.yaml build api
docker compose -f compose.baseline.yaml up -d --force-recreate api
```

## Start hardened reference
Stop the baseline first:
```bash
docker compose -f compose.baseline.yaml down
docker compose -f compose.hardened.yaml up --build -d
```

## Stop and clean
```bash
docker compose -f compose.hardened.yaml down
```

Add `-v` only if you intentionally want to delete the lab database volume.

## Create your working copy for Exercise 3
```bash
cp compose.baseline.yaml compose.student.yaml
```
Make your incremental Compose hardening changes in `compose.student.yaml`. Keep `compose.hardened.yaml` as a reference until you have completed the exercises.
