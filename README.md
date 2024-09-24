# Fastag-Fraud-detection-Model

## Objective

The  project aims to develop a machine learning-based fraud detection system for Fastag transactions. Utilizing a dataset containing transaction details, vehicle information, geographical locations, and transaction amounts, the objective is to build a robust classification model. This model will accurately identify fraudulent activities, ensuring the security and integrity of Fastag transactions.


## Steps

- DATA EXTRACTION:- Extract the necessary dataset from KAGGLE Repository. Load the dataset in Python .Use python codes to get a overview of the dataset.
- DATA CLEANING:- Address any missing, duplicate, data type conversion or inconsistent data. This includes writing codes to clean the data.
- DATA ENCODING:- Data encoding is a crucial step in preparing your dataset for machine learning models. It involves converting categorical data into a numerical format that can be used by the algorithms.
- DATA UNDERSAMPLING:- Undersampling involves reducing the number of instances in the majority class to match the number of instances in the minority class. This can help create a more balanced dataset, which can 
  improve the performance of machine learning models.
- DATA SPLITTING:- Divide the data into training, validation, and test sets.
- MODEL TRAINING:- Train the chosen models on the training data.
- MODEL EVALUATION:- Choose appropriate metrics (e.g., accuracy, precision, recall, F1-score) to measure performance. Use the validation set to evaluate models performance.
- TEST THE MODEL:- Evaluate the models on the test set. Ensure the model performs well on unseen data.
- FINAL MODEL:- Select the model that you have to take forward for deployment purpose.
- DEVELOP A WEB API:-Using the required features, a web application is developed in the Fastag Fraud Detection model.

## Data Description

Columns:
-Transaction_ID: Unique identifier for each transaction.
-Timestamp: Date and time of the transaction.
-Vehicle_Type: Type of vehicle (e.g., Bus, Car, Motorcycle, Truck, Van).
-FastagID: Unique identifier for the Fastag used.
-TollBoothID: Identifier for the toll booth.
-Lane_Type: Type of lane (e.g., Express, Regular).
-Vehicle_Dimensions: Size category of the vehicle (e.g., Small, Medium, Large).
-Transaction_Amount: Total amount charged for the transaction.
-Amount_paid: Amount actually paid.
-Geographical_Location: Latitude and longitude of the transaction.
-Vehicle_Speed: Speed of the vehicle during the transaction.
-Vehicle_Plate_Number: License plate number of the vehicle.
-Fraud_indicator: Indicator of whether the transaction was fraudulent (Fraud, Not Fraud).




