import streamlit as st
import time
import requests
from groq import Groq
from streamlit_mic_recorder import mic_recorder
import streamlit.components.v1 as components

st.set_page_config(page_title="Bastien_IA Ultra v1.0", page_icon="🔮", layout="centered")

GROQ_API_KEY = "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"
CODE_SECRET_CONSOLE = "Filtres0IA332303Ok"
CODE_CONNEXION_BASTIEN = "BastAI2303Ok"

HF_VOICE_API_URL = "https://huggingface.co"
HF_HEADERS = {"Authorization": "Bearer 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"}

def generer_voix_ia_hd(texte):
    try:
        payload = {"inputs": texte, "parameters": {"lang": "fr"}}
        response = requests.post(HF_VOICE_API_URL, headers=HF_HEADERS, json=payload)
        if response.status_code == 200: return response.content
    except: pass
    return None
  
