# `sample-service`

A tiny Flask service for validating the SmartGenie local CI/CD and GitOps flow.

## Local build target
This image is meant to be built into Minikube for the local POC:

```powershell
minikube image build -t smartgenie-sample:local .\sample-service
kubectl apply -k .\sg-gitops\environments\dev
kubectl get pods -n smartgenie-dev
kubectl port-forward -n smartgenie-dev svc/smartgenie-sample 8080:80
```

Then open: `http://127.0.0.1:8080/health`
