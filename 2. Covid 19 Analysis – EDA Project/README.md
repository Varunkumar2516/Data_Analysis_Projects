
# 🦠 COVID-19 India Data Analysis – EDA Project

![COVID Analysis](https://img.shields.io/badge/Project-COVID--19%20EDA-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

### 🔗 [View Streamlit Version]()

## 📌 Project Overview

This project focuses on **Exploratory Data Analysis (EDA)** of COVID-19 in India, utilizing publicly available datasets. The goal is to extract insights related to case trends, state-wise comparisons, vaccination distribution, and gender-based vaccination patterns.

We use two datasets:
- 📁 COVID-19 India dataset (daily cases and deaths)               [__Dataset Link__](Datasets/covid_19_india.csv)
- 💉 COVID-19 Vaccination data
[__Dataset Link__](Datasets/covid_vaccine_statewise.csv)

---

## 📊 Key Objectives

- Clean and preprocess COVID and vaccination datasets
- Analyze and visualize trends in active cases, recoveries, and deaths
- Identify states with the most severe impact (deaths, active cases)
- Study vaccination distribution across gender and states
- Compare most vs least vaccinated states

---

## 📁 Dataset Details

- **Source**: COVID-19 and Vaccination Data ( from Kaggle )
- **Files**:
  - `covid_19_india.csv` – Contains daily COVID case records - [__Dataset Link__](Datasets/covid_19_india.csv)
  - `vaccination.csv` – Contains vaccination records with demographic breakdown - [__Dataset Link__](Datasets/covid_vaccine_statewise.csv)


---

## 🧹 Data Cleaning

### 🧼 COVID Dataset:
- Dropped irrelevant columns: `Sno`, `Time`, `ConfirmedIndianNational`, etc.
- Converted `Date` column to datetime format
- Removed rows with null values

### 💉 Vaccination Dataset:
- Cleaned whitespace in column names
- dropped missing values 
- State (India ) in some rows remove those rows

---

## 🔍 Deep Analysis & Insights

### 🦠 Active Cases Analysis
- Created new column: `Active = Confirmed - (Recovered + Deaths)`
- Visualized **Top 10 states** by active cases
- Found that **Maharashtra, Kerala, Karnataka** showed the highest burden

### 💀 Top 10 States with Highest Deaths
- Used grouped data to identify top 10 states with the highest cumulative deaths
- Maharashtra significantly led in total fatalities

### 📈 Growth Trend Analysis
- Aggregated data by date and visualized trends for:
  - Confirmed cases
  - Recovered cases
  - Deaths

### 💉 Vaccination Insights

#### 👥 Male vs Female Vaccination
- Compared total vaccinations by gender
- Visualized with bar and pie charts

#### 🔝 Most Vaccinated States
- **Uttar Pradesh, Maharashtra, and Gujarat** ranked highest in vaccinations

#### 🔻 Least Vaccinated States
- **Dadra & Nagar Haveli**, **Lakshadweep**, and other small UTs had low vaccination coverage

---

## 📊 Visualization Techniques Used

- 📊 Matplotlib & Seaborn for bar charts, line plots
- 📈 Plotly for interactive visualizations
- 🧮 GroupBy and Aggregation for trend analysis
- 📅 Time-series plotting for growth over time

---

## ✅ Conclusion

Key takeaways from this analysis:

- **Maharashtra** experienced the highest deaths and active cases.
- **Uttar Pradesh** led in vaccination coverage.
- **Gender-based vaccination** data showed fairly balanced efforts.
- **Growth trends** helped understand the trajectory and effectiveness of pandemic response.

---

## 🧠 Future Scope

- Integrate **real-time data** using APIs (e.g., CoWIN)
- Apply **forecasting models** to predict future case counts or vaccination needs
- Include **age-group analysis** if data is available
- Study correlation with **mobility data** or government policy responses

---

## 📁 Folder Structure

```bash
📦 covid-india-analysis/
├── 📁AnalysisNotebook
    ├── 📄 Covid_Analysis.ipynb    # Jupyter Notebook with all analysis
├── 📁Datasets
    ├── 📄 covid_19_india.csv                             # Datafile
    ├── 📄 Covid_vaccine_statewise_Analysis.ipynb         #  Vaccination dataset
├── 📄 Covid_19AnalysisREADME.md   # Readme FIle(Summary)
