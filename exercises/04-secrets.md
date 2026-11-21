# Exercise 4 — Handle application secrets

## Objective
Remove credentials from tracked source/configuration and understand the remaining risks.

## Baseline observation
The Compose file interpolates values from `.env` or fallback demo values. `.env` is ignored by Git, but it is not encrypted and should not be treated as a production secrets manager.

## Tasks
1. Copy `.env.example` to `.env` and change the demo passwords.
2. Confirm `.env` is ignored:
   ```bash
   git check-ignore -v .env
   git status --short
   ```
3. Inspect the Compose configuration:
   ```bash
   docker compose -f compose.baseline.yaml config
   ```
4. Discuss how environment variables may be visible to users with sufficient Docker/host privileges.
5. Review the optional Compose secrets pattern in `instructor/INSTRUCTOR-GUIDE.md`.

## Questions
- Is `.env` encrypted?
- Who can read the host file?
- Can a Docker administrator inspect container environment variables?
- How would you use AWS Secrets Manager, Azure Key Vault or Vault in production?

## Deliverable
A secrets-handling recommendation that distinguishes local development from production.
