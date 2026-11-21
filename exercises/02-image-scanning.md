# Exercise 2 — Scan container images with Trivy

## Objective
Find known vulnerabilities in images and dependencies, interpret severity and decide what to remediate first.

## Tasks
Install Trivy using the official instructions for your operating system: https://trivy.dev/latest/getting-started/installation/

Build the API image:
```bash
docker compose -f compose.baseline.yaml build api
docker images
```

Scan it:
```bash
trivy image <api-image-name>
trivy image --severity HIGH,CRITICAL <api-image-name>
```

Optionally scan the MySQL and Nginx images too.

## Interpret the report
For several findings, record:
- CVE identifier;
- affected package;
- installed version and fixed version, if available;
- severity;
- whether the vulnerable component is present in the running image;
- remediation or risk-acceptance recommendation.

## Questions
- What is a CVE?
- Does a HIGH or CRITICAL finding prove exploitability in this application?
- Why can a secure application contain a vulnerable operating-system package?
- What are the trade-offs of using a slim or minimal base image?

## Deliverable
A prioritized vulnerability report. Do not blindly upgrade every package during the exercise; explain the proposed fix and retest.
