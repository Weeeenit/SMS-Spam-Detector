## 📱 SMS Spam Detector

An AI-powered web app that detects whether an SMS message is **Spam** or **Ham (Normal)** using a Bidirectional LSTM model.

---

## ✨ Features
- Detects spam messages like fake offers, OTP scams, and promotions.
- Built with **TensorFlow** for model training.
- Web interface built with **Streamlit**.
- Ready for deployment on **Streamlit Cloud**.

---

## 🚀 How to Run Locally
### 1. Clone this repository
git clone https://github.com/your-username/sms-spam-detector.git
cd sms-spam-detector

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
streamlit run app.py

## 🧠 Model
- Model Type: Bidirectional LSTM
- Training Dataset: Publicly available SMS spam dataset.
- Pretrained model is included (\`spam_model.h5\`) for instant usage.


## 📂 Project Structure
SMS-Spam-Detector
-> app.py              ← Streamlit app code
-> model/              ← Folder for ML model & tokenizer
     -> spam_model.h5   ← Trained model
     -> tokenizer.pkl   ← Tokenizer
-> requirements.txt    ← Dependencies
-> README.md           ← Project documentation


## 🌐 Deployment
- Easily deployable on [Streamlit Cloud](https://share.streamlit.io/).



## 👨‍💻 Author
**Vinit Puri**
