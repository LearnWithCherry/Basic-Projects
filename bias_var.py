# Importing Important Libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Giving dataset to the model
np.random.seed(42)

X = np.linspace(-3, 3, 100)
Y = 0.5 * X**3 - X**2 + 2 + np.random.randn(100) * 3

# Reshaping
X = X.reshape(-1, 1)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

print("Training Samples:", len(X_train))
print("Test Samples:", len(X_test))

# Underfit Model
underfit_model = make_pipeline(
    PolynomialFeatures(degree=1),
    LinearRegression()
)

# Good Fit Model
goodfit_model = make_pipeline(
    PolynomialFeatures(degree=3),
    LinearRegression()
)

# Overfit Model
overfit_model = make_pipeline(
    PolynomialFeatures(degree=15),
    LinearRegression()
)

# L1 Regularized Model
Lasso_model = make_pipeline(
    PolynomialFeatures(degree=15),
    Lasso(alpha=0.01, max_iter=10000)
)

# Training Models
underfit_model.fit(X_train, Y_train)
goodfit_model.fit(X_train, Y_train)
overfit_model.fit(X_train, Y_train)
Lasso_model.fit(X_train, Y_train)

print("All models are trained SUCCESSFULLY")

# Plotting Predictions
X_plot = np.linspace(-3, 3, 500).reshape(-1, 1)

Y_under = underfit_model.predict(X_plot)
Y_good = goodfit_model.predict(X_plot)
Y_over = overfit_model.predict(X_plot)
Y_lasso = Lasso_model.predict(X_plot)

# Dictionary of Models
models = {
    "Under Fit": underfit_model,
    "Good Fit": goodfit_model,
    "Over Fit": overfit_model,
    "L1 Regularized": Lasso_model
}

print("=" * 30, "Model Performance", "=" * 30)

# Evaluating Models
for name, model in models.items():

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_error = mean_squared_error(Y_train, train_pred)
    test_error = mean_squared_error(Y_test, test_pred)

    print(f"{name}:")
    print(f"Training Error: {train_error:.2f}")
    print(f"Testing Error: {test_error:.2f}")
    print("-" * 50)

# Plotting
plt.figure(figsize=(12, 8))

plt.scatter(X, Y, color="black", label="Data", alpha=0.5)

plt.plot(X_plot, Y_under, label="Under Fit (Degree 1)")
plt.plot(X_plot, Y_good, label="Good Fit (Degree 3)")
plt.plot(X_plot, Y_over, label="Over Fit (Degree 15)")
plt.plot(X_plot, Y_lasso, label="L1 Regularized")

plt.legend()
plt.title("Underfitting vs Good Fit vs Overfitting")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()