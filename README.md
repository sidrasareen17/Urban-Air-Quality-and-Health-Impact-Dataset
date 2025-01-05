# Urban-Air-Quality-and-Health-Impact-Dataset

##Overview

This repository contains the implementation of a Linear Regression model aimed at predicting health risk scores based on environmental factors. The goal is to assess the relationship between weather data and health risks by analyzing various input features such as temperature, humidity, wind speed, and more.

         ## Project Description

Project Description

This project focuses on creating a linear regression model to predict the health risk score based on various environmental variables. The input data includes information such as temperature, humidity, windspeed, solar energy, and more, which are commonly associated with human health risks in various weather conditions.

Objective:

 * Build a predictive model to assess the health risk score based on the environmental data.

*  Use Linear Regression to model and understand the relationships between input features and the target health risk score.

*  Improve the accuracy and interpretability of the model using different data preprocessing techniques.

The following key features are part of the project contains:

The dataset contains several weather-related features, which are used to predict the health risk score. The dataset includes the following columns:

DateTime: Date and time of the data recording.

Temperature: Ambient temperature (in °C or °F).

Feel Like: Apparent temperature that humans feel.

Maximum Temperature: Highest recorded temperature during the given period.

Minimum Temperature: Lowest recorded temperature during the given period.

Humidity: Humidity level (as a percentage).

Snow: Snowfall amount (if applicable).

Wind Speed: Speed of the wind in the area (in km/h or mph).

Pressure: Air pressure (in hPa).

Visibility: Distance visible in the current weather conditions.

Solar Radiation: Amount of solar radiation (in W/m²).

Solar Energy: Energy derived from solar radiation.

Sunrise Hour: Hour of sunrise.

Condition: Weather condition (e.g., clear, cloudy, rainy).

Season: Season of the year (spring, summer, fall, winter).

Day of Week: Day of the week when the data was recorded.

Station Source: The source or location of the weather station.

City: City for which the data is collected.

Temperature & Humidity: These are significant variables in determining health risks, such as heat stress and dehydration.

Wind Speed & Pressure: These help in predicting environmental stability and potential storm risks.

Solar Energy & Radiation: Provides insight into UV exposure risks.

Weather Conditions: Identifying conditions like heat waves or severe storms.

Requirements:

pandas - for data manipulation

numpy - for numerical operations

scikit-learn - for building and evaluating machine learning models

matplotlib and seaborn - for data visualization

The model uses Linear Regression to predict the health risk score. The steps involved are:

1. Data Preprocessing:

Cleaning the dataset by handling missing values, encoding categorical features, and normalizing continuous variables.


2. Feature selection:

 additional features (e.g., temperature ranges, interaction between humidity and temperature) to improve model performance.

3. Model Building:

Splitting the data into training and test sets.

Training the Linear Regression model on the training data.

4. Evaluation:

Evaluating the model using metrics like Mean Squared Error (MSE), R², etc.


Results
 @Training side
 The MSE Output Is: 0.009790153792185617
********************
The RMSE Output Is: 0.09894520600911201
********************
The MAE Output Is: 0.07857408952604533
********************
The R_SQUARED Output Is: 0.9786536722994215
********************

@Testing side
The MSE Output Is: 0.013337952633846895
********************
The RMSE Output Is: 0.11549005426376288
********************
The MAE Output Is: 0.08766457135303547
********************
The R_SQUARED Output Is: 0.9718004090579153


License: 

This project  Data is licensed under the MIT License
