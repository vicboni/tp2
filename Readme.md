# TP 2 : Docker/Kubernetes

## Instructions
Le TP s'appuie sur [un autre repo Github](https://github.com/cours-ece/simple-java-hello-world).
Les réponses aux questions posées dans cet énoncé sont attendues dans un fichier **answers.md** situé dans le repo mentionné ci-dessus.

Le TP doit être réalisé individuellement

## Rappels
* installer l'auto completion
* doc docker
* doc docker-compose
* doc kubernetes

### Docker
* Concepts
  * Building
  * Shipping
  * Running
* [Docker doc reference](https://docs.docker.com/reference/)
  * Dockerfile
  * docker-compose.yml
  * command line 

### Kubernetes
* Orchestrateur
* Ressources
* Kind
  * Node
  * Pods
  * Service
  * Namespace
  * Secret
* Probes
* AKS

### Ce qu'on ne va pas voir
* Logging
* Monitoring
* Alerting
* Rolling update - Pas sur pour celui la
* Helm
* Service Mesh

### Gitflow
![Gitflow diagram](https://stxnext.com/media/filer_public_thumbnails/filer_public/d4/41/d4414c91-483b-4904-9c1b-fc92c899678c/gitflow.png__1011x520_q85_crop_subsampling-2_upscale.png "Gitflow diagram")


## 0 : Description du projet
rng = web service generating random bytes
hasher = web service computing hash of POSTed data
worker = background process using rng and hasher
webui = web interface to watch progress

How DockerCoins works:
* worker asks to rng to generate a few random bytes
* worker feeds these bytes into hasher
* and repeat forever!
* every second, worker updates redis to indicate how many loops were done
* webui queries redis, and computes and exposes "hashing speed" in your browser

## 1 : Docker

* Faire une pull request comme d'hab + donner un nombre à chaque personnes / table

* Ecrire un dockerfile
* Build
* Créer un compte sur docker hub
* Ship
* Run
* Run with parameter (port, interactive, 

## 2 : Docker Compose
- link between app
- volume, network
- named volume, named network
- up, down, logs (-f), -d, 
- --scale worker=2 (to 10 after)
each time, see logs 

## 3 : Kubernetes

### 2.0 : Configurer Kubernetes pour se connecter au cluster
Diviser la classe en 7 groupes de 4 personnes, puis attribuer un chiffre de 1 à 7 à chaque groupe.
Dans la suite de la consigne du tp, le nombre qui vous sera attribué sera nommé {NB}.

* [Installer kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-using-curl)
* [Configurer Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#configure-kubectl) en utilisant le fichier situé dans kube/config.zip
```bash
cd kube
unzip config.zip
# Le mot de passe est au tableau
```
* [Configurer l'autocompletion](https://kubernetes.io/docs/tasks/tools/install-kubectl/#enabling-shell-autocompletion)

* Configurer le cluster à pointer
```bash
kubectl config use-context ece{NB}
```

* Vérifier que la configuration fonctionne correctement
```bash
kubectl get pods --all-namespaces
```
```bash
NAMESPACE     NAME                                    READY   STATUS    RESTARTS   AGE
kube-system   heapster-5f8d5688-lr5p4                 2/2     Running   0          14h
kube-system   kube-dns-v20-668899dbdc-n4rg8           3/3     Running   0          14h
kube-system   kube-dns-v20-668899dbdc-v8fwh           3/3     Running   0          14h
kube-system   kube-proxy-m8gqs                        1/1     Running   0          14h
kube-system   kube-proxy-sr4nr                        1/1     Running   0          14h
kube-system   kube-proxy-xwvt8                        1/1     Running   0          14h
kube-system   kube-svc-redirect-56cx6                 2/2     Running   0          14h
kube-system   kube-svc-redirect-gxzw9                 2/2     Running   0          14h
kube-system   kube-svc-redirect-rf4nb                 2/2     Running   0          14h
kube-system   kubernetes-dashboard-7ff68ff786-h44zh   1/1     Running   2          14h
kube-system   metrics-server-76f76c6bfd-dhjbl         1/1     Running   0          14h
kube-system   tunnelfront-5b5b89b86c-qjgbt            1/1     Running   0          14h
```

### 2.1 : Naviguer dans l'aide de Kubernetes

### 2.2 : Se familiariser avec Kubernetes

```bash
# Récupérer les infos du cluster
kubectl cluster-info
# Lister les nodes
kubectl get node
# Récupérer l'OS et le kernel de chaque noeud
kubectl get node -o wide
# Lister les pods
kubectl get pod
```

### 2.3 : Déployer le projet sur Kubernetes

* Regarder du coté de [Kompose](http://kompose.io/)
* Voir les manifests générés et déployer sur Kubernetes
* A quoi servent les fichiers *deployment* et *service* ?
* Lister les déploiements, les pods et les services générés sur le cluster