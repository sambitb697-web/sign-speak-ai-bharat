import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Sign Speak AI Bharat", page_icon="🤟")

st.title("🤟 Sign Speak AI Bharat")
st.markdown("Indian Sign Language ko Text me badlo")

# KEY KO SECRETS SE LO
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except:
    st.error("API Key nahi mili! Settings > Secrets me GOOGLE_API_KEY daalo")
    st.stop()

uploaded_file = st.camera_input("Photo lo ya upload karo")

if uploaded_file and st.button("Translate Sign"):
    image = Image.open(uploaded_file)
    st.image(image)
    
    with st.spinner("Translate ho raha hai..."):
        prompt = "You are an expert in Indian Sign Language. Identify this hand gesture and reply with only 1 word in English and 1 word in Hindi."
        response = model.generate_content([prompt, image])
        st.success(f"Result: {response.text}")
