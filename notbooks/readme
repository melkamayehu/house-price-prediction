# 🏠 House Price Prediction

A machine learning project that predicts house prices based on different property features using **Linear Regression**.

## 📌 Project Overview

The goal of this project is to build a machine learning model that can predict the price of a house using information such as:

* Area
* Number of bedrooms
* Number of bathrooms
* Number of stories
* Parking spaces
* Main road access
* Guest room
* Basement
* Hot water heating
* Air conditioning
* Preferred area
* Furnishing status

The project includes data exploration, preprocessing, model training, evaluation, and prediction.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook / VS Code

## 📂 Project Structure

```text
house-price-prediction/
│
├── data/
│   └── Housing.csv
│
├── src/
│   └── model.py
│
├── house_price_model.pkl
├── requirements.txt
└── README.md
```

## 🔎 Exploratory Data Analysis

The dataset was explored using:

* Dataset shape and information
* Descriptive statistics
* Missing-value checks
* Duplicate-value checks
* Price distribution
* Area vs. price analysis
* Average price by number of bedrooms
* Average price by bathrooms
* Average price by stories
* Average price by parking spaces
* Correlation analysis

## 🧹 Data Preprocessing

The dataset contains categorical variables that needed to be converted into numerical values before training the machine learning model.

### Binary Encoding

The following columns were converted from `yes`/`no` into `1`/`0`:

```text
mainroad
guestroom
basement
hotwaterheating
airconditioning
prefarea
```

### One-Hot Encoding

The `furnishingstatus` column was converted using one-hot encoding.

This created separate numerical columns for:

* Furnished
* Semi-furnished
* Unfurnished

## 🤖 Machine Learning Models

Two regression models were tested:

### 1. Linear Regression

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### 2. Random Forest Regression

```python
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

The models were compared using:

* Mean Absolute Error (MAE)
* R² Score

Based on the test results, **Linear Regression performed better on this dataset**, so it was selected as the final model.

## 📊 Model Evaluation

The Linear Regression model was evaluated using:

### MAE

Mean Absolute Error measures the average difference between the actual and predicted house prices.

**Lower is better.**

### RMSE

Root Mean Squared Error gives more weight to larger prediction errors.

**Lower is better.**

### R² Score

R² measures how much of the variation in house prices is explained by the model.

**Higher is better.**

## 💾 Saved Model

The final trained Linear Regression model was saved using Joblib:

```python
joblib.dump(model, "house_price_model.pkl")
```

The saved model can later be loaded without retraining:

```python
loaded_model = joblib.load("house_price_model.pkl")
```

## 🔮 Making a Prediction

After loading the saved model, a new house can be passed to the model to generate a predicted price.

```python
predicted_price = loaded_model.predict(new_house)

print("Predicted price:", predicted_price[0])
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/melkamayehu/house-price-prediction.git
```

### 2. Enter the project folder

```bash
cd house-price-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the model

```bash
python src/model.py
```

## 🎯 Learning Outcomes

Through this project, I practiced:

* Data cleaning
* Exploratory data analysis
* Data visualization
* Categorical encoding
* Feature and target selection
* Train/test splitting
* Linear Regression
* Random Forest Regression
* Model evaluation
* Model comparison
* Saving and loading machine learning models
* Building a complete machine learning workflow

## 🔮 Future Improvements

Possible improvements include:

* Hyperparameter tuning
* Cross-validation
* Trying additional regression algorithms
* Feature engineering
* Building a simple web interface
* Deploying the model as an application

## 👩‍💻 Author

**Melkam Ayehu**

Computer Engineering Student
Interested in Machine Learning, AI, and Computational Neuroscience.
# 🏠 House Price Prediction

A machine learning project that predicts house prices based on different property features using **Linear Regression**.

## 📌 Project Overview

The goal of this project is to build a machine learning model that can predict the price of a house using information such as:

* Area
* Number of bedrooms
* Number of bathrooms
* Number of stories
* Parking spaces
* Main road access
* Guest room
* Basement
* Hot water heating
* Air conditioning
* Preferred area
* Furnishing status

The project includes data exploration, preprocessing, model training, evaluation, and prediction.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook / VS Code

## 📂 Project Structure

```text
house-price-prediction/
│
├── data/
│   └── Housing.csv
│
├── src/
│   └── model.py
│
├── house_price_model.pkl
├── requirements.txt
└── README.md
```

## 🔎 Exploratory Data Analysis

The dataset was explored using:

* Dataset shape and information
* Descriptive statistics
* Missing-value checks
* Duplicate-value checks
* Price distribution
* Area vs. price analysis
* Average price by number of bedrooms
* Average price by bathrooms
* Average price by stories
* Average price by parking spaces
* Correlation analysis

## 🧹 Data Preprocessing

The dataset contains categorical variables that needed to be converted into numerical values before training the machine learning model.

### Binary Encoding

The following columns were converted from `yes`/`no` into `1`/`0`:

```text
mainroad
guestroom
basement
hotwaterheating
airconditioning
prefarea
```

### One-Hot Encoding

The `furnishingstatus` column was converted using one-hot encoding.

This created separate numerical columns for:

* Furnished
* Semi-furnished
* Unfurnished

## 🤖 Machine Learning Models

Two regression models were tested:

### 1. Linear Regression

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### 2. Random Forest Regression

