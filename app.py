import streamlit as st

# Page Configuration
st.set_page_config(page_title="BMI Calculator", page_icon="🚀", layout="centered")

# Title & Description
st.title("🎉 BMI Calculator")
st.markdown("<p style='color: green;'>Enter your **weight & height** to calculate BMI.</p>",unsafe_allow_html=True)

# Input Fields
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Height (m):", min_value=0.5, format="%.2f") 

# BMI Calculation
if st.button("Calculate"): 
    if height > 0 and weight > 0:  
        bmi = weight / (height ** 2)
    
    st.subheader("Your BMI is:")
    st.markdown(f"<h3 style='color: blue;'>{bmi:.2f}</h3>", unsafe_allow_html=True)

    # BMI Categories
    if bmi < 18.5:
        st.error("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("Your weight is normal.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are in the obesity category.")
else:
    st.info("Please enter a valid weight and height.")

