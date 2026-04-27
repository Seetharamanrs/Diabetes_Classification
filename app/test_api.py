import requests

url = "http://127.0.0.1:5000/predict"

test_cases = {
    "Non-Diabetic": {
        "Pregnancies": 0,
        "Glucose": 90,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 80,
        "BMI": 22,
        "DiabetesPedigreeFunction": 0.2,
        "Age": 25
    },
"Diabetic": {
        "Pregnancies": 6,
        "Glucose": 180,
        "BloodPressure": 90,
        "SkinThickness": 35,
        "Insulin": 200,
        "BMI": 40,
        "DiabetesPedigreeFunction": 0.8,
        "Age": 50
    },

    "Borderline": {
        "Pregnancies": 2,
        "Glucose": 135,
        "BloodPressure": 75,
        "SkinThickness": 25,
        "Insulin": 120,
        "BMI": 28,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 35
    }
}

for case_name, data in test_cases.items():
    response=requests.post(url,json=data)
    print( f"{case_name}-> {response.json()}")