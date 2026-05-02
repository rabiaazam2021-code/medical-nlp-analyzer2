import streamlit as st
import pandas as pd
import sys
import os

# Hassan ke src folder ko path mein add karna
sys.path.append(os.path.abspath('src'))

# Backend functions ko import karna
try:
    from predict import predict_sentiment 
    # Agar Hassan ne NER ka function bhi banaya hai toh yahan add karein
except ImportError:
    st.error("Error: 'src/predict.py' not found or function missing.")

# --- Page Configuration ---
st.set_page_config(page_title="Medical NLP Analyzer", page_icon="💊", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.image("https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d47353039331e16a92ad.svg", width=50)
    st.title("Project Info")
    st.info("""
    **Dataset:** UCI Drug Review  
    **Task:** Sentiment Analysis & NER  
    **Collaboration:** Hassan Ali & Rabia Azam
    """)
    st.markdown("---")
    st.write("v1.0.0 | Built with Streamlit")

# --- Main UI ---
st.title("💊 Medical NLP Analyzer")
st.markdown("Analyze patient reviews and extract meaningful medical insights instantly.")

# Input Section
st.subheader("Enter Patient Review")
user_input = st.text_area(
    "Patient Feedback", 
    placeholder="e.g., 'The medication was effective but I experienced some nausea...'", 
    height=150
)

# Analysis Logic
if st.button("Run Analysis"):
    if user_input:
        col1, col2 = st.columns(2)
        
        with st.spinner('Analyzing text...'):
            # 1. Sentiment Analysis
            try:
                sentiment_result = predict_sentiment(user_input)
                
                with col1:
                    st.markdown("### 📊 Sentiment Result")
                    if "positive" in sentiment_result.lower():
                        st.success(f"Result: {sentiment_result}")
                    elif "negative" in sentiment_result.lower():
                        st.error(f"Result: {sentiment_result}")
                    else:
                        st.warning(f"Result: {sentiment_result}")
            except Exception as e:
                st.error(f"Sentiment Analysis Error: {e}")

            with col2:
                st.markdown("### 🔍 Extracted Entities")
                # NER Model display
                st.info("NER Model processing drugs and conditions...")
                # st.write(extract_entities(user_input)) # Uncomment karein agar function available ho
                
        st.divider()
        st.balloons()
    else:
        st.warning("Please enter some text to analyze!")

# --- Footer ---
st.markdown("<br><hr><center>Developed with ❤️ by Rabia & Hassan</center>", unsafe_allow_html=True)