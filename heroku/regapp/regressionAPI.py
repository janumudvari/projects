from flask import Flask, jsonify, request
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route("/currentDetails", methods=['GET'])
def current_details():
   df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vS37MqRL0SL1twLDjX5vFw-WqICPgBW0ev_4KMR2kzzcMAWkKNQo_wnbr_QqcXXuFgBXX8K-Amogx-9/pub?output=csv")

   train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
   df_copy = train_set.copy()

   train_set_full = train_set.copy()

   train_set = train_set.drop(["hwy_mpg"], axis=1)

   train_labels = df_copy["hwy_mpg"]

   # creating model with training data
   lin_reg = LinearRegression()

   lin_reg.fit(train_set, train_labels)

   hwy_mpg_pred = lin_reg.predict(37)
   hwy_mpg_pred
   if request.method == 'GET':
        try:
            lr = lin_reg
            training_set = train_set
            labels = train_labels

            return jsonify({"score": lr.score(training_set, labels),
                            "coefficients": lr.coef_.tolist(), "intercepts": lr.intercept_})
        except (ValueError, TypeError) as e:
            return jsonify("Error when getting details - {}".format(e))
                      

if __name__ == '__main__':
    app.run(debug=True)
