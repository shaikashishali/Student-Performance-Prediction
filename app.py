
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template(
        'index.html',
        prediction=None,
        error=None
    )


@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours_studied = float(request.form['hours_studied'])
        previous_scores = float(request.form['previous_scores'])
        extracurricular = int(request.form['extracurricular'])
        sleep_hours = float(request.form['sleep_hours'])
        sample_papers = int(request.form['sample_papers'])

        if not 0 <= hours_studied <= 24:
            raise ValueError("Hours studied must be between 0 and 24.")

        if not 0 <= previous_scores <= 100:
            raise ValueError("Previous scores must be between 0 and 100.")

        if extracurricular not in [0, 1]:
            raise ValueError("Please select a valid extracurricular option.")

        if not 0 <= sleep_hours <= 24:
            raise ValueError("Sleep hours must be between 0 and 24.")

        if sample_papers < 0:
            raise ValueError("Sample papers cannot be negative.")

        input_data = pd.DataFrame([[
            hours_studied,
            previous_scores,
            extracurricular,
            sleep_hours,
            sample_papers
        ]], columns=[
            'Hours Studied',
            'Previous Scores',
            'Extracurricular Activities',
            'Sleep Hours',
            'Sample Question Papers Practiced'
        ])

        result = model.predict(input_data)[0]
        prediction = round(float(np.clip(result, 0, 100)), 2)

        return render_template(
            'index.html',
            prediction=prediction,
            error=None
        )

    except ValueError as e:
        return render_template(
            'index.html',
            prediction=None,
            error=str(e)
        )

    except Exception:
        return render_template(
            'index.html',
            prediction=None,
            error="Something went wrong. Please try again."
        )


if __name__ == '__main__':
    app.run(debug=True)
