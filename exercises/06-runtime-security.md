# Exercise 6 — Runtime security and Falco

## Objective
Understand why secure images and hardened configuration do not remove the need to monitor workload behaviour after startup.

## Concepts
Image scanning finds known issues in image contents. Runtime detection looks for suspicious behaviour while a workload is running, such as unexpected shell execution or access to sensitive files.

## Demonstration
On the lab host:
```bash
docker compose -f compose.baseline.yaml exec api sh
id
ps
```
Discuss why an unexpected shell inside a production application container may be suspicious. This command is a benign simulation for the class; it is not proof that Falco is installed or detecting the event.

## Falco environment requirement
Falco is designed around Linux kernel event visibility. Docker Desktop on macOS and Windows runs containers inside a Linux VM, so host-level event collection is not equivalent to running Falco on a native Linux host.

For a reliable hands-on Falco exercise, use a dedicated Ubuntu Linux VM/host with a supported Falco driver and kernel. Follow the current official install guide:
https://falco.org/docs/setup/

Do not promise that Falco will work identically on every student's Docker Desktop machine. If no Linux VM is available, deliver this as an instructor-led demonstration using prepared alert output.

## Questions
- How does runtime detection differ from image scanning?
- What behaviour would be unusual for this API?
- What is an alert, and what investigation should follow it?
- What are false positives and false negatives?

## Deliverable
A short incident note describing a suspicious runtime event, its possible impact and the first response steps.
