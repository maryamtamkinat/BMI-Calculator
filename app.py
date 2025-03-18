import streamlit as st

# Page Configuration
st.set_page_config(page_title="BMI Calculator", page_icon="🚀", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        .main {background-color: #f5f7fa;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 18px; border-radius: 8px; padding: 10px;}
        .stButton>button:hover {background-color: #45a049;}
        .stTextInput>div>div>input {border-radius: 8px; padding: 8px; font-size: 16px;}
        .bmi-result {text-align: center; font-size: 22px; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown("""<h1 style='text-align: center; color: #2E86C1;'>🎉 BMI Calculator</h1>""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: green;'>Enter your <b>weight & height</b> to calculate BMI.</p>", unsafe_allow_html=True)

# Input Fields
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Height (m):", min_value=0.5, format="%.2f")

# BMI Calculation
st.markdown("---")
if st.button("Calculate 🚀"): 
    if height > 0 and weight > 0:  
        bmi = weight / (height ** 2)
        st.markdown(f"<p class='bmi-result' style='color: blue;'>Your BMI is: {bmi:.2f}</p>", unsafe_allow_html=True)

        # BMI Categories with Enhanced UI
        if bmi < 18.5:
            st.error("⚠️ You are underweight. Consider a healthy diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ Your weight is normal. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight. Consider maintaining a balanced diet and exercise.")
        else:
            st.error("🚨 You are in the obesity category. Please consult a healthcare professional.")
    else:
        st.warning("Please enter valid weight and height values.")
else:
    st.info("Enter details and click Calculate to see results.")


