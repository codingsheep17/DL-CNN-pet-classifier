# 🐾 PetPulse: Deep Learning Cat vs. Dog Classifier

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow 2.x](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)

An efficient, modular Image Classification web app that uses a **Convolutional Neural Network (CNN)** to distinguish between cats and dogs with 80%+ accuracy. Built for scalability and clean deployment.
---

## ✨ Key Features
- **Modular Architecture:** Separates AI logic (`model_logic.py`) from the UI (`app.py`) for easy maintenance.
- **Optimized Inference:** Uses the modern `.keras` format for fast model loading and memory efficiency.
- **Responsive UI:** A clean, user-friendly interface built with Streamlit.
- **Production Ready:** Fully compatible with GitHub and Streamlit Community Cloud.
---

## 🛠️ Tech Stack
- **Engine:** TensorFlow 2.x / Keras
- **Frontend:** Streamlit
- **Data Processing:** NumPy, Pillow (PIL)
- **Model Format:** `.keras` (Deep Learning Standard)
---

## 📂 Project Structure
├── app.py                # Streamlit Web Interface
├── model_logic.py        # AI Inference Module (Modular Logic)
├── requirements.txt      # Dependencies for Deployment
└── model/
    └── cat_dog_classifier.keras  # Pre-trained CNN Weights
---

💻 Local Installation
Clone the repository:
git clone https://github.com/codingsheep17/DL-CNN-pet-classifier.git
---
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py
☁️ Deployment to Streamlit Cloud
Push your code to a Public GitHub Repository.
Visit Streamlit Cloud.
Connect your GitHub account and select this repository.
Set the "Main file path" to app.py.
Click Deploy!
🧠 Model Training Details
---
The model was trained using a CNN architecture with the following parameters:
Optimizer: Adam
Loss Function: Binary Cross-Entropy
Input Size: 150x150 pixels
Training Samples: 2,000 images
Epochs: 15
