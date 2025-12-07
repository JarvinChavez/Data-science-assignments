# Crash Analysis and Alcohol Involvement Prediction

This project analyzes accident-level data from the **FARS (Fatality Analysis Reporting System)** and predicts alcohol involvement in crashes.  
It covers **data loading, preprocessing, supervised & unsupervised learning, and visualizations**.

---

## Features

1. **Data Loading and Cleaning**  
   - Automatically finds required CSV files (`ACC_AUX.CSV`, `VEH_AUX.CSV`, `PER_AUX.CSV`)  
   - Supports loading from ZIP archives  
   - Prepares accident- and person-level datasets for analysis  

2. **Alcohol Involvement Label**  
   - Creates a binary label `alcohol_involved` at the accident level  
   - Aggregates driver-level alcohol test results to crash-level  

3. **Supervised Learning**  
   - Logistic Regression model predicts alcohol involvement  
   - Provides accuracy, classification report, and feature importance  

4. **Unsupervised Learning**  
   - K-Means clustering to explore patterns in crashes  
   - Clusters accidents by time of day, weather, and road type  

5. **Visualization**  
   - Distribution plots for alcohol involvement, time of day, and weather  
   - Annotated for easy interpretation  

---

## Project Structure

project/
│
├─ data/ # Raw data files (CSV or ZIP)
├─ notebooks/ # Jupyter notebooks for analysis
├─ models/ # Serialized trained models (.joblib)
├─ scripts/ # Python scripts for processing & modeling
├─ README.md # Project documentation