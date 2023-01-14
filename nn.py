import numpy as np


# apylint: disable=too-many-instance-attributes
class Network:
    def __init__(self):
        self.input_layer = 2
        self.hidden_layer = 3
        self.output_layer = 1

        self.wt1 = np.random.randn(self.input_layer, self.hidden_layer)  # 2*3
        self.wt2 = np.random.randn(self.hidden_layer, self.output_layer)  # 3*1

        self.act2 = self.zact2 = None
        self.act3 = self.zact3 = None
        self.yhat = None

    sigmoid = lambda x: 1 / (1 + np.exp(-x))

    sigmoid_prime = lambda x: np.exp(-x) / (1 + np.exp(-x)) ** 2

    def forward(self, X, Y):
        self.act2 = np.dot(X, self.wt1)  # n*3
        self.zact2 = Network.sigmoid(self.act2)  # n*3

        self.act3 = np.dot(self.zact2, self.wt2)  # n*1
        self.yhat = Network.sigmoid(self.act3)  # n*1
        print("yHat :\n", self.yhat)

        cost = 1 / 2 * sum((Y - self.yhat) ** 2)

        return cost

    # needs a check
    def gradient(self, X, Y):  # X is n*2, Y is n*1
        diff = self.yhat - Y  # n*1

        delta2 = diff * Network.sigmoid_prime(self.act3)  # n*1
        dcdw2 = np.dot(self.zact2.T, delta2)  # should be same size as wt2 - 3*1

        delta1 = np.dot(delta2, self.wt2.T) * Network.sigmoid_prime(self.act2)
        dcdw1 = np.dot(np.array(X).T, delta1)  # should be same size as wt1 - 2*3

        return dcdw2, dcdw1

    def backprop(self, X, Y):
        k = 3  # scalar
        dcdw2, dcdw1 = self.gradient(X, Y)
        self.wt2 = self.wt2 - k * dcdw2
        self.wt1 = self.wt1 - k * dcdw1
        print("propagated backwards")


# X should be n*input_layer size - in our case n*2
# Y should be between 0 and 1 - of size  n*output_layer size - in this case n*1
