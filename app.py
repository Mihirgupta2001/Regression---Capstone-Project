
import streamlit as st
import joblib
import numpy as np
from datetime import date

joblib_model = joblib.load('model_joblib')


def predict_close_price (Open, High, Low, range, sma_2, sma_5, sma_7,
         sma_10, sma_20, MACD, MACD_signal, rsi_14, atr_14, upper_bb, lower_bb):
    e = np.array([Open, High, Low, range, sma_2, sma_5, sma_7,
       sma_10, sma_20, MACD, MACD_signal, rsi_14, atr_14,
       upper_bb, lower_bb]).astype(float)
    prediction = joblib_model.predict(date(2017,12,1),exog = e)
  
    return prediction


def main():
    st.title("Stock Closing Price Predicter")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Stock Closng Price Prediction APP </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Open = st.text_input("Opening Price") 
    High = st.text_input("Highest Price") 
    Low = st.text_input("Lowest Price")
    range = st.text_input("Highest - Lowest Price")
    sma_2 = st.text_input("Simple Moving Average of 2 months") 
    sma_5 = st.text_input("Simple Moving Average of 5 months") 
    sma_7 = st.text_input("Simple Moving Average of 7 months") 
    sma_10 = st.text_input("Simple Moving Average of 10 months") 
    sma_20 = st.text_input("Simple Moving Average of 20 months") 
    MACD = st.text_input("MACD")  
    MACD_signal = st.text_input("MACD Signal")  
    rsi_14 = st.text_input("Relative Strength Index of 14 months")  
    atr_14 = st.text_input("Average True Range of 14") 
    upper_bb = st.text_input("Upper Value of Boolinger Band")  
    lower_bb = st.text_input("Lower Value of Boolinger Band") 
    result=""
    if st.button("Predict"):
        result=predict_close_price(Open, High, Low, range, sma_2, sma_5, sma_7,
         sma_10, sma_20, MACD, MACD_signal, rsi_14, atr_14, upper_bb, lower_bb)
    st.success('The Closing Price Will be {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
