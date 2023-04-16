# YES BANK STOCK PRICE PREDICTION

### Introduction

The aim of this project is to predict the closing price of the Yes Bank stock for the next month. Through rigorous data analysis, it has been observed that some bad news/FUD heavily manipulated the market from 2018, which created a rug pull-like scenario as it was undetected by any indicator we have used in the project. Although signs of retracement and capitulation could have been seen through detailed analysis from mid-2018 till 2020, it was a continuous downfall and not a healthy market movement.

## Dataset

The dataset used in this project is the historical stock market data of Yes Bank from 2015 to 2020. The data was collected from Kaggle and contains information on the open, high, low and close of the month for Yes Bank's stock.

## Methedology

The following steps were followed to accomplish the project goal:

### Data cleaning and preprocessing 
The dataset was cleaned and preprocessed to remove any missing or erroneous values, and more features were added(Indicators) to ensure that a better and reliable model is being developed
### Exploratory data analysis (EDA) 
EDA was performed to identify any patterns or anomalies in the data. Various charts and graphs were plotted to visualize the trends in the data over time, including the open, high, low and close prices of the stock as well as standard market indicators like RSI 14 ATR 14 and Boolinger Bands along with various moving averages.
### Building several predictive models 
Four different models were built to forecast the closing price of the next month:

- Linear Regression: A linear regression model is a linear approach to modeling the relationship between a dependent variable and one or more independent variables.
- Decision Tree: A decision tree algorithm is a non-parametric method that constructs a tree-like model of decisions and their possible consequences.
- Random Forest: A random forest algorithm is an ensemble learning method that constructs a multitude of decision trees at training time and outputs the mode or mean prediction of the individual trees.
- SARIMAX: A seasonal autoregressive integrated moving average with exogenous variables (SARIMAX) model is a time series forecasting model that takes into account the seasonality and trend of the data and can be used to forecast future values in the series.
### Developing a custom evaluation metric 
A custom evaluation metric called "backtesting" was developed to assess the models' performance. The backtesting metric took the predicted closing value and checked if the change was more than the threshold value (a given percentage). If the change exceeded the threshold, the test was executed, and the net change of investment over 3 years was reported.
### Deploying the best performing model 
The SARIMAX model gave the best performance, with a 280% monetary gain over 3 years. The best performing model was deployed using the Streamlit library to create an interactive web app that allows users to input the desired values of Open, High, Low as well as indicator like Moving average 5,7,10,20, RSI, ATR and Bollinger Bands which will enable the web app to predict close price.

## Results 
The models were evaluated based on their ability to predict the closing price of the next month. The SARIMAX model gave the best performance, with a 280% monetary gain over 3 years with 0% threshold value followed by Linear Regression with 218% monetary gain with 2% threshold value. The evaluation metric "backtesting" was used to assess the performance of the models, which took the predicted closing value and checked if the change was more than the threshold value (a given percentage). If the change exceeded the threshold, the test was executed, and the net change of investment over 3 years was reported.

## Installation

To run the code in this repository, you need to have the following libraries installed:

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Streamlit

## Usage

To run the code, simply execute the app.py file. The Streamlit web app is deployed and can be accessed through the provided link in local host. Users can input the desired threshold value and the best performing model (SARIMAX) will predict the closing price of the next month. If the change in price exceeds the threshold value, the "backtesting" test will be executed and the net change of investment over 3 years will be reported.

## Conclusion

In conclusion, this project used various machine learning algorithms to predict the closing price of Yes Bank stock. The SARIMAX model performed the best, achieving a 280% monetary gain in our portfolio over the last three years of the dataset. The project can be used by investors to make informed decisions and predict the closing price of the stock for the next month.
