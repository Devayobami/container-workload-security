# Exercise 3 — Harden the Flask API container

## Objective
Apply least privilege and reduce the impact of a compromised API container.

## Files used
- `api/Dockerfile`
- `compose.student.yaml` (your working copy of the baseline)

Before starting, create your working copy:
```bash
cp compose.baseline.yaml compose.student.yaml
```
Use `compose.student.yaml` for the rest of this exercise. The completed `compose.hardened.yaml` is an instructor reference.

The target is the Flask API service, not Nginx or MySQL. The baseline and hardened Compose files both build from `api/Dockerfile`.

## 3A — Run as a non-root user
Edit `api/Dockerfile`. Create an unprivileged user and switch to it. For example:

```dockerfile
RUN useradd --create-home --uid 10001 appuser
USER 10001:10001
```

Rebuild and recreate:
```bash
docker compose -f compose.student.yaml build api
docker compose -f compose.student.yaml up -d --force-recreate api
docker compose -f compose.baseline.yaml exec api id
```

Expected: the process is not UID 0. Confirm the application still responds.

## 3B — Drop Linux capabilities
In the `api` service of the Compose file you are using, add:

```yaml
cap_drop:
  - ALL
```

Recreate the service and test `/api/` and `/api/db`.

Explain that capabilities are granular Linux privileges. Only add a capability back if the application demonstrably needs it.

## 3C — Read-only root filesystem
Add to the API service:

```yaml
read_only: true
tmpfs:
  - /tmp:rw,noexec,nosuid,size=64m
```

Recreate and test. The app should continue to work because this example does not write application files and `/tmp` is available for temporary writes.

## 3D — Prevent privilege escalation
Add:

```yaml
security_opt:
  - no-new-privileges:true
```

Explain setuid/setgid and why a process should not be able to gain extra privileges unexpectedly.

## 3E — Resource limits
Add:

```yaml
mem_limit: 512m
cpus: 0.5
```

Explain that limits reduce the chance of a single workload exhausting host resources. They are not a substitute for capacity planning.

## Validation
After each individual change:
```bash
docker compose -f compose.student.yaml up --build -d api
docker compose -f compose.student.yaml ps
docker compose -f compose.student.yaml logs --tail=50 api
```
Test:
- `http://localhost:8080/api/`
- `http://localhost:8080/api/db`

Inspect effective settings:
```bash
docker inspect <api-container>
```

## Questions
- Why is non-root not the same as “secure”?
- What are Linux capabilities?
- Why might a read-only filesystem break an application?
- What is the purpose of `no-new-privileges`?
- What can happen if a container has no resource limits?

## Deliverable
A hardened API configuration and a short explanation of each control. Apply one control at a time and record any failures.
