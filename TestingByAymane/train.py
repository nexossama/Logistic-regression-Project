# Import des librairies nécessaires
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from LogisticRegression import LogisticRegression,accuracy

# Chargement des données du cancer du sein
bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Instanciation du modèle de régression logistique avec un taux d'apprentissage de 0.01
clf = LogisticRegression(lr=0.01)

# Entraînement du modèle sur les données d'entraînement
clf.fit(X_train,y_train)

# Prédiction sur les données de test
y_pred = clf.predict(X_test)

# Calcul de l'accuracy du modèle
acc = accuracy(y_pred, y_test)
print(acc)

# Affichage d'une visualisation des prédictions sur les deux premières caractéristiques des données de test
plt.scatter(X_test[:,0], X_test[:,1], c=y_pred, cmap='jet')
plt.show()
