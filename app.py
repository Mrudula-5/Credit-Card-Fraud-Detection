import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load model
model = joblib.load("fraud_model.pkl")

# Load banner image
image = Image.open("creditcard_fraud.png")

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    # Show image banner
    st.image(image, width=450)

    st.title("🔐 Login")

    user = st.text_input("User Id")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "mrudula" and password == "1234":

            st.session_state.logged_in = True
            st.success("Login Successful ✅")
        else:
            st.error("Invalid Credentials ❌")

# ---------------- PAYMENT PAGE ----------------
else:

    # Show image banner
    st.image(image, use_container_width=True)

    st.markdown(
        """
        <style>
        .small-font {
            font-size:14px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("💳 Payments")

    # Name full width
    name = st.text_input("Name")

    # Row 1
    col1, col2 = st.columns(2)
    with col1:
        ccno = st.text_input("CC No")
    with col2:
        cvv = st.text_input("CVV Code")

    # Row 2
    col3, col4 = st.columns(2)
    with col3:
        expiry = st.text_input("Date Of Expiry")
    with col4:
        amount = st.number_input("Amount", value=0.0)

    # Row 3
    col5, col6 = st.columns(2)
    with col5:
        country = st.text_input("Country")
    with col6:
        ip = st.text_input("IP")


    st.write("---")

    if st.button("Pay"):

        # Create dummy features
        input_data = {f'V{i}': 0 for i in range(1, 29)}
        input_data['scaled_amount'] = amount

        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)

        # If amount very high OR model predicts fraud
        if amount > 2000 or prediction[0] == 1:
            st.error("⚠️ Transaction is FRAUDULENT")
        else:
            st.success("✅ Transaction is VALID")
