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
Tout au lond de ce tp, nous allons nous baser sur le projet situé dans le répertoire app de ce repo. Cette application est composée d'un front qui fait essentiellement office de passe-plat vers le back qui lui réalise les actions.
L'application renvoie différentes informations sur:
* les hostname des back et front
* l'url appelée
* l'heure d'appel
* l'environement dans lequel l'app à été déployée

L'application peut être requêtée sur :
* n'importe quel path
* ou sur le path /write

Un appel sur le path /write, engendrera une écriture de l'argument passé en paramètre dans un fichier de log situé dans le container back.

## 1 : Docker
Cette première partie est à réaliser individuellement.

### 1.0 : Pull request time !!
Forker et cloner [le repository du tp2](https://github.com/cours-ece/tp2).
Ajouter votre prénom, votre nom au fichier answers.md et votre numéro d'équipe (de 1 à 7), puis réaliser une pull request sur le repository du tp.

### 1.1 : Comprendre l'app

Inspecter les fichiers contenus dans le repertoire **app** pour comprendre la structure du projet.

### 1.2 : Let's Build it

Dans le répertoire app/back, créer un fichier **Dockerfile** capable de builder une image python contenant notre code back.

Help:
* Consulter la [Dockerfile reference documentation](https://docs.docker.com/engine/reference/builder/)
* Se baser sur une image python [Docker Hub](https://hub.docker.com/)
* Python utilise des libraires à installer sur un host avant de pouvoir démarrer le programme. Pour installer ces libraires, exécuter la commande suivante (dans le Dockerfile)
```bash
pip install -r requirements.txt
```
* la commande **WORKDIR** peut aider
* Créer un repertoire logs à la racine de votre projet
* Alpine, c'est la vie

### 1.3 : Un premier lancement pas très concluant
Lancer un container à partir de l'image Docker que vous venez de créer. Ecrire la commande utilisée dans le fichier answers.md

### 1.4 : Accéder au service
Essayer d'accéder à l'application sur l'URL indiquée par les logs. Pourquoi, cette adresse ne répond rien ? 

Redémarrer le container en ouvrant les ports nécessaires pour accéder au service. Ecrire la commande utilisée dans le fichier answers.md

### 1.5 : Env var
Essayer d'accéder à l'application sur l'URL indiquée par les logs. Retourner dans votre terminal, vous êtes gratifiés d'une belle stacktrace d'erreur. Cette erreur survient car le programme s'attend à trouver la variable d'environement **ENVIRONMENT** settée dans le container.

Redémarrer le container en ajoutant la variable d'environement manquante pour que le service réponde correctement (inspiration: vous êtes dans un environement de développement). Ecrire la commande utilisée dans le fichier answers.md

L'application démarre correctement et vous pouvez y accéder en suivant l'URL affichée par les logs.

### 1.6 : Let's Ship it
Afin de partager votre nouvelle création fantastique avec le monde, nous allons pousser l'image sur la registry officielle Docker appelée Docker Hub (ou Docker Store)

Pour cela: 
* Se créer un compte sur [Docker Hub](https://hub.docker.com/)
* Créer un nouveau repository rattaché à votre compte
* Puis, pousser votre image fraichement créée sur votre repository

Votre image ne peut pas être poussée telle qu'elle est. Pourquoi ? Modifier le nom de votre image et pousser la à nouveau sur votre repository Docker Hub. Ecrire la commande utilisée dans le fichier answers.md

### 1.7 : Let's Run it
Maintenant votre image partagée avec le monde, vous pouvez la puller depuis n'importe quelle machine sur laquelle Docker est installé.

Supprimer toutes vos images créée depuis le début du tp sur votre machine. Ecrire la commande utilisée dans le fichier answers.md

Relancer maintenant un container en vous basant sur l'image que vous venez de pousser dans votre repository Docker Hub. Que se passe t'il avant que l'image démarre. Ecrire la commande utilisée dans le fichier answers.md

Votre container fonctionne comme espéré mais si vous fermez votre terminal, celui-ci se stoppe. Relancer le container en mode détaché et vérifier que le container est accessible via son interface web. Ecrire la commande utilisée dans le fichier answers.md

### 1.8 : Le naming, c'est important
Votre container semble bien être démarré. En mode détaché, comment pouvez vous observer que le container est bien démarré ? Quel est le nom de votre container ?. Ecrire la commande utilisée dans le fichier answers.md

Redémarrer votre container en le renommant avec un nom ayant du sens. Ecrire la commande utilisée dans le fichier answers.md

### 1.9 : Go inside
Votre container back à présent démarré, ouvrir une session interactive pour observer les fichiers à l'interieur du container. Exécuter la commande suivante permettant de récupérer des infos sur l'OS:
```bash
cat /etc/*release
```
Quel est l'OS utilisé dans le container ? Copier la sortie de cette commande dans le fichier answers.md.


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
