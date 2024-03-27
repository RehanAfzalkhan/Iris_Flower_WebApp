# # Linear Regression (Without NumPy, Torch, TensorFlow, etc.)
# # Least Squares Method

# # y = bo + b1x                  # b1 = slope, b0 = y-intercept
# # bo = y_mean - b1 * x_mean
# # y_pred = bo + b1 * x

# # xs = [-1, 0, 1, 2, 3, 4]
# # ys = [-3, -1, 1, 2.8, 5.1, 6.9]

# # import math

# class LinearRegression:
#     def __init__(self):
#         self.coef_ = 0
#         self.intercept_ = 0
#         self.SSR = 0
#         self.SST = 0
#         self.r2score = 0

#     def fit(self, x, y):
#         if len(x) != len(y):
#             raise ValueError("x and y must have the same length")

#         # self.n = len(x)
#         # self.coef_ = (self.n * sum([x[i] * y[i] for i in range(self.n)]) - sum(x) * sum(y)) / (self.n * sum([x[i] ** 2 for i in range(self.n)]) - sum(x) ** 2)
#         # self.intercept_ = (sum(y) - self.m * sum(x)) / self.n

#         x_mean = sum(x) / len(x)
#         y_mean = sum(y) / len(y)

#         # Least Squares Method
#         numerator = denominator = 0
#         for i in range(len(x)):
#             numerator += ((x[i] - x_mean) * (y[i] - y_mean))
#             denominator += ((x[i] - x_mean) ** 2)
k
#         self.coef_ = numerator / denominator
#         self.intercept_ = y_mean - self.coef_ * x_mean

#         y_pred = []
#         for i in range(len(x)):
#             y_pred.append(self.intercept_ + (self.coef_ * x[i]))

#         # R2 Score
#         for i in range(len(y)):
#             self.SSR += (y[i] - y_pred[i]) ** 2
#             self.SST += (y[i] - y_mean) ** 2

#         self.r2score = 1 - (self.SSR / self.SST)


#     def predict(self, x):
#         y_pred = []
#         for i in range(len(x)):
#             y_pred.append(self.intercept_ + (self.coef_ * x[i]))

#         return y_pred


# # Instantiate the LinearRegression
# linear_model = LinearRegression()

# xs = [-1, 0, 1, 2, 3, 4]
# ys = [-3, -1, 1, 2.8, 5.1, 6.9]

# linear_model.fit(xs, ys)        # Model Training

# # print(linear_model.coef_)
# # print(linear_model.intercept_)

# print("\n", ys)
# print(linear_model.predict(xs)) # Model Prediction

# print("Score: ", linear_model.r2score)  # Model Evaluation

# -----------


# Linear Regression (With Python and Python Built-in Modules)
# like math module

import statistics


class LinearRegression:
    def __init__(self):
        self.coef_ = 0
        self.intercept_ = 0
        self.SSR = 0
        self.SST = 0
        self.r2score = 0

    def fit(self, x, y):
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")

        x_mean = statistics.mean(x)
        y_mean = statistics.mean(y)

        numerator = denominator = 0
        for i in range(len(x)):
            numerator += (x[i] - x_mean) * (y[i] - y_mean)
            denominator += (x[i] - x_mean) ** 2

        self.coef_ = numerator / denominator
        self.intercept_ = y_mean - self.coef_ * x_mean

        y_pred = []
        for i in range(len(x)):
            y_pred.append(self.intercept_ + (self.coef_ * x[i]))

        for i in range(len(y)):
            self.SSR += (y[i] - y_pred[i]) ** 2
            self.SST += (y[i] - y_mean) ** 2

        self.r2score = 1 - (self.SSR / self.SST)

    def predict(self, x):
        y_pred = []
        for i in range(len(x)):
            y_pred.append(self.intercept_ + (self.coef_ * x[i]))

        return y_pred


# NumPy

# import numpy as np

# class LinearRegression:
#     pass
