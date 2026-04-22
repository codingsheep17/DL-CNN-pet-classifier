import streamlit as st
from model_logic import process_and_predict # <--- IMPORTING YOUR MODULE
st.set_page_config(page_title="Pet Classifier", page_icon="🐾")
st.title("🐱 vs 🐶 AI Classifier")
st.write("Modular Deployment Example")

#create the File Uploader
uploaded_file = st.file_uploader("Upload an image of a cat or dog...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    #Display the image
    st.image(uploaded_file, caption="Target Image", use_container_width=True)
    with st.spinner('AI is thinking...'):
        #Use MODULAR logic to get the result
        label, score = process_and_predict(uploaded_file)
        
    #Show the result with some style
    if label == "DOG":
        st.success(f"Result: {label} (Confidence: {score:.2%})")
    else:
        st.info(f"Result: {label} (Confidence: {score:.2%})")