# fleet-on-kind

**Status: skeleton.** This directory currently only proves that a local Kubernetes cluster can be created, checked and removed. No fleet runs on it yet.

## What this will become

A reference fleet you can run with one command, with no Kubernetes knowledge needed. The cluster is a [kind](https://kind.sigs.k8s.io/) cluster, so everything runs in Docker on your own machine.

## Prerequisites

- Docker (running)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- make

## Targets

| Target | What it does |
|---|---|
| `make up` | Creates the `fleet-on-kind` cluster from `kind-config.yaml`. Does nothing if it already exists. |
| `make down` | Deletes the cluster. No error if it is absent. |
| `make smoke` | Runs `up`, waits for the node to be Ready, then runs `down` even if the wait failed. Exits non-zero if the wait failed. |
