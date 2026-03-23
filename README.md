# 🚀 KServe Deployment on Single-Node Kubernetes

### CPU-Based ML Inference Platform with Autoscaling

---

## 📌 Overview

This project demonstrates the deployment of a **CPU-based machine learning model** using **KServe** on a **single-node Kubernetes cluster**. The system is designed to simulate a **production-grade inference platform**, supporting:

* Scalable model serving
* Request-based autoscaling using Knative
* Containerized deployment via Kubernetes
* Observability-ready architecture

The implementation uses a **Scikit-learn model (Iris classifier)** served via KServe and tested using real-time inference requests.

---

## 🏗️ Architecture

```
Client Request
     ↓
Istio Ingress Gateway
     ↓
Knative Service (Autoscaler)
     ↓
KServe InferenceService
     ↓
Queue Proxy (Concurrency Control)
     ↓
Model Server (Sklearn Container)
```

---

## ⚙️ Tech Stack

* **Kubernetes (K3s / Minikube)** – Container orchestration
* **KServe** – ML model serving
* **Knative Serving** – Autoscaling & serverless layer
* **Istio** – Ingress and traffic routing
* **Docker Containers** – Model runtime
* **PVC (Persistent Volume Claim)** – Model storage

---

## 📦 Project Structure

```
.
├── manifests/
│   ├── pvc.yaml              # Storage for model artifacts
│   └── sklearn.yaml          # KServe InferenceService
├── README.md
└── (report & presentation)
```

---

## ⚙️ Setup & Installation

### 1️⃣ Kubernetes Cluster

* Single-node cluster (K3s / Minikube)

### 2️⃣ Install Required Components

* Istio
* Knative Serving
* KServe

---

## 🚀 Deployment Steps

```bash
kubectl apply -f manifests/pvc.yaml
kubectl apply -f manifests/sklearn.yaml
```

### Verify Deployment

```bash
kubectl get inferenceservice
kubectl get pods
```

Ensure:

* `READY = True`
* Pods are in `Running` state

---

## 🔹 Inference Endpoint Access

Due to restricted VM networking (no external LoadBalancer/NodePort access), the service is exposed using **port-forwarding**.

---

### Step 1: Start Port Forward

```bash
kubectl port-forward pod/<pod-name> 8081:8080
```

---

### Step 2: Verify Model

```bash
curl http://127.0.0.1:8081/v1/models
```

Expected:

```json
{"models":["1"]}
```

---

### Step 3: Send Inference Request

```bash
curl -X POST http://127.0.0.1:8081/v1/models/1:predict \
-H "Content-Type: application/json" \
-d '{"instances": [[5.1, 3.5, 1.4, 0.2]]}'
```

Expected:

```json
{"predictions":[0]}
```

---

## 📈 Autoscaling Demonstration

### Generate Load

```bash
while true; do
  for i in {1..30}; do
    curl -s -X POST http://127.0.0.1:8081/v1/models/1:predict \
    -H "Content-Type: application/json" \
    -d '{"instances": [[5.1, 3.5, 1.4, 0.2]]}' > /dev/null &
  done
  wait
done
```

---

### Monitor Scaling

```bash
kubectl get pods -w
```

### Observed Behavior

* Pods scale up with increasing traffic
* Pods scale down when traffic stops
* Scaling is based on **request concurrency (Knative)**

---

## 🔍 Key Concepts Demonstrated

* **InferenceService (KServe CRD)**
* **Serverless Autoscaling (Knative)**
* **Concurrency-based scaling vs HPA**
* **Model storage via PVC**
* **Queue-proxy for traffic handling**
* **Port-forward debugging approach**

---

## ⚠️ Limitations (Environment Constraints)

* No external LoadBalancer
* NodePort blocked by firewall
* Endpoint accessible only via port-forward

---

## 🏭 Production Architecture & Host360 Relevance

This project reflects a **production-grade ML serving architecture** that can be leveraged by platforms like **Host360** for scalable AI deployments.

### 🔹 How Host360 Can Use This

#### 1. Scalable Inference Platform

* Automatically scales based on traffic
* Handles burst workloads efficiently
* Ensures high availability

#### 2. Cost Optimization

* Scale-to-zero reduces idle costs
* Efficient CPU resource utilization
* Pay-per-usage model in production

#### 3. Multi-Model Deployment

* Multiple models can be deployed independently
* Supports multi-tenant architecture
* Enables different services for different clients

#### 4. CI/CD Integration

* Integrate with Jenkins/GitHub Actions
* Automate model deployment pipelines
* Continuous retraining & redeployment

#### 5. Advanced Traffic Management

Using Istio:

* Canary deployments
* A/B testing
* Traffic splitting

#### 6. Observability & Monitoring

* Prometheus metrics integration
* Latency and throughput tracking
* Alerting and performance monitoring

#### 7. Flexible Storage Integration

* Replace PVC with:

  * AWS S3
  * MinIO
* Enables real-world data pipelines

---

## 🚀 Production Improvements

To make this fully production-ready:

* Use **cloud LoadBalancer (AWS/GCP/Azure)**
* Configure **custom domain with Istio Gateway**
* Add **authentication & API gateway**
* Use **Grafana + Prometheus dashboards**
* Implement **secure secrets management**

---

## 📌 Summary

This project demonstrates a **complete ML inference lifecycle**:

* Model deployment using KServe
* Traffic handling via Istio
* Autoscaling with Knative
* Real-time inference testing
* Production-ready architecture design

It provides a strong foundation for building **scalable, cost-efficient AI platforms** like those used in Host360.

---

kubectl apply -f manifests/pvc.yaml
kubectl apply -f manifests/sklearn.yaml
