# KServe Deployment on Single-Node Kubernetes

## Overview
This project demonstrates deployment of a CPU-based machine learning model using KServe on a single-node Kubernetes cluster. The system supports autoscaling based on request load.

---

## Architecture
User → Istio → Knative → KServe → Model Pod

---

## Setup

### 1. Kubernetes Cluster
- Single-node cluster (K3s / Minikube)

### 2. Components Installed
- Istio
- Knative Serving
- KServe

---

## Deployment

```bash
kubectl apply -f manifests/pvc.yaml
kubectl apply -f manifests/sklearn.yaml
