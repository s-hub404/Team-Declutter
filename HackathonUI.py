import streamlit as st
import pandas as pd

mobileData_df = pd.read_csv('Pricing_model.csv')
Dep_prediction_df = pd.read_csv('Price_depriciation_value.csv')

st.title("Save Nature, recycle Electronics")
st.write("""
Get the best value for your Used Mobile's \n

""")

model_name = st.selectbox("Select your model",("Iphone 12", "Oneplus 8", "Samsung S21", "Xiaomi Mi 10"))
st.write("Thanks for opting to recycle ", model_name)
is_working = st.radio('Is it in working condition ?', ['Yes','No'])
#st.write(is_working)
#months_used = st.slider("Number of months used ", min_value=1, max_value=60)

st.sidebar.image('./Ways-In-Which-Recycling-Helps-Our-Environment.png')
st.sidebar.title('Team Declutter')
st.sidebar.image('./Team.jpg')

index = 0
for ind in mobileData_df['Mobile']:
    #print(ind)
    if ind == model_name:
        mob_ind = index
    index = index + 1 
    
#st.write("MRP ", mobileData_df.iloc[mob_ind, 2])
#st.write("Months ", months_used)

if is_working == 'Yes':
    months_used = st.slider("Number of months used ", min_value=1, max_value=60)
    Dep_mobile_price = mobileData_df.iloc[mob_ind, 2]*(Dep_prediction_df.iloc[months_used-1, 1]/100) 
    st.write("Get the best price for your Model, you gets ", round(Dep_mobile_price, 2)," $")
else:
    Dep_mobile_price = mobileData_df.iloc[mob_ind, 2]*(Dep_prediction_df.iloc[47, 1]/100)
    st.write("Don't worry, we got it covered 🙂 ")
    st.write("You gets, ", round(Dep_mobile_price, 2)," $")
     
#Dep_mobile_price = mobileData_df.iloc[mob_ind, 2]*(Dep_prediction_df.iloc[months_used-1, 1]/100) 
#st.write("Get the best price for your Model, you gets ", round(Dep_mobile_price, 2)," $")





