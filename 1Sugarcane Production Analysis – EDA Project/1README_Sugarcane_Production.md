
# 🌾 Sugarcane Production Analysis – EDA Project

![DATA SCIENCE](https://img.shields.io/badge/EDA-Pandas%20%7C%20Matplotlib%20%7C%20Seaborn-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on global sugarcane production data. It explores critical variables such as:

- 🌱 **Production Volume**
- 🌾 **Land Usage (Acreage)**
- 🌿 **Yield per Hectare**
- 👤 **Production per Person**

The goal is to uncover insights into how different countries and continents contribute to sugarcane production, identify top producers, evaluate efficiency, and support data-driven decisions in agricultural strategy and resource management.

---

## 📊 Dataset

- 📄 **CSV File**: [List of Countries by Sugarcane Production](List%20of%20Countries%20by%20Sugarcane%20Production.csv)
- 📦 **Repo**: [RepoLink](https://github.com/Varunkumar2516/Data_Analysis_Projects.git)

---

## 🧹 Data Cleaning

**✔ Removed Unwanted Characters:**
- Periods (`.`) used as thousands separators
- Commas (`,`) standardized for decimals

**✔ Dropped Unnecessary Columns:**
- Example: `Unnamed: 0`

**✔ Renamed Columns:**
- Standardized names like `Production (Tons)` → `Production(Tons)`

**✔ Handled Missing Values:**
- Dropped rows with missing `Acreage(Hectare)` and `Yield(Kg/Hectare)`

**✔ Converted Data Types:**
- Converted to `float` for numeric operations

---

## 🔍 Exploratory Data Analysis

### 🟦 Univariate Analysis

- **Countries by Continent**:
  - 🌍 Africa (38)
  - 🌏 Asia (25)
  - 🌎 North America (22)
  - 🌎 South America (11)
  - 🌐 Oceania (4)
  - 🇪🇺 Europe (2)

- **Distribution Insights**:
  - Production and per-person values are right-skewed
  - Outliers like Brazil, India, and China dominate

- **High Yield Efficiency**:
  - Guatemala and Egypt stand out

---

### 🟩 Bivariate Analysis

- 🇧🇷 **Top Producer**: Brazil (≈ 768M Tons)
- 🌿 **Highest Acreage**: Brazil > India > China
- 💧 **Highest Yield**: Guatemala (≈ 129,049 Kg/Hectare)
- 👥 **Per Capita Production**: Paraguay leads

**Correlations:**
- 🟢 Strong: `Acreage` ↔ `Production` (0.997)
- 🔴 Weak: `Yield` ↔ `Production` (0.13)

📉 Scatter Plots show:
- More land = more production
- Higher yield ≠ higher total output

---

### 🟨 Continental Insights

- **Top Producers**:
  - 🥇 South America
  - 🥈 Asia
  - 🥉 North America

- **Country Count ≠ Output**:
  - South America has fewer countries but leads due to Brazil

---

## ✅ Conclusion

Key takeaways from the analysis:

- **Brazil** is the top producer with highest acreage and output
- **Guatemala** demonstrates optimal yield efficiency
- **South America** dominates despite fewer countries
- **Land area** is a better predictor of production than yield efficiency

These insights are valuable for optimizing land use, targeting yield improvements, and guiding policy for sustainable agriculture.

---

## 📁 Files Included

```bash
📦 Sugarcane-Production-EDA/
├── 📄 Sugarcane_Production_Analysis.ipynb
├── 📄 README.md
└── 📄 List of Countries by Sugarcane Production.csv
```

---

## 🧠 Future Scope

- ⏳ Add time-series trend analysis (multi-year data)
- 🔮 Implement ML models for production forecasting
- 🌍 Evaluate environmental impact in top-producing regions

---


