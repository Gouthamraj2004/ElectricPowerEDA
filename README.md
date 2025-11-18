# Electric Power Consumption Analysis

This repository contains Python scripts and resources for analyzing, forecasting, and categorizing electric power consumption using the Individual Household Electric Power Consumption dataset.

---

## Project Overview

This project performs the following tasks:

- Exploratory Data Analysis (EDA) including time-series visualization, anomaly identification, and hourly pattern analysis.
- Supervised Learning for time-series forecasting of next-hour global active power.
- Unsupervised Learning for anomaly detection and clustering daily consumption profiles.
- A simple rule-based AI module to categorize predicted power consumption and provide usage suggestions.

---

## Dataset

The dataset (`household_power_consumption.txt`) is **not included** 
You can download the dataset here:  
[UCI Machine Learning Repository - Individual Household Electric Power Consumption](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)

After downloading, place the file in the root directory of this project to run the scripts.

---

## Requirements

Python 3.7+ is required.  
Recommended packages:

---

## Usage Instructions

Run the Python scripts in the following order:

1. **Exploratory Data Analysis (EDA):**
python eda_power_consumption.py


3. **Supervised Learning (Forecasting):**
python forecast_power_consumption.py


4. **Unsupervised Learning (Anomaly Detection & Clustering):**
python anomaly_clustering_power_consumption.py


5. **AI Rule-Based Categorizer:**
python ai_rule_based_categorizer.py

---

## Acknowledgments

- Thanks for following this project!
---
