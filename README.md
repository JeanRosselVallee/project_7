<img src="https://www.whenthebanksaysno.co.uk/wp-content/uploads/2023/05/D9585792-ED4C-4363-900E-1EDCE31B99B1.jpeg">
    
# Buts : 
- Mettre en oeuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit
- Classifier la demande du client en crédit accordé ou refusé. 

# Contexte :
- on a 2 classes de clients en fonction de la probabilité qu'il rembourse
- les demandes sont approuvées en fonction de cette probabilité.
crédit réfusé à un bon client.

# Arborescence des répertoires :
- api  pour le déploiement de l'API
- modeling pour la modélisation
- test_api pour les tests automatisés
- website pour le formulaire de test de l'API

# GitHub Actions inclut un seul workflow avec plusieurs tâches ou jobs
- installation de modules
- déploiement en pré-prod
- lancement des tests sur serveur de pré-prod
- déploiement conditionnel sur la production si les tests sont réussis
