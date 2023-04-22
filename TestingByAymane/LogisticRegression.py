# Importation de la bibliothèque NumPy
import numpy as np

# Définition de la fonction de la fonction d'activation sigmoïde
def sigmoid(x):
    return 1/(1+np.exp(-x))


# Définition de la fonction pour calculer la précision (accuracy) du modèle
def accuracy(y_pred, y_test):
    return np.sum(y_pred==y_test)/len(y_test)


# Définition de la classe LogisticRegression
class LogisticRegression():
    # Initialisation des hyperparamètres
    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    # Entraînement du modèle
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_pred = np.dot(X, self.weights) + self.bias
            predictions = sigmoid(linear_pred)

            # Calcul des gradients
            dw = (1/n_samples) * np.dot(X.T, (predictions - y))
            db = (1/n_samples) * np.sum(predictions-y)

            # Mise à jour des paramètres
            self.weights = self.weights - self.lr*dw
            self.bias = self.bias - self.lr*db

    # Prédiction des classes
    def predict(self, X):
        linear_pred = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_pred)
        class_pred = [0 if y<=0.5 else 1 for y in y_pred]
        return class_pred