```python
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

The models were compared using:

* Mean Absolute Error (MAE)
* R² Score

Based on the test results, **Linear Regression performed better on this dataset**, so it was selected as the final model.

## 📊 Model Evaluation

The Linear Regression model was evaluated using:

### MAE

Mean Absolute Error measures the average difference between the actual and predicted house prices.

**Lower is better.**

### RMSE

Root Mean Squared Error gives more weight to larger prediction errors.

**Lower is better.**

### R² Score

R² measures how much of the variation in house prices is explained by the model.

**Higher is better.**

## 💾 Saved Model

The final trained Linear Regression model was saved using Joblib:

```python
joblib.dump(model, "house_price_model.pkl")
```

The saved model can later be loaded without retraining:

```python
loaded_model = joblib.load("house_price_model.pkl")
```

## 🔮 Making a Prediction

After loading the saved model, a new house can be passed to the model to generate a predicted price.

```python
predicted_price = loaded_model.predict(new_house)

print("Predicted price:", predicted_price[0])
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/melkamayehu/house-price-prediction.git
```

### 2. Enter the project folder

```bash
cd house-price-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the model

```bash
python src/model.py
```
# 🏠 House Price Prediction

A machine learning project that predicts house prices based on different property features using **Linear Regression**.

## 📌 Project Overview

The goal of this project is to build a machine learning model that can predict the price of a house using information such as:

* Area
* Number of bedrooms
* Number of bathrooms
* Number of stories
* Parking spaces
* Main road access
* Guest room
* Basement
* Hot water heating
* Air conditioning
* Preferred area
* Furnishing status

The project includes data exploration, preprocessing, model training, evaluation, and prediction.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook / VS Code

## 📂 Project Structure

```text
house-price-prediction/
│
├── data/
│   └── Housing.csv
│
├── src/
│   └── model.py
│
├── house_price_model.pkl
├── requirements.txt
└── README.md
```

## 🔎 Exploratory Data Analysis

The dataset was explored using:

* Dataset shape and information
* Descriptive statistics
* Missing-value checks
* Duplicate-value checks
* Price distribution
* Area vs. price analysis
* Average price by number of bedrooms
* Average price by bathrooms
* Average price by stories
* Average price by parking spaces
* Correlation analysis

## 🧹 Data Preprocessing

The dataset contains categorical variables that needed to be converted into numerical values before training the machine learning model.

### Binary Encoding

The following columns were converted from `yes`/`no` into `1`/`0`:

```text
mainroad
guestroom
basement
hotwaterheating
airconditioning
prefarea
```

### One-Hot Encoding

The `furnishingstatus` column was converted using one-hot encoding.

This created separate numerical columns for:

* Furnished
* Semi-furnished
* Unfurnished

## 🤖 Machine Learning Models

Two regression models were tested:

### 1. Linear Regression

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### 2. Random Forest Regression

```python
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

The models were compared using:

* Mean Absolute Error (MAE)
* R² Score

Based on the test results, **Linear Regression performed better on this dataset**, so it was selected as the final model.

## 📊 Model Evaluation

The Linear Regression model was evaluated using:

### MAE

Mean Absolute Error measures the average difference between the actual and predicted house prices.

**Lower is better.**

### RMSE

Root Mean Squared Error gives more weight to larger prediction errors.

**Lower is better.**

### R² Score

R² measures how much of the variation in house prices is explained by the model.

**Higher is better.**

## 💾 Saved Model

The final trained Linear Regression model was saved using Joblib:

```python
joblib.dump(model, "house_price_model.pkl")
```

The saved model can later be loaded without retraining:

```python
loaded_model = joblib.load("house_price_model.pkl")
```

## 🔮 Making a Prediction

After loading the saved model, a new house can be passed to the model to generate a predicted price.

```python
predicted_price = loaded_model.predict(new_house)

print("Predicted price:", predicted_price[0])
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/melkamayehu/house-price-prediction.git
```

### 2. Enter the project folder

```bash
cd house-price-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the model

```bash
python src/model.py
```

## 🎯 Learning Outcomes

Through this project, I practiced:

* Data cleaning
* Exploratory data analysis
* Data visualization
* Categorical encoding
* Feature and target selection
* Train/test splitting
* Linear Regression
* Random Forest Regression
* Model evaluation
* Model comparison
* Saving and loading machine learning models
* Building a complete machine learning workflow

## 🔮 Future Improvements

Possible improvements include:

* Hyperparameter tuning
* Cross-validation
* Trying additional regression algorithms
* Feature engineering
* Building a simple web interface
* Deploying the model as an application

## 👩‍💻 Author

**Melkam Ayehu**

Computer Engineering Student
Interested in Machine Learning, AI, and Computational Neuroscience.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Data cleaning
* Exploratory data analysis
* Data visualization
* Categorical encoding
* Feature and target selection
* Train/test splitting
* Linear Regression
* Random Forest Regression
* Model evaluation
* Model comparison
* Saving and loading machine learning models
* Building a complete machine learning workflow

## 🔮 Future Improvements

Possible improvements include:

* Hyperparameter tuning
* Cross-validation
* Trying additional regression algorithms
* Feature engineering
* Building a simple web interface
* Deploying the model as an application

## 👩‍💻 Author

**Melkam Ayehu**

Computer Engineering Student
Interested in Machine Learning, AI, and Computational Neuroscience.
