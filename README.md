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
## 🔹 Inference Endpoint Access (KServe)

Due to the VM being in a restricted network environment (no external LoadBalancer or open NodePort), the inference service is exposed using **kubectl port-forward**.

### Step 1: Verify Running Resources

```bash
kubectl get inferenceservice
kubectl get pods
```

Ensure:

* InferenceService status = `READY`
* Predictor pod is in `Running` state

---

### Step 2: Start Port Forwarding

```bash
kubectl port-forward pod/<pod-name> 8081:8080
```

Example:

```bash
kubectl port-forward pod/sklearn-iris-predictor-default-00002-deployment-xxxxx 8081:8080
```

---

### Step 3: Verify Model Availability

```bash
curl http://127.0.0.1:8081/v1/models
```

Expected Output:

```json
{"models":["1"]}
```

---

### Step 4: Send Inference Request

```bash
curl -X POST http://127.0.0.1:8081/v1/models/1:predict \
-H "Content-Type: application/json" \
-d '{"instances": [[5.1, 3.5, 1.4, 0.2]]}'
```

Expected Response:

```json
{"predictions":[0]}
```

---

### 🔹 Notes

* The model name is dynamically resolved and verified using `/v1/models`.
* Endpoint used:

```
http://127.0.0.1:8081/v1/models/1:predict
```

* Port-forwarding is required because external access via VM IP is restricted.

---


## Deployment

```bash
kubectl apply -f manifests/pvc.yaml
kubectl apply -f manifests/sklearn.yaml
