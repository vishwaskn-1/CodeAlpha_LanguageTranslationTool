import streamlit as st
from googletrans import Translator
import pyttsx3
import pyperclip

# Set Streamlit page config
st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌐 Language Translation Tool")

# Supported languages (Google Translate codes)
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
    "Kannada": "kn"
}

# Input Section
text_input = st.text_area("Enter text to translate:")

src_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

# Translate Button
if st.button("Translate"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translator = Translator()
            translated = translator.translate(
                text_input, src=languages[src_lang], dest=languages[target_lang]
            )
            st.subheader("📝 Translated Text:")
            st.success(translated.text)

            # Copy Button
            if st.button("📋 Copy to Clipboard"):
                pyperclip.copy(translated.text)
                st.info("Copied successfully!")

            # Speak Button
            if st.button("🔊 Speak Text"):
                engine = pyttsx3.init()
                engine.say(translated.text)
                engine.runAndWait()

        except Exception as e:
            st.error(f"❌ Error: {e}")
