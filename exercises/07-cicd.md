# Exercise 7 — Add image scanning to GitHub Actions

## Objective
Run a container image vulnerability scan automatically when code is pushed or a pull request is opened.

## Tasks
1. Create a GitHub repository from this lab.
2. Review `.github/workflows/container-security.yml`.
3. Push the repository to GitHub.
4. Open the Actions tab and inspect the workflow run.
5. Review the Trivy output and understand why the job passes or fails.

## Security note
The example workflow uses the Trivy Action pinned to a version tag for readability. For production, pin third-party Actions to a verified full commit SHA and review updates deliberately. The workflow scans the API image; extend it to scan Nginx and MySQL if desired.

## Questions
- What is a security gate?
- What happens when a scan returns a qualifying finding?
- Why scan before publishing or deploying an image?
- Who should approve an exception, and how should it be documented?

## Deliverable
A successful GitHub Actions run and a screenshot or link to the scan result.
