# Crash Analysis and Accident Contributing Factors

This project analyzes accident-level data from the **FARS (Fatality Analysis Reporting System)** to explore **how alcohol and other factors (weather, time of day, road conditions) contribute to crashes**.  
It focuses on **data loading, preprocessing, feature engineering, supervised learning, and exploratory analysis** to understand potential correlations and risk factors.

---

## Objectives

1. **Understand Accident Contributing Factors**  
   - Identify how alcohol involvement interacts with weather, time, and road conditions  
   - Explore which factors are most strongly associated with crash severity  

2. **Data Loading and Cleaning**  
   - Automatically finds required CSV files (`ACC_AUX.CSV`, `VEH_AUX.CSV`, `PER_AUX.CSV`)  
   - Supports loading from ZIP archives  
   - Prepares accident- and person-level datasets for analysis  

3. **Feature Engineering**  
   - Aggregates driver-level alcohol information to accident-level  
   - Encodes categorical variables (time of day, weather, road type) for analysis  

4. **Supervised Learning**  
   - Logistic Regression predicts the probability that alcohol was involved  
   - Provides accuracy, classification metrics, and feature importance  
   - Helps explore relationships between alcohol and contextual factors  

5. **Exploratory and Unsupervised Analysis**  
   - K-Means clustering or other techniques to detect patterns in crashes  
   - Examines how accident characteristics cluster by time, weather, road, and alcohol involvement  

6. **Visualization**  
   - Distribution plots and correlation charts for alcohol involvement and other factors  
   - Annotated for clear interpretation of contributing factors  

---

## Project Structure

---

## Notes

- The goal is **not just to predict alcohol involvement**, but to **investigate correlations and potential contributing factors** to crashes.  
- Supervised models serve as a tool to quantify how alcohol and other variables may increase crash risk in combination with weather, time, and road conditions.
