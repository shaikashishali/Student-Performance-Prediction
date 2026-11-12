# Student-Performance-Prediction


# Student Performance Prediction Using Machine Learning

## 1. Project Overview

The **Student Performance Prediction** project is a machine learning-based web application designed to predict a student's academic performance based on different factors related to their studies and daily routine.

The main goal of this project is to understand how study habits, previous academic scores, sleep hours, extracurricular activities, and practice question papers can influence a student's performance.

I developed this project using **Python and Linear Regression**. The trained machine learning model is integrated with a **Flask web application**, where users can enter their details and receive a predicted Performance Index.

The application provides a simple and user-friendly interface to make predictions easily.

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- HTML
- CSS
- Pickle

---

## 2. Dataset Information

This project uses a dataset named **Student_Performance.csv**.

The dataset contains information about students' study habits and academic performance.

### Input Features

| Feature | Description |
|---|---|
| Hours Studied | Number of hours a student spends studying |
| Previous Scores | Student's previous academic scores |
| Extracurricular Activities | Whether the student participates in extracurricular activities (Yes/No) |
| Sleep Hours | Average number of hours the student sleeps |
| Sample Question Papers Practiced | Number of practice question papers completed |

### Target Variable

**Performance Index**

The Performance Index is the target variable that the machine learning model predicts.

### Data Preprocessing

Before training the model, the dataset is prepared using the following steps:

- Load the dataset using Pandas.
- Check the dataset structure, missing values, and data types.
- Convert extracurricular activities from text into numerical values:
  - Yes = 1
  - No = 0
- Separate the input features and target variable.
- Split the dataset into training and testing sets.

---

## 3. Installation Setup

Follow these steps to run the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd Student_Performance_Prediction
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application

Make sure the trained model file `model.pkl` is available in the project directory.

Start the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

You can now enter student information and generate a performance prediction.

---

## 4. Project Structure

The project is organized into the following structure:

```text
Student_Performance_Prediction/
│
├── app.py
│
├── model.pkl
│
├── Student_Performance.csv
│
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

### File Description

- **app.py:** Flask backend that loads the trained model and handles user predictions.
- **model.pkl:** Saved Linear Regression model used to generate predictions.
- **Student_Performance.csv:** Dataset used for training and testing.
- **requirements.txt:** Contains the Python libraries required to run the project.
- **templates/index.html:** Frontend HTML page containing the prediction form.
- **static/style.css:** CSS file responsible for the application's design and styling.
- **README.md:** Project documentation.

---

## 5. Model Training Process

The machine learning model is developed using the **Linear Regression algorithm** from Scikit-learn.

The training process follows these steps:

### Step 1: Import Required Libraries

Import Pandas, NumPy, Matplotlib, Seaborn, and the required Scikit-learn modules.

### Step 2: Load the Dataset

Load `Student_Performance.csv` using Pandas.

```python
import pandas as pd

df = pd.read_csv("Student_Performance.csv")
```

### Step 3: Data Preprocessing

Convert extracurricular activities into numerical values.

```python
df["Extracurricular Activities"] = (
    df["Extracurricular Activities"].map({
        "Yes": 1,
        "No": 0
    })
)
```

### Step 4: Separate Features and Target

```python
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
```

### Step 5: Split the Dataset

Split the dataset into 80% training data and 20% testing data.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
```

### Step 6: Train the Model

Create and train the Linear Regression model.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

### Step 7: Evaluate the Model

Generate predictions on the testing dataset and evaluate the model using R² score and Mean Squared Error.

```python
from sklearn.metrics import r2_score, mean_squared_error

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R2 Score:", r2)
print("Mean Squared Error:", mse)
```

### Step 8: Save the Trained Model

Save the trained model using Pickle so that it can be reused in the Flask application without training it again.

```python
import pickle

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
```

The saved `model.pkl` file is loaded by the Flask backend to generate predictions.

---

## 6. Deployment Instructions

The Flask application can be deployed using a hosting platform such as **Render**.

### Step 1: Prepare the Project

