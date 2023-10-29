from flask import Flask
from flask import jsonify,request
import pickle
from waitress import serve
import pandas as pd

def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('standardscaler.bin')
model = load('lgb_model.bin')

def preprocess(df):
    df['Gender_Male']=df['Gender'].apply(lambda x: 1 if x == 'Male' else 0)   
    df['Vehicle_Age_< 1 Year']=df['Vehicle_Age'].apply(lambda x: 1 if x == '< 1 Year' else 0)
    df['Vehicle_Age_> 2 Years']=df['Vehicle_Age'].apply(lambda x: 1 if x == '> 2 Years' else 0)
    df['Vehicle_Damage_Yes']=df['Vehicle_Damage'].apply( lambda x : 1 if x =='Yes' else 0) 
    df.drop(columns=['Vehicle_Damage','Vehicle_Age','Gender','id'],inplace=True)
    return df


app = Flask('PeopleCare')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    client = preprocess(pd.DataFrame([client]))
    X = dv.transform(client)
    y_pred = model.predict_proba(X)[0, 1]
    return jsonify({'prediction': float(y_pred),
                    "interested in purchase of insurance": bool(y_pred >= 0.5)})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)   
