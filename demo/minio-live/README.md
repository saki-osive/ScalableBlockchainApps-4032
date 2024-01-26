kubectl apply -f minio-pvc.yaml
kubectl create -f minio.yaml
kubectl port-forward pod-name 9000:9000