Make sure your project contains:

- `app.py`
- `model.pkl`
- `requirements.txt`
- `templates/index.html`
- `static/style.css`

### Step 2: Create requirements.txt

Add the required dependencies:

```text
Flask
numpy
pandas
scikit-learn
gunicorn
```

### Step 3: Push the Project to GitHub

Upload your project files to a GitHub repository.

Make sure `model.pkl` is included in the repository and is accessible to the deployed application.

### Step 4: Create a Render Web Service

1. Visit https://render.com/
2. Sign in to your account.
3. Select **New +** and choose **Web Service**.
4. Connect your GitHub repository.
5. Select the repository containing your project.

### Step 5: Configure Deployment

Use the following settings:

| Setting | Value |
|---|---|
| Environment | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

### Step 6: Deploy

Click **Deploy Web Service**.

Render will install the dependencies and start the Flask application.

Once deployment is successful, Render will provide a public URL.

Open that URL to access your Student Performance Prediction application online.

---

## Conclusion

This project helped me understand how machine learning can be used to solve real-world prediction problems.

By combining Linear Regression with Flask, I created a web application that allows users to predict student performance through a simple interface.

It also gave me practical experience in data preprocessing, model training, model evaluation, Python web development, and deployment.

**Developed by:** Ashish Ali Shaik

**Project:** Student Performance Prediction

**Organization :** ViharaTech

**Visualization Screenshots :**


<img width="700" height="700" alt="pie" src="https://github.com/user-attachments/assets/20fe0ef2-309a-4020-a56b-ea1cd3a28317" />
<img width="1536" height="752" alt="pie 2" src="https://github.com/user-attachments/assets/2f98420a-30b6-4443-90d5-4646379a8233" />
<img width="700" height="400" alt="hist" src="https://github.com/user-attachments/assets/2d0e4061-e257-4e69-ac0a-8bfe067b2c0d" />
<img width="640" height="480" alt="bar_chart" src="https://github.com/user-attachments/assets/91b37a7e-b207-41c4-a9dc-002608daf47a" />


## 7. Model Results and Evaluation

After training and testing the Linear Regression model, the following results were obtained.

### Dataset Summary

| Description | Result |
|---|---:|
| Total Records | 10,000 |
| Total Features | 5 |
| Target Variable | Performance Index |
| Training Samples | 8,000 (80%) |
| Testing Samples | 2,000 (20%) |
| Missing Values | 0 |

### Model Performance

The model was evaluated using three important regression metrics: R² Score, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.9881 |
| R² Score (%) | 98.81% |
| Mean Squared Error (MSE) | 4.1056 |
| Root Mean Squared Error (RMSE) | 2.0262 |

### Understanding the Results

- **R² Score (98.81%):** The model explains approximately 98.81% of the variation in the Performance Index on the test dataset.
- **Mean Squared Error (4.1056):** This measures the average squared difference between actual and predicted values. Lower values indicate better predictions.
- **Root Mean Squared Error (2.0262):** The model's prediction errors have a root mean squared magnitude of approximately 2.03 Performance Index points.

### Model Verification

To verify the trained model, a sample input was provided:

```python
sample = [19, 80, 1, 6, 1]
```

**Input Details:**

| Feature | Value |
|---|---:|
| Hours Studied | 19 |
| Previous Scores | 80 |
| Extracurricular Activities | Yes (1) |
| Sleep Hours | 6 |
| Sample Question Papers Practiced | 1 |

**Predicted Performance Index:**

```text
[100.]
```

The model predicted a Performance Index of **100** for the given sample.

### Final Observation

The Linear Regression model achieved an R² score of approximately **98.81%** on the testing dataset, indicating a strong fit to the data. The RMSE of approximately 2.03 also suggests that the model's predictions are close to the actual Performance Index values on average in terms of squared error.

Overall, the model performed well on the test data and was successfully integrated into a Flask web application for interactive student performance prediction.

*Note: The R² score is a regression evaluation metric, not classification accuracy.*



