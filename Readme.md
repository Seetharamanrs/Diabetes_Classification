# Diabetes Classification & Prediction API
## Overview
    This project is an end-to-end Machine Learning application that predicts whether a patient is diabetic or not based on medical attributes. It includes data analysis, model building, and deployment using a REST API.

## Features
- Exploratory Data Analysis (EDA)
- Data preprocessing and validation
- Multiple model training and comparison
- Model optimization using hyperparameter tuning
- REST API for real-time predictions
- Scenario-based API testing
- Cloud deployment on AWS EC2

## Dataset
- Source: Pima Indians Diabetes Dataset
- Features include:
    - Pregnancies
    - Glucose
    - BloodPressure
    - SkinThickness
    - Insulin
    - BMI
    - DiabetesPedigreeFunction
    - Age
- 786 instances and 9 features
## Exploratory Data Analysis
- Analyzed feature distributions using histograms
- Compared feature behavior across diabetic and non-diabetic groups
- Identified key predictors such as Glucose, BMI, and Age
- Verified dataset quality and consistency
## Model Building
- Models used:
    - Logistic Regression
    - Random Forest Classifier
- Selected Random Forest as final model due to better performance
## Model Evaluation
- Evaluated using Accuracy, Precision, Recall 
- Confusion Matrix used for performance analysis
- Avoided overfitting by proper validation
## API Deployment
- Built using Flask
- Endpoint:
     ``` POST /predict ```
## Testing
- API tested using:
    - Postman
    - Python test script (test_cases.py)
- Created multiple scenarios:
    - Non-diabetic
    - Diabetic
    - Borderline cases


## How to Run
1. Clone repository
    - git clone <your-repo-link>
    - cd diabetes-project
2. Install dependencies
    - pip install -r requirements.txt
3. Run API
    - python app.py
4. Test API

Use Postman or run:

python ``` test/test_cases.py```   


##  Key Learnings
- Importance of data preprocessing and validation
- Understanding feature impact through EDA
- Building and comparing ML models
- Deploying ML models using REST APIs
- Ensuring consistency between training and prediction pipelines
-  Deploying ML applications on AWS EC2 and exposing public APIs

## Conclusion

    This project demonstrates a complete ML pipeline from data analysis to deployment, showcasing practical skills required for real-world AI/ML roles.