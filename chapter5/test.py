import polyreg
import linearreg
import numpy as np
import matplotlib.pyplot as plt

# データ生成
np.random.seed(0)


def f(x):
    return 1 + 2 * x


x = np.random.random(10) * 10
y = f(x) + np.random.randn(10)

# 多項式回帰
model = polyreg.PolynomialRegression(10)
model.fit(x, y)

