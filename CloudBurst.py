import streamlit 
import scikit-learn sk
import pandas pd
import numpy np


page = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://th-i.thgim.com/public/incoming/1raw55/article65900336.ece/alternates/FREE_1200/WhatsApp%20Image%202022-09-16%20at%209.21.53%20PM.jpeg");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page, unsafe_allow_html=True)

try:
    model = pickle.load(open("cbmodel.pkl", "rb"))
except pickle.UnpicklingError as e:
    st.error(f"Error loading the model: {e}")
    model = None

st.title("CloudBurst")

input_tem = st.number_input("Enter the Temperature", format="%.5f")
input_atem = st.number_input("Enter the Apparent Temperature", format="%.5f")
input_hum = st.number_input("Enter the Humidity")
input_ws = st.number_input("Enter the Wind Speed", format="%.4f")
input_wb = st.number_input("Enter the Wind Bearing")
input_vis = st.number_input("Enter the Visibility", format="%.4f")
input_pre = st.number_input("Enter the Pressure")

pred = [[input_tem, input_atem, input_hum, input_ws, input_wb, input_vis, input_pre]]

if st.button("Predict"):
    if model is not None:
        result = model.predict(pred)[0]  # Get scalar value
        if result == 0:
            st.header("🛑 Cloudburst Predicted!")
        else:
            st.header("✅ No Cloudburst Predicted")
    else:
        st.error("Cannot predict: Model failed to load.")

# Remove the if _name_ == "_main_" block for deployment
