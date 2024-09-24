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

## Codes & Model Deployment

We employed a one-hot encoder to encode the vehicle type and subsequently dropped the following columns: 'Timestamp', 'FastagID', 'Vehicle_Type', 'TollBoothID', 'Geographical_Location', and 'Vehicle_Plate_Number'.

### Ordinal Coding

We utilized an ordinal encoder to encode the columns "Lane_order," "Vehicle_Dimensions_order," and "Fraud_indicator_order".We used an ordinal encoder to encode "Lane_order," "Vehicle_Dimensions_order," and "Fraud_indicator_order," integrating the encoded values into the original table by replacing the existing columns with the new encoded columns.

### Under sampling codes

Under-sampling is a technique used in data analysis and machine learning to address class imbalance issues in datasets. Class imbalance occurs when one class (or category) of data significantly outnumbers the other classes. This can cause problems for  machine learning algorithms, as they may become biased towards the majority class and perform poorly on the minority class. Under-sampling aims to balance the class distribution by reducing the number of instances in the majority class.

### Model codes

As the Ordinal encoding and balancing of data is done. Then data is divided into train and test, then later back into x and y. 80% percent of the data is used as train data. After this the model will be created . Four machine learning models—the decision tree, random forest, logistic regression, and SVM classification on the fastag data—have been created, and we predict each one of them. The model's output is expressed as accuracy, f1 score, precision, and recall.

## After getting an accurate model now we have created a pickle file as “random_forest_model.pkl” which further will be used in flask.

## Flask code 

To connect pickle to the html file.

## WEB API

A web API is an application programming interface for either a web server or a web browser. As a web development concept, it can be related to a web application's client side. A web API is an application programming interface (API) for either a web server or a web browser. As a web development concept, it can be related to a web application's client side (including any web frameworks being used). Using the required features, a web application is developed in the Fastag Fraud Detection model. It will forecast whether fraud is occurring or not by utilizing the hidden data.

## Key insights
Decision Tree and Random Forest have a 100% in Training and Test data accuracy than Logistic Regression of 99% and an SVC of 69.09%.When comparing precision & recall for 4 models, Here the Decision tree and Random forest performed much better than the Logistics Regression and SVC as we can see that the detection of fraud cases is around 100 % and 98 %, and Logistics Regression and SVC of 72% and 62%.
So overall Decision tree and Random Forest Method performed much better in determining the fraud cases which is 100%. We can also improve on this accuracy by increasing the sample size or use deep learning algorithms however at the cost of computational expense. We can also use complex anomaly detection models to get better accuracy in determining more fraudulent cases.











