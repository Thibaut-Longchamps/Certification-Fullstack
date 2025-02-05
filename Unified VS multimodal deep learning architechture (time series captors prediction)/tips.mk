python3 -m venv venv => créer environnement virtuel

venv\Scripts\activate => activer environnement virtuel (windows)
source venv/bin/activate (wsl2 ubuntu)
source ../venv/bin/activate


(si bug car venv pas installé sur wsl2)
sudo apt update
sudo apt install python3.12-venv  # Ou python3-venv si tu utilises une autre version

dans powershell:
wsl -d Ubuntu

accéder au conteneur de airflow:
docker exec -it my_ml_project-airflow-1 bash
airflow db init



cd /mnt/c/Users/33760/Desktop/airflow_mlflow_project/my_ml_project
(python3 -m venv venv) = que la première fois

sudo apt install python3.12-venv
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements_venv.txt

sudo chmod -R 777 ./logs
ls -ld ./logs

docker-compose exec airflow-scheduler bash
airflow db init



pip install jupyter et ipykernel (obligatoire)

sudo apt update => met à jour gestionnaire de paquet

sudo apt install python3-pip => install pip

pip3 install --upgrade pip => met à jour pip

python -m ipykernel install --user --name nom_du_kernel --display-name "Nom du Kernel"
(pour rendee accessible le kernel)

------------------------------------------------------------------

Minio open source:

linux : 
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
./minio server /data

linux: créer dossier data
sudo mkdir /data

sudo chown -R minioadmin /data
sudo chmod u+rxw /data


linux: arrêter minio
ps aux | grep minio
kill <PID>

accés à la console:
http://127.0.0.1:9000
http://localhost:9000

-------------------------------------------------------------------------------------------

pip install => installer les librairies


Commande création des fichiers (via terminal ubuntu)
mkdir -p my_ml_project/{dags,data,models,scripts} && touch my_ml_project/{docker-compose.yml,Dockerfile,requirements.txt}

my_ml_project/
│
├── dags/               # Pour les DAGs Airflow
├── data/               # Répertoire temporaire pour stocker les données transformées
├── models/             # Répertoire optionnel pour modèles
├── scripts/            # Scripts Python pour le traitement des données et les modèles
|__ notebook/
├── docker-compose.yml  # Fichier Docker Compose pour orchestrer les services
├── Dockerfile          # Dockerfile pour configurer Airflow
└── requirements.txt    # Dépendances Python pour Airflow et les scripts



PostgreSQL : Stocke les données propres après la transformation.
MLflow : Gère le suivi des métriques des modèles.
MinIO : Simule un dépôt S3 pour stocker les artefacts (modèles, graphes, logs).
Airflow : Orchestration du pipeline, extrait les données, les transforme, entraîne des modèles et enregistre les métriques dans MLflow.

prompt : donc on refait le projet avec airflow docker docker compose minio postgre pour 
stocker les données propres du pipeline on integre le model dans le pipeline qui stockera
 ses metriques dans mlflow et les graph dans minio. Tout doit être commenté. Je suis novice j'ai besoin
 de tous les détails possibles des étapes.