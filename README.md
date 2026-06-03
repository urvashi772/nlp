 **💳 Loan & Credit Card Eligibility Predictor**

**Live Project Link :**  https://hgekzqwmm3kx7yqgp5jkst.streamlit.app/

**📌 Project Overview**

The **Loan & Credit Card Eligibility Predictor** is a Machine Learning-powered web application that helps determine whether a customer is eligible for a **Loan**, **Credit Card**, **Both**, or **Neither** based on their financial information.

The application provides instant predictions using a trained classification model and presents results through an intuitive and user-friendly Streamlit interface.

---

**🚀 Features**

* Predicts customer eligibility in real time
* Supports four prediction categories:

  * ❌ Not Eligible
  * 💳 Credit Card Only
  * 🏦 Loan Only
  * 💳🏦 Both Loan & Credit Card
* Interactive Streamlit dashboard
* Credit score slider input
* Income-based eligibility assessment
* Personalized recommendations based on prediction results
* Modern and professional UI design

---

**🛠️ Technologies Used**

* Python
* Streamlit
* NumPy
* Scikit-learn
* Pickle
* Machine Learning

---

**📂 Project Structure**

```text
Loan-Credit-Card-Eligibility-Predictor/
│
├── app.py
├── eligibility_model.pkl
├── scaler.pkl
├── requirements.txt
├── dataset.csv
└── README.md
```

---

**📊 Input Parameters**

| Feature       | Description                      |
| ------------- | -------------------------------- |
| Annual Income | Customer's yearly income         |
| Credit Score  | Creditworthiness score (300–900) |

---

**🎯 Prediction Classes**

| Output | Meaning                 |
| ------ | ----------------------- |
| 0      | Not Eligible            |
| 1      | Credit Card Only        |
| 2      | Loan Only               |
| 3      | Both Loan & Credit Card |

---

**⚙️ Installation**

**Clone Repository**

```bash
git clone https://github.com/urvashi772/Loan-Credit-Card-Eligibility-Predictor.git
```

**Navigate to Project Directory**

```bash
cd Loan-Credit-Card-Eligibility-Predictor
```

**Install Dependencies**

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User enters annual income.
2. User selects credit score.
3. Input data is scaled using the saved scaler.
4. Machine Learning model predicts eligibility.
5. Application displays prediction and recommendations.

---

## 📈 Machine Learning Workflow

* Data Collection
* Data Preprocessing
* Feature Scaling
* Model Training
* Model Evaluation
* Model Serialization using Pickle
* Deployment with Streamlit

---

## 📸 Application Preview

Add screenshots of application.

<img width="1166" height="802" alt="2" src="https://github.com/user-attachments/assets/88275457-12d5-4300-b92f-a2a1ffe02a28" />
<img width="1134" height="802" alt="2 2" src="https://github.com/user-attachments/assets/7b7eef6a-ddbf-4490-94b8-d571fe1fe600" />
<img width="1179" height="810" alt="1" src="https://github.com/user-attachments/assets/94a72c0b-654a-4e23-b61d-d66ccc98fb5f" />
<img width="1090" height="802" alt="1 1" src="https://github.com/user-attachments/assets/f0a490b7-614f-4ec0-8572-ec182cc5293c" />


---

## 🔮 Future Enhancements

* Add age and employment status
* Include loan amount prediction
* Credit risk analysis
* Multiple ML model comparison
* Database integration
* Cloud deployment

---

## 👩‍💻 Author

**Urvashi Chotaliya**

Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer


This project is developed for educational and portfolio purposes.
