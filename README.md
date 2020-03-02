# kubernetes-swagger-api

This is an exercise in containerizing a Python Flask web server. A CRUD RESTful API is implemented to manipulate data in a MongoDB database about passengers on the Titanic which can then be deployed to a Kubernetes cluster.

## Prereqs

* [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) installed or `kubectl` configured for your Kubernetes cluster.

## Run the app

1. Clone this repo to a location of your choice.
2. `cd` to this repo.
3. Set up the cluster with the following command.

   `kubectl apply -f app-service.yaml,mongodb-service.yaml,app-deployment.yaml,mongo-seed-deployment.yaml,mongodb-deployment.yaml`

4. Open the API site with

   `open $(minikube service app --url)/ui`

## Considerations & Improvements

### Load balancing

If this were being run in AWS or Google Cloud, the `ServiceType` of `app` could be changed to `LoadBalancer` automatically allocating an Ingress load balancer to the service.  Otherwise to prevent the arbitrary port of `30000` from being exposed as a `NodePort` an [Ingress resource](https://kubernetes.io/docs/concepts/services-networking/ingress/#the-ingress-resource) and [Ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) could be created.

### Storage

For the `mongodb` database, a more complicated, but reliable storage structure could be implemented including creating a `StorageClass`, `Headless Service`, and a `StatefulSet` to move the storage lifecycle from that of the Pod and to its [own persistent resource](https://kubernetes.io/blog/2017/01/running-mongodb-on-kubernetes-with-statefulsets/).
