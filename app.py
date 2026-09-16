import streamlit as st
import joblib

# Load model
model = joblib.load('salary_model.pkl')

# Page config
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: gray;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.title("💼 Employee Salary Predictor")
    st.markdown("### 🔧 Created by **John Annish Colin**")
    st.markdown("📧 johnannishcolin@gmail.com")
    st.markdown("---")

    # Input
    age = st.slider("📅 Age", 18, 90, 30)
    education_num = st.slider("🎓 Education Level (numeric)", 1, 16, 10)
    hours_per_week = st.slider("⏰ Hours per Week", 1, 100, 40)

    # Predict
    if st.button("💰 Predict Salary Level"):
        input_data = [[age, education_num, hours_per_week]]
        prediction = model.predict(input_data)[0]

        if prediction >= 0.5:
            st.success("✅ Prediction: High Salary (More than ₹50K)")
        else:
            st.info("💡 Prediction: Low Salary (₹50K or Less)")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">🔗 Built using Streamlit | Developed by John Annish Colin</div>', unsafe_allow_html=True)
