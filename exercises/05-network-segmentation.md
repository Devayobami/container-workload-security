# Exercise 5 — Segment container networks

## Objective
Limit unnecessary service-to-service connectivity and avoid publishing the database to the host.

## Tasks
1. Inspect the baseline network:
   ```bash
   docker network ls
   docker network inspect <baseline-network>
   ```
2. Review `compose.hardened.yaml`.
3. Compare the network attachments:
   - Nginx: `frontend`
   - Flask API: `frontend` and `backend`
   - MySQL: `backend` only
4. Notice that MySQL has no published host port in the hardened file.
5. Start the hardened deployment:
   ```bash
   docker compose -f compose.hardened.yaml up --build -d
   ```
6. Verify the application still works at `http://localhost:8080/api/db`.
7. Inspect the networks and published ports:
   ```bash
   docker compose -f compose.hardened.yaml ps
   docker network ls
   ```

## Questions
- Why does the API need to join both networks?
- Why should Nginx not connect directly to MySQL?
- What is the benefit and limitation of Docker bridge-network isolation?
- Does Docker network segmentation replace cloud security groups or host firewall rules?

## Deliverable
A simple network diagram and an explanation of allowed communication paths.
