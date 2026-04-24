# Insomnia Detection System

## 📌 Overview
The **Insomnia Detection System** is a machine learning-based web application that predicts the risk of insomnia based on user lifestyle, screen usage, and mental health factors.

Built using **Streamlit**, this app provides an interactive interface where users can input their daily habits and receive instant predictions.

---

## 🚀 Features
- 🎯 Predicts insomnia risk using a trained ML model  
- 📊 Considers multiple lifestyle and sleep factors  
- ⚡ Real-time prediction results  
- 📱 Simple and user-friendly interface  

---

## 🧠 How It Works
1. User enters personal, behavioral, and sleep-related data  
2. Inputs are preprocessed 
3. Preprocessed data is passed to the trained machine learning model  
4. The model predicts:
   - ✅ Low Insomnia Risk  
   - ⚠️ High Insomnia Risk  

---

## 📊 Input Parameters

### 👤 Personal Information
- Age  
- Gender  
- Content consumption type  

### 📱 Screen Usage
- Usage between **10 PM – 2 AM**  
- Longest continuous usage  
- Short video (Reels/Shorts) time  

### 🧠 Mental State
- Daily stress level (1–5)  
- Overthinking level (1–5)  

### 😴 Sleep Data
- Sleep latency  
- Night awakenings  
- Sleep quality  
- Sleep duration  

---

## 🛠️ Tech Stack
- **Python** – Backend  
- **Streamlit** – UI Framework  
- **Scikit-learn** – Machine Learning  
- **Pickle** – Model loading  
- **CSS** – Custom styling  

---


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
- git clone https://github.com/your-username/insomnia-detection.git
- cd insomnia-detection
### Install Dependencies
- pip install streamlit scikit-learn
### Run the Application
- streamlit run app.py

