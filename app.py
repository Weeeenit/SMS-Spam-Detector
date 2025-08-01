import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

# Load model & tokenizer
MODEL_PATH = "model/spam_model.h5"
TOKENIZER_PATH = "model/tokenizer.pkl"

model = load_model(MODEL_PATH)
with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

max_len = 50

def predict_message(msg):
    msg_clean = clean_text(msg)
    seq = tokenizer.texts_to_sequences([msg_clean])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')
    prediction = model.predict(padded)[0][0]
    label = "Spam" if prediction > 0.3 else "Ham"
    return label, prediction

# Sidebar
st.sidebar.title("About This App")
st.sidebar.markdown("""
### Features:
- AI-powered spam detection using Bidirectional LSTM.
- Trained on real-world SMS dataset.
- Detects spam like fake offers, OTP scams, etc.

**Made by:** Vinit Puri
""")

# Title
st.markdown("<h1 style='text-align: center;'>📱 SMS Spam Detector</h1>", unsafe_allow_html=True)
st.write("Detect whether an SMS message is **Spam** or **Ham (Normal)** using an AI-powered model.")

# Input form
with st.form(key="sms_form"):
    user_sms = st.text_area("Enter your SMS message:", height=100)
    submit_button = st.form_submit_button("Predict")

if submit_button and user_sms.strip():
    label, prob = predict_message(user_sms)
    st.markdown(f"### Prediction: **{label}**")
    st.write(f"**Probability:** {prob:.2f}")

# Footer
st.markdown("<hr style='margin-top:50px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Built with Streamlit & TensorFlow</p>", unsafe_allow_html=True)
