# 🏎️ F1 Pit Stop Prediction Classification

An end-to-end Machine Learning project focused on predicting whether a Formula 1 car will make a pit stop on the next lap using race telemetry and strategic race data.

This project includes:
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- XGBoost Classification
- ROC-AUC Evaluation
- Feature Importance Analysis
- FastAPI Deployment
- Real-time Prediction API

---

# 📌 Project Type

Supervised Machine Learning — Binary Classification

---

# Notebook rendering note

The original monolithic notebook was split into smaller Jupyter notebooks so the project renders more cleanly on GitHub and avoids oversized notebook issues.

The workflow is now organized into:
- `01_Data_Loading_EDA.ipynb`
- `02_Feature_Engineering_and_Preprocessing.ipynb`
- `03_Model_Training_Evaluation.ipynb`
- `04_Prediction_and_Submission.ipynb`

This keeps the full analysis readable and easier to run step by step.

If you want to open the original combined notebook in Colab, use:
```
https://colab.research.google.com/github/PIYUSHKUMAR371/f1-pitstop-prediction-classification/blob/main/f1_pediction_stops.ipynb
```

# 🎯 Objective

The goal of this project is to predict:

> Will the car pit on the next lap?

Target Variable:

```python
PitNextLap
```

- `1` → Pit stop expected next lap
- `0` → No pit stop expected

---

# 📂 Dataset

Dataset Source:
- Kaggle Playground Series — Season 6 Episode 5

Dataset Files:
- `train.csv`
- `test.csv`
- `sample_submission.csv`

---

# 📊 Features Used

| Feature | Description |
|---|---|
| Driver | Driver Identifier |
| Compound | Tyre Compound |
| Race | Grand Prix Name |
| Year | Race Year |
| PitStop | Current Pit Status |
| LapNumber | Current Lap |
| Stint | Current Stint |
| TyreLife | Tyre Age |
| Position | Current Position |
| LapTime (s) | Lap Time |
| LapTime_Delta | Lap Time Difference |
| Cumulative_Degradation | Tyre Degradation |
| RaceProgress | Race Completion Percentage |
| Position_Change | Position Gain/Loss |

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- FastAPI
- Uvicorn
- Joblib

---

# 📈 Exploratory Data Analysis (EDA)

The project includes extensive visualization and analysis of:
- Numerical feature distributions
- Categorical feature analysis
- Correlation heatmaps
- Boxplots
- Histograms
- Countplots
- Feature relationships
- Outlier analysis
- Class distribution analysis

---

# 🤖 Machine Learning Model

Model Used:

```python
XGBClassifier
```

Reason for choosing XGBoost:
- High performance on structured/tabular data
- Handles non-linear relationships well
- Excellent classification accuracy
- Strong feature importance analysis
- Robust against overfitting

---

# 📉 Model Evaluation

Evaluation Metrics Used:
- Accuracy Score
- ROC-AUC Score
- Classification Report
- Confusion Matrix
- Precision-Recall Curve

---

# 🚀 Model Performance

## ROC-AUC Score

```python
0.9471
```

This indicates excellent classification performance.

---

# 📊 ROC Curve

The ROC curve demonstrates strong separation capability between pit stop and non-pit stop classes.

---

# 🔥 Feature Importance

Feature importance analysis was performed to identify the most influential variables affecting pit stop prediction.

Important features included:
- TyreLife
- LapTime_Delta
- Cumulative_Degradation
- RaceProgress
- LapTime (s)

---

# 💾 Model Serialization

The trained model was saved using:

```python
joblib
```

Generated files:
- `xgboost_pitstop_model.pkl`
- `label_encoders.pkl`

---

# 🌐 FastAPI Deployment

This project includes a real-time prediction API using FastAPI.

---

# ▶️ Running the API

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI Server

```bash
uvicorn api:app --reload
```

---

# 📍 API Documentation

After running the server:

```text
http://127.0.0.1:8000/docs
```

Swagger UI will open automatically.

---

# 🧪 Example API Request

```json
{
  "Driver": "D109",
  "Compound": "HARD",
  "Race": "Canadian Grand Prix",
  "Year": 2022,
  "PitStop": 0,
  "LapNumber": 50,
  "Stint": 2,
  "TyreLife": 39.0,
  "Position": 8,
  "LapTime_s": 78.491,
  "LapTime_Delta": -7.564,
  "Cumulative_Degradation": 21.019,
  "RaceProgress": 0.714,
  "Position_Change": 5.0
}
```

---

# ✅ Example API Response

```json
{
  "PitNextLapPrediction": 1,
  "Probability": 0.8375
}
```

---

# 📁 Project Structure

```text
f1-pitstop-prediction-classification/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
│
├── f1_pediction_stops.ipynb                     # Original combined notebook kept for reference
├── 01_Data_Loading_EDA.ipynb                   # Step 1: data loading & EDA
├── 02_Feature_Engineering_and_Preprocessing.ipynb  # Step 2: feature engineering & prep
├── 03_Model_Training_Evaluation.ipynb          # Step 3: training & evaluation
├── 04_Prediction_and_Submission.ipynb          # Step 4: predictions & submission
│
├── api.py
├── requirements.txt
├── submission.csv
├── xgboost_pitstop_model.pkl
├── label_encoders.pkl
├── NOTEBOOK_GUIDE.md
├── README.md
└── .gitignore
```

---

# 📌 Future Improvements

Possible future enhancements:
- Hyperparameter tuning
- Cross-validation optimization
- Streamlit dashboard
- Docker deployment
- Cloud deployment
- Real-time telemetry integration
- Advanced feature engineering
- Ensemble learning

---

# 🏁 Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow:
- Data preprocessing
- EDA
- Visualization
- Classification modeling
- Evaluation
- Deployment
- API inference

The project successfully predicts Formula 1 pit stop behavior with strong classification performance.

---

# 👨‍💻 Author

Piyush Kumar

GitHub:
https://github.com/PIYUSHKUMAR371
