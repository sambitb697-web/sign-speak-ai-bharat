import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sign Speak AI Bharat", layout="centered")
st.title("🤟 Sign Speak AI Bharat")
st.markdown("**NXTWAVE Hackathon Project** - Sign Language se baat karo, AI awaaz me jawab dega")

api_key = st.text_input("Google AI API Key daalo", type="password")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.warning("Pehle API Key daalo: https://aistudio.google.com/app/apikey")
    st.stop()

SIGN_DICT = {"hand_up": "Hello", "fist": "Help", "two_fingers": "Thank You", "open_palm": "Yes"}

tab1, tab2 = st.tabs(["Sign to Voice", "Voice to Hindi"])

with tab1:
    st.header("Sign se Hindi")
    img = st.camera_input("Camera on karke sign dikhao")
    if img and st.button("Translate Sign"):
        sign = "hand_up" 
        text = SIGN_DICT.get(sign, "Not Recognized")
        prompt = f"Make a polite Hindi sentence from this sign language word: {text}"
        response = model.generate_content(prompt)
        st.success(response.text)

with tab2:
    st.header("Voice se Hindi")
    text_input = st.text_input("English me likho")
    if st.button("Translate") and text_input:
        prompt = f"Translate this to Hindi: {text_input}"
        response = model.generate_content(prompt)
        st.success(response.text)
