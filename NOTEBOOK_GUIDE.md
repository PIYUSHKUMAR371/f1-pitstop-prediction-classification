# 🏎️ Formula 1 Pit Stop Prediction - ML Pipeline

A complete Machine Learning pipeline for predicting Formula 1 pit stop outcomes using classification techniques.

## 📌 Project Overview

This project builds a highly accurate predictive model to determine whether a pit stop will occur on the next lap in F1 racing. The original `f1_pediction_stops.ipynb` notebook was split into **4 smaller Jupyter notebooks** so the project renders more cleanly on GitHub and avoids oversized notebook issues.

## 📊 Dataset

- **Training Set**: `data/train.csv` - Contains historical race data with pit stop labels
- **Test Set**: `data/test.csv` - Contains unlabeled race data for predictions  
- **Target Variable**: `PitNextLap` - Binary classification (0 or 1)

## 🔄 Pipeline Structure

The complete workflow consists of **4 sequential notebooks**:

### **1️⃣ Part 1: Data Loading & EDA**
📄 Notebook: `01_Data_Loading_EDA.ipynb`

- Load training and test datasets
- Inspect data shapes, types, and structure
- Missing values analysis
- Exploratory Data Analysis (EDA):
  - Driver performance analysis
  - Tyre compound behavior
  - Race progression analysis
  - Target variable distribution
  - Correlation analysis

**Output**: Understanding of data structure and patterns

---

### **2️⃣ Part 2: Feature Engineering & Preprocessing**
📄 Notebook: `02_Feature_Engineering_and_Preprocessing.ipynb`

- Detailed numerical feature analysis (distributions, skewness, outliers)
- Detailed categorical feature analysis (value distributions)
- **Categorical Variable Encoding** using Label Encoding
  - Driver encoding
  - Compound encoding
  - Race encoding
- Feature selection (separate features and target)
- Train-Validation Split (80-20 split with stratification)
- **Save prepared datasets** for next notebook

**Outputs**: 
- `label_encoders.pkl` - Categorical encoders
- `X_train.csv, X_valid.csv, y_train.csv, y_valid.csv, X_test.csv` - Prepared datasets

---

### **3️⃣ Part 3: Model Training & Evaluation**
📄 Notebook: `03_Model_Training_Evaluation.ipynb`

- Load prepared datasets from Part 2
- **Train XGBoost Classifier** (500 estimators)
- Model Evaluation:
  - Accuracy score
  - AUC/ROC curve
  - Confusion matrix
  - Classification report
- **Feature Importance Analysis** - Identify top predictive features
- **Save trained model** for predictions

**Key Metrics**:
- Accuracy: ~[Will be shown when notebook runs]
- AUC Score: ~[Will be shown when notebook runs]

**Output**: `xgboost_pitstop_model.pkl` - Trained model

---

### **4️⃣ Part 4: Prediction & Submission**
📄 Notebook: `04_Prediction_and_Submission.ipynb`

- Load trained model from Part 3
- Load test data
- **Generate predictions** on test set
- **Create submission file**: `submission.csv`
- Final validation and summary

**Output**: `submission.csv` - Ready for submission!

---

## 🚀 How to Run

### **Step 1️⃣: Run Part 1**
```
Open and execute: 01_Data_Loading_EDA.ipynb
```
This loads and explores the data.

### **Step 2️⃣: Run Part 2**
```
Open and execute: 02_Feature_Engineering_and_Preprocessing.ipynb
```
This prepares the data and saves:
- Encoded datasets (CSV files)
- Label encoders (PKL file)

### **Step 3️⃣: Run Part 3**
```
Open and execute: 03_Model_Training_Evaluation.ipynb
```
This trains the model and saves:
- Trained XGBoost model (PKL file)

### **Step 4️⃣: Run Part 4**
```
Open and execute: 04_Prediction_and_Submission.ipynb
```
This generates the final `submission.csv` file.

---

## 📦 Dependencies

Required libraries (see `requirements.txt`):
```
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
joblib
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
f1-pitstop-prediction-classification/
├── 01_Data_Loading_EDA.ipynb                   # Part 1: Data loading & EDA
├── 02_Feature_Engineering_and_Preprocessing.ipynb  # Part 2: Feature engineering & prep
├── 03_Model_Training_Evaluation.ipynb          # Part 3: Model training
├── 04_Prediction_and_Submission.ipynb          # Part 4: Prediction & submission
├── data/
│   ├── train.csv                          # Training data
│   ├── test.csv                           # Test data
│   └── sample_submission.csv              # Submission format
├── label_encoders.pkl                     # Saved encoders (generated in Part 2)
├── xgboost_pitstop_model.pkl              # Saved model (generated in Part 3)
├── submission.csv                         # Final submission (generated in Part 4)
├── X_train.csv, X_valid.csv, y_train.csv # Prepared data (generated in Part 2)
├── y_valid.csv, X_test.csv
├── api.py                                 # API for model deployment
├── README.md                              # This file
└── requirements.txt                       # Dependencies
```

---

## 🎯 Model Details

### **Algorithm**: XGBoost Classifier
- **Estimators**: 500
- **Learning Rate**: 0.05
- **Max Depth**: 6
- **Subsample**: 0.8
- **Colsample by Tree**: 0.8
- **Objective**: Binary classification
- **Evaluation Metric**: AUC

### **Why XGBoost?**
✅ Excellent for tabular/structured data  
✅ Handles feature interactions well  
✅ Fast training and prediction  
✅ Built-in feature importance  
✅ Robust to outliers  

---

## 📊 Feature Categories

### **Numerical Features**:
- LapTime (s)
- TyreLife
- RaceProgress
- Position
- GapToLeader
- And more...

### **Categorical Features**:
- Driver
- Compound (Tyre type)
- Race

---

## 📈 Evaluation Metrics

The model is evaluated using:
1. **Accuracy** - Percentage of correct predictions
2. **AUC Score** - Area Under ROC Curve (0-1, higher is better)
3. **Confusion Matrix** - True/False Positives and Negatives
4. **Classification Report** - Precision, Recall, F1-Score
5. **ROC Curve** - Trade-off between TPR and FPR

---

## 🔍 Key Insights

The notebooks will reveal:
- Which features are most important for pit stop prediction
- Driver-specific pit stop patterns
- Impact of tyre compounds on pit stops
- Race progression effects
- Feature correlations and relationships

---

## ✅ Output Files

After running all notebooks, you'll have:

| File | Purpose | Generated in |
|------|---------|--------------|
| `submission.csv` | Final predictions for submission | Part 4 |
| `xgboost_pitstop_model.pkl` | Trained model | Part 3 |
| `label_encoders.pkl` | Categorical encoders | Part 2 |
| `X_train.csv` | Training features | Part 2 |
| `X_valid.csv` | Validation features | Part 2 |
| `y_train.csv` | Training target | Part 2 |
| `y_valid.csv` | Validation target | Part 2 |
| `X_test.csv` | Test features | Part 2 |

---

## 🤝 Contribution & Improvement

Potential improvements:
- Try different algorithms (LightGBM, CatBoost, RandomForest)
- Perform hyperparameter tuning
- Add feature engineering
- Ensemble multiple models
- Use cross-validation for better evaluation
- Analyze prediction confidence/probabilities

---

## 📝 Notes

- **Why split into 4 notebooks?** GitHub has a rendering limit (~5MB). Splitting avoids this issue and makes the code more digestible.
- **Run in sequence**: Parts depend on previous outputs. Don't skip any!
- **Reproducibility**: Random seeds are set for consistent results.
- **Data Integrity**: No modifications to original data files during processing.

---

## 🎓 Learning Outcomes

After completing this pipeline, you'll understand:
- ✅ Complete ML workflow from data to deployment
- ✅ Exploratory Data Analysis (EDA) techniques
- ✅ Feature engineering and categorical encoding
- ✅ Train-validation split and stratification
- ✅ XGBoost classifier training
- ✅ Model evaluation metrics
- ✅ Feature importance analysis
- ✅ Generating predictions and submissions

---

## 📞 Support

For issues or questions:
1. Check that all previous notebooks have been run
2. Verify all data files are in `data/` folder
3. Ensure all dependencies are installed
4. Check file paths match your setup

---

## 📄 License

This project is provided as-is for educational purposes.

---

**Happy Predicting! 🏁**
