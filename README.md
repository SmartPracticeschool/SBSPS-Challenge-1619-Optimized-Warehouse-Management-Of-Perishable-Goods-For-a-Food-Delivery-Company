# SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company



## Table of Contents

- [Introduction](#introduction)
- [Brainstorming for Solution](#brainstorming-for-solution)
- [Proposed Solution](#proposed-solution)
- [Software Designing](#software-designing)
- [Applications](#applications)
- [Conclusion](#conclusion)
- [Future Scope](#future-scope)
- [Project Links](#project-links)
- [Reference](#reference)
- [Team Members](#team-members)
- [Screenshot](#screenshots)

##
## Introduction
This is a Software Prototype on Demand Forecasting of perishable goods using machine learning solutions. The project aims to predict number of orders a meal delivery company would receive depending upon the past.

## Brainstorming for Solution
Initaially we used LSTM model to see if we a can get a proper time series prediction but that doesnt work out good. Accuracy turns out to be bad

![LSTM](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Time%20Series%20Prediction%20Lstm.png)


![LSTM](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Time%20Prediction%20LSTM2.png)

Next we hop on to a Simple Neural Network. Again this wouldnt work as it overfitted the data easily and with regularizer it didnt produce results as good as our final competent.
![Neural Network](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Normal%20Prediction%20NN.png)

And so finally we use a pipeline of Random Forrest Regressor and then a Bayesian Ridge Regression. We divide the whole dataset into smaller ones depending on their MEAL ID as that posed as a stronger feature than CENTER ID.

## Proposed Solution
Create a data pipeline with four nodes. The first node gets predicted data, cleans it and engineers features. The second node uses RandomForestRegressor and a BayesianRidgeRegressor on features , all trained on historical data to predict the number of orders for 10 weeks in advance. Along with the features in data set it takes in account to the pattern generated in recent past (the pattern of mean of orders and errors). Taking into consideration the region we can roughly estimate the cuisine type. The third node deploys the predictions and other essential data to a web-based platform for easier conveyance. The final node replaces the historical data, with predicted data and actual data, for the same time and date 2 years back, for better training of the model.

Prediction after Random Forrest Regression
![Random Forrest Regression](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Normal%20Prediction%20Ml.png)

Prediction after Bayesian Ridge regression
![Bayesian Ridge regression](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Normal%20Prediction%20ML2.png)

## Software Designing
Also all the models were trained and the respective trained model was saved as separate .sav files. Using NodeJS they were deployed to a web platform. The user uploads an excel file with proper input and gets another excel spreadsheet with  proper output for number of orders, cuisine type and the number of employees required.

## Applications
- Used in food industries to have a rough idea about the working
- Used in warehouse management to save raw materials.
- Used to employ and manage the working of employees
- Altogether gives the food delivery company a robustness and financial stability

## Conclusion
Our project accurately predicts the number of orders from each area. So as a result, the food delivery company can estimate the total production required and number of employees to deployed to each area. Depending on the cuisine type the raw materials are ordered. Wastage can minimized further.



## Future Scope
Machine Learning (ML) and Artificial Intelligence (AI) have found their impact in every arenas and walk of life. As was Internet to 80's so is Artificial Inteligence now or even more. It is bound to bring about a new revolution in mankind.
In this project AI can predict demographic movement and thus can provide a better solution to the problem. It can also predict many other features like weather or any major change in lifestyle of people of a particular area and thus can map their effect on the number of orders. Hypothetically speaking their are countless benefits this project can draw from growing AI.

## Project Links
- [App Url](https://meal-delivery-forecast.herokuapp.com/)
- Video Demonstration 

  - [Web Page](https://drive.google.com/file/d/1do-ZuE6ucV5WKTq6Ny36zK6fRKGC8_i-/view?usp=sharing)
  
  - [Working](https://drive.google.com/file/d/1qD1K7Mxexa-Gpx9oyzuZU9-KqRHIUZyP/view?usp=sharing)
  
 - [Powerpoint](https://drive.google.com/file/d/10NywlioAOTA_0P9GxibInBeRCgXFwJVf/view?usp=sharing)

## Reference
- Data Collected from
  - [Kaggle Meal Delivery Company (https://www.kaggle.com/ghoshsaptarshi/av-genpact-hack-dec2018?rvi=1))
- [Machine Learning](https://scikit-learn.org/)
- [Neural network](https://keras.io/)(https://www.tensorflow.org/)
- [Long Short Term Memory](https://en.wikipedia.org/wiki/Long_short-term_memory)

## Team Members
| Surya Prakash Mishra (Team Lead) | Rishab Agarwal | Somya Jain |

## Screenshots

#### InputFile
![Input File](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Input%20File.png)

#### Webpage
![Web Page](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Webpage1.png)

#### Result File
![Result File](https://github.com/SmartPracticeschool/SBSPS-Challenge-1619-Optimized-Warehouse-Management-Of-Perishable-Goods-For-a-Food-Delivery-Company/blob/master/Images/Result.png)
