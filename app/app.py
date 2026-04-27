from flask import Flask, request, jsonify
import joblib
import numpy as np

app=Flask(__name__)

model=joblib.load(r"D:\my_git\Diabetes_Classification\model\model.pkl")
scaler=joblib.load(r'D:\my_git\Diabetes_Classification\model\scaler.pkl')

@app.route("/")
def home():
    return "Diabetes Prediction API is running!"

@app.route("/predict",methods=['POST'])
def predict():
    data= request.get_json()
    features=np.array([list(data.values())])
    # features_scaled=scaler.transform(features)
    prediction = model.predict(features)[0]
    proba=model.predict_proba(features)[0][1]
    return jsonify(   { "prediction": int(prediction),
    "probability": float(proba)})

if __name__=="__main__":
    app.run(debug=True)