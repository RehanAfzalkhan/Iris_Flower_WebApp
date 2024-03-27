import joblib
import pandas as pd
import streamlit as st

#load the dataset
iris_pd=pd.read_csv("../datasets/Iris.csv")
#drop the id column
iris_pd.drop("Id", axis=1, inplace=True)

knn_model = joblib.load("../Persistence/knn_model.sav")
scalar = joblib.load("../Persistence/scaler_features.sav")
encoder = joblib.load("../Persistence/label_encoder.sav")
st.sidebar.header("Input parameters")
sl=st.sidebar.slider("Select Sepal Length",0.0,10.0,5.0)
sw=st.sidebar.slider("Select Sepal width",0.0,10.0,5.0)
pl=st.sidebar.slider("Select Petal length",0.0,10.0,5.0)
pw=st.sidebar.slider("Select Petal width",0.0,10.0,5.0)

new_data=[[sl,sw,pl,pw]]
new_data_scaled=scalar.transform(new_data)
predictions=knn_model.predict(new_data_scaled)
encoded_predictions=encoder.inverse_transform(predictions)

st.write("""
# Iris Flower prediction App
This app predicts the **Iris flower** type!         
""")

st.write(iris_pd)
st.write("""
#Prediction
The predicted iris flower is:         
""")

st.write(encoded_predictions[0])
if encoded_predictions[0]=="Iris-virginica":
    st.image("../pics/verginca.JPG")
elif encoded_predictions[0]=="Iris-versicolor":
    st.image("../pics/versicolor.JPG")
elif encoded_predictions[0]=="Iris-setosa":
    st.image("../pics/setosa.JPG")
