# Food Delivery Time Prediction Using Machine Learning

## Project Overview

This project predicts food delivery time using machine learning regression techniques.

The model uses delivery-related information such as distance, weather, traffic level, time of day, vehicle type, preparation time, and courier experience to predict the estimated delivery time in minutes.

## Objective

The objective of this project is to build and evaluate regression models that can predict:

`Delivery_Time_min`

The project follows a complete machine learning workflow from data preprocessing to model evaluation and hyperparameter tuning.

## Dataset Features

| Feature | Description |
|---|---|
| Distance_km | Distance of the delivery |
| Weather | Weather condition |
| Traffic_Level | Traffic condition |
| Time_of_Day | Time period of delivery |
| Vehicle_Type | Vehicle used for delivery |
| Preparation_Time_min | Food preparation time |
| Courier_Experience_yrs | Courier experience |
| Delivery_Time_min | Target variable |

`Order_ID` was removed because it is an identifier and does not provide useful information for prediction.

## Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Missing Value Handling
   ↓
Feature Selection
   ↓
Categorical Encoding
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Cross Validation
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Final Model Selection

Data Preprocessing
Missing Values

Numerical missing values were handled using the median.

Categorical missing values were handled using the mode.

Categorical Encoding

Categorical features were converted into numerical features using one-hot encoding.

pd.get_dummies(
    X,
    drop_first=True,
    dtype=int
)
Models Used

The following regression models were trained and evaluated:

Linear Regression

Used as the baseline regression model.

Ridge Regression

Ridge Regression was evaluated with different alpha values.

Best alpha:

1
Lasso Regression

Lasso Regression was evaluated with different alpha values.

Best alpha:

0.01
Model Performance
Test Set Results
Model	MAE	RMSE	R² Score
Linear Regression	5.899	8.826	0.826
Ridge Regression	5.904	8.829	0.826
Lasso Regression	5.906	8.833	0.826
Final Model

Linear Regression was selected as the final model based on the evaluated test-set performance.

Final Results
MAE  : 5.899
RMSE : 8.826
R²   : 0.826

The model achieved an R² score of approximately 0.826 on the test set.

Cross Validation

5-fold cross-validation was performed to evaluate model stability.

Mean R² scores:

Linear Regression : 0.7685
Ridge Regression  : 0.7686
Lasso Regression  : 0.7686

The three models showed very similar cross-validation performance.

Hyperparameter Tuning
Ridge Regression

Different alpha values were tested to identify the best regularization parameter.

Best alpha:

1
Lasso Regression

Different alpha values were tested.

Best alpha:

0.01
Model Analysis

The project includes:

Exploratory Data Analysis
Actual vs Predicted analysis
Residual analysis
Feature coefficient analysis
Cross-validation
Hyperparameter tuning
Model comparison
Model Saving

The trained model was saved using Joblib:

linear_regression_model.pkl

The feature columns used during training were also saved:

feature_columns.pkl

These files can be used to make predictions on new data.

Technologies Used
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Joblib
Jupyter Notebook
Project Structure
Food-DeliveryTime-Prediction/
│
├── Food_Delivery_Times.csv
├── project.ipynb
├── linear_regression_model.pkl
├── feature_columns.pkl
├── README.md
└── requirements.txt
Key Learning Outcomes

Through this project, I learned how to:

Clean and preprocess data
Handle missing values
Encode categorical variables
Split data into training and testing sets
Build regression models
Compare multiple regression algorithms
Apply feature scaling
Perform cross-validation
Tune hyperparameters
Evaluate regression models
Analyze model coefficients
Save trained machine learning models
Future Improvements
Feature engineering
Testing additional regression algorithms
Ensemble regression models
Advanced hyperparameter optimization
Using larger datasets
Further error analysis
Author

Jangili Ch M Srinivasa Vara Prasad

B.Tech - Computer Science and Engineering