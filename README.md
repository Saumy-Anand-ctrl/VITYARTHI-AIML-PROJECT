# 🏠 House Price Predictor

A beginner-friendly Machine Learning project that predicts house prices (in Indian Rupees, Lakhs) using Linear Regression based on three key features: Cost of Living, Locality Rating, and City Population.

---

## 📌 Project Overview

This project demonstrates a simple supervised learning workflow using **scikit-learn's Linear Regression** model. It takes socio-economic features of a city/locality as input and predicts the approximate house price in lakhs (₹).

---

## 🧰 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core programming language |
| NumPy | Numerical operations |
| Pandas | Data handling & DataFrame |
| scikit-learn | ML model (Linear Regression) |

---

## 📁 Project Structure

```
house-price-predictor/
│
├── house_price_predictor.py   # Main Python script
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies
```

---

## 📊 Dataset

The dataset is hardcoded within the script and contains 8 sample records with the following features:

| Feature | Description | Example Value |
|---|---|---|
| `Cost_of_Living` | Annual cost of living in the city (₹) | 50000 |
| `Locality_Rating` | Rating of the area on a scale of 1–10 | 7 |
| `Population` | Approximate city population | 300000 |
| `Price` | House price in Lakhs (₹) — Target | 65 |

> ⚠️ **Note:** The dataset has only 8 records. This is suitable for demonstration but not for production use.

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Script
```bash
python house_price_predictor.py
```

### 4. Enter Input When Prompted
```
Enter details to predict house price:
  Cost of Living (e.g. 50000)       : 60000
  Locality Rating on scale 1-10     : 7
  Approximate City Population        : 280000

========================================
  Predicted House Price: ₹52.34 Lakhs
========================================
```

---

## 📦 Requirements

Create a `requirements.txt` file with the following:

```
numpy
pandas
scikit-learn
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

1. **Data Preparation** — A small dataset of 8 cities is loaded into a Pandas DataFrame.
2. **Feature Selection** — Three features (`Cost_of_Living`, `Locality_Rating`, `Population`) are selected as inputs (X), and `Price` is the target (y).
3. **Train-Test Split** — Data is split 80% training / 20% testing using `train_test_split`.
4. **Model Training** — A `LinearRegression` model from scikit-learn is trained on the training set.
5. **Evaluation** — The model is evaluated using **MAE** (Mean Absolute Error) and **R² Score**.
6. **Prediction** — The user inputs custom values and gets a predicted house price.

---

## 📈 Model Evaluation Metrics

| Metric | Description |
|---|---|
| **MAE** | Mean Absolute Error — average prediction error in lakhs |
| **R² Score** | Coefficient of Determination — how well the model fits (1.0 = perfect) |

---

## ⚠️ Limitations

- Only 8 data points — model may overfit and not generalize well to real-world data.
- No feature scaling applied (not required for Linear Regression but useful for others).
- No handling of multicollinearity between features.
- Dataset does not account for other important factors like bedroom count, age of property, amenities, etc.

---

## 🔮 Future Improvements

- [ ] Expand dataset with real-world data (e.g., from housing APIs or Kaggle datasets)
- [ ] Add more features: number of bedrooms, floor area, proximity to schools/hospitals
- [ ] Try other models: Decision Tree, Random Forest, XGBoost
- [ ] Build a web interface using Flask or Streamlit
- [ ] Add data visualizations (scatter plots, correlation heatmap)

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- Email: your.email@example.com

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
