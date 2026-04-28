from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app=Flask(__name__)
base_dir=os.path.dirname(os.path.abspath(__file__))
pr_root=os.path.dirname(base_dir)
model_path=os.path.join(pr_root,"model",'model.pkl')

model=joblib.load(model_path)

@app.route("/")
def home():
    return "Diabetes Prediction API is running!"

@app.route("/predict",methods=['POST'])
def predict():
    data= request.get_json()
    features=np.array([list(data.values())])
    prediction = model.predict(features)[0]
    proba=model.predict_proba(features)[0][1]
    return jsonify(   { "prediction": int(prediction),
    "probability": float(proba)})

if __name__=="__main__":
    app.run(debug=True)