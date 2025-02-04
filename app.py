import streamlit as st
import pandas as pd 
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

model.fit(x,y)

st.title("Prevendo o valor de uma pizza")