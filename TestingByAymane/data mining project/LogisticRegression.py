import  numpy as np



class myLogisticRegression:
    def __init__(self, l_rate=0.001, iterations=1000):  # assign values for hyper-parameters
        self.l_rate = l_rate  # learning rate
        self.iterations = iterations  # number of iterations

    def fit(self, x, y):  # Fit the training data using Gradient Descent
        self.losses = []  # An empty list to store the error in each iteration
        self.theta = np.zeros((1 + x.shape[1]))  # intitalization,,,Array of zeros
        n = x.shape[0]  # number of training examples 768

        for i in range(self.iterations):
            # Step1
            y_pred = self.theta[0] + np.dot(x, self.theta[1:])  # hypothesis h(x)
            z = y_pred
            # Step2
            g_z = 1 / (1 + np.e ** (-z))  # map predicted values to probabilities between 0 & 1

            # Step3
            cost = 0
            for iy in y:
                cost += (-iy * np.log(g_z) - (1 - iy) * np.log(1 - g_z)) / n  # cost function
            self.losses.append(cost)  # Tracking losses

            # Step4
            d_theta1 = (1 / n) * np.dot(x.T, (g_z - y))  # Derivatives of theta[1:]
            d_theta0 = (1 / n) * np.sum(g_z - y)  # Derivatives of theta[0]

            # Step5
            self.theta[1:] = self.theta[1:] - self.l_rate * d_theta1  # upadting values of thetas using Gradient descent
            self.theta[0] = self.theta[
                                0] - self.l_rate * d_theta0  # upadting the value of theta 0 using Gradient descent
        return self

    def predict(self, x):  # Predicts the value after the model has been trained.
        y_pred = self.theta[0] + np.dot(x, self.theta[1:])
        z = y_pred
        g_z = 1 / (1 + np.e ** (-z))
        return [1 if i > 0.5 else 0 for i in g_z]  # Threshold




def accuracy(y_pred, Y_test):
    s = 0
    for i in range(len(y_pred)):
        if y_pred[i] == Y_test[i]:
            s += 1
    return s / len(Y_test)