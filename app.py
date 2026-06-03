import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Loan & Credit Card Eligibility Predictor",
    page_icon="💳",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #E8F5E9;
}

/* Title */
.title {
    text-align: center;
    color: #1B5E20;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #388E3C;
    font-size: 18px;
    margin-bottom: 25px;
}

/* Card */
.card {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    border: 2px solid #C8E6C9;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.08);
}

/* Labels */
label {
    color: #1B5E20 !important;
    font-weight: 600 !important;
}

/* Subheaders */
h3 {
    color: #1B5E20 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #43A047;
    color: white;
    border-radius: 10px;
    border: none;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #2E7D32;
    color: white;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #C8E6C9;
    padding: 15px;
    border-radius: 12px;
}

/* Footer Hide */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("eligibility_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---------------- HEADER ----------------
st.markdown("""
<h1 class='title'>
💳 Loan & Credit Card Eligibility Predictor
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class='subtitle'>
Smart Financial Eligibility Checker Powered by Machine Learning
</p>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Customer Information")

income = st.number_input(
    "💰 Annual Income (₹)",
    min_value=0,
    step=10000
)

score = st.slider(
    "📊 Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if st.button("🔍 Check Eligibility"):

    data = np.array([[income, score]])
    scaled = scaler.transform(data)
    pred = model.predict(scaled)[0]

    st.markdown("---")

    # Metrics
    col1, col2 = st.columns(2)

    with col1:
        st.metric("💰 Income", f"₹{income:,.0f}")

    with col2:
        st.metric("📊 Credit Score", score)

    st.markdown("### 🎯 Prediction Result")

    if pred == 0:
        st.error("❌ Not Eligible for Loan or Credit Card")

        st.info("""
### Suggestions to Improve Eligibility

✅ Increase your income

✅ Pay bills on time

✅ Reduce existing debts

✅ Maintain a credit score above 650

✅ Avoid multiple loan applications
""")

    elif pred == 1:
        st.success("💳 Eligible for Credit Card Only")

        st.info("""
### Recommendations

✅ Keep credit utilization below 30%

✅ Continue timely repayments

✅ Build a longer credit history

✅ Increase income for future loan eligibility
""")

    elif pred == 2:
        st.success("🏦 Eligible for Loan Only")

        st.info("""
### Recommendations

✅ Improve credit score

✅ Maintain stable income

✅ Build strong repayment history

✅ Avoid late payments
""")

    elif pred == 3:
        st.balloons()

        st.success(
            "🎉 Congratulations! Eligible for Both Loan & Credit Card"
        )

        st.info("""
### Benefits

✅ High approval probability

✅ Better loan offers

✅ Premium credit card eligibility

✅ Lower interest rate opportunities

✅ Higher credit limits
""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Built with Streamlit | Machine Learning Eligibility Prediction System")