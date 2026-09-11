import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -------------------------
# 1. Load the dataset
# -------------------------
df = pd.read_csv("../data/Housing.csv")


# -------------------------
# 2. Convert yes/no columns
# -------------------------
yes_no_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for col in yes_no_columns:
    df[col] = df[col].map({"yes": 1, "no": 0})


# -------------------------
# 3. Encode furnishing status
# -------------------------
df = pd.get_dummies(
    df,
    columns=["furnishingstatus"],
    dtype=int
)


# -------------------------
# 4. Separate features and target
# -------------------------
X = df.drop("price", axis=1)
y = df["price"]


# -------------------------
# 5. Split the data
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -------------------------
# 6. Train Linear Regression
# -------------------------
model = LinearRegression()

model.fit(X_train, y_train)


# -------------------------
# 7. Make predictions
# -------------------------
y_pred = model.predict(X_test)


# -------------------------
# 8. Evaluate the model
# -------------------------
mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)


print("Linear Regression Results")
print("-------------------------")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)


# -------------------------
# 9. Save the model
# -------------------------
joblib.dump(model, "../house_price_model.pkl")

print("\nModel saved successfully!")