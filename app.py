import streamlit as st
from datetime import time

st.set_page_config(page_title="Insomnia Predictor", layout="centered")

st.markdown("""
<style>
            
/* Hide Streamlit header (main cause of white gap) */
header {
    visibility: hidden;
    height: 0px;
}

/* ----------- BASE BACKGROUND ----------- */
.stApp {
    background: linear-gradient(to bottom, #0b132b, #1c2541, #3a506b);
    color: white;
}

/* ----------- STARS LAYER ----------- */
.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background-image: radial-gradient(white 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.3;
    top: -50%;
    left: -50%;
    animation: twinkle 8s linear infinite;
    z-index: -1;
}

/* ----------- TWINKLE ANIMATION ----------- */
@keyframes twinkle {
    0%   { transform: translate(0, 0); opacity: 0.2; }
    25%  { transform: translate(-20px, -20px); opacity: 0.4; }
    50%  { transform: translate(-40px, 10px); opacity: 0.2; }
    75%  { transform: translate(20px, -10px); opacity: 0.35; }
    100% { transform: translate(0, 0); opacity: 0.2; }
}

/* ----------- STAR OVERLAY ----------- */
.stApp::before {
    
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background-image: radial-gradient(white 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0.25;
    top: 0;
    left: 0;
    z-index: -1;
}

/* ----------- TEXT ----------- */
h1, h2, h3, h4, h5, h6, p, label {
    color: #ffffff !important;
}

/* ----------- INPUT FIELDS ----------- */
.stTextInput input, 
.stTimeInput input,
 {
    color: white !important;
    border-radius: 10px !important; 
}
/* Target actual input inside number_input */
    div[data-testid="stNumberInput"] input {
    background-color: rgba(255, 255, 255, 0.15) !important;
    color: black !important;
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 8px !important;
}
            

/* Placeholder text (if any) */
div[data-testid="stNumberInput"] input::placeholder {
    color: rgba(255, 255, 255, 0.6) !important;
}

/* Focus state */
div[data-testid="stNumberInput"] input:focus {
    border: 1px solid #00c6ff !important;
    box-shadow: 0 0 6px #00c6ff;
    outline: none;
}

/* Step buttons (+ / -) */
div[data-testid="stNumberInput"] button {
    background-color: rgba(255, 255, 255, 0.2) !important;
    color: white !important;
}
            

/* Selected value (inside box) */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    color: black !important;
}

/* Dropdown options text */
div[data-testid="stSelectbox"] ul {
    color: black !important;
}

/* Dropdown menu background (optional for clarity) */
div[data-testid="stSelectbox"] ul {
    background-color: white !important;
}
            
/* Make label text clearly visible */
div[data-testid="stRadio"] label {
    color: white !important;
    font-size: 16px;
}

/* Make selected radio circle blue */
div[data-testid="stRadio"] input[type="radio"] {
    accent-color: #007BFF;  /* blue */
}

/* ----------- SLIDER ----------- */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #00c6ff, #0072ff) !important;
}

/* ----------- BUTTON ----------- */
.stButton button {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

/* ----------- SUCCESS / ERROR ----------- */
.stSuccess {
    background-color: rgba(0, 255, 100, 0.15) !important;
    color: #00ff88 !important;
    border-radius: 10px;
}

.stError {
    background-color: rgba(255, 0, 80, 0.15) !important;
    color: #ff4b5c !important;
    border-radius: 10px;
}

.stWarning {
    background-color: rgba(255, 200, 0, 0.15) !important;
    color: #ffcc00 !important;
    border-radius: 10px;
}

/* ----------- INFO BOX ----------- */
.stInfo {
    background-color: rgba(0, 150, 255, 0.15) !important;
    color: #4db8ff !important;
    border-radius: 10px;
}



/* ----------- REMOVE WHITE BOX ----------- */
.block-container {
    padding-top: 2rem;
}

/* ----------- SMOOTH UI ----------- */
* {
    transition: all 0.2s ease-in-out;
}

</style>
""", unsafe_allow_html=True)

import pickle
d1 = {"female":1 , "male":2}
d2 = {"Entertainment":1 , "Educational/Entertainment": 4, "Educational":2, "Motivational":1, "Emotional/Drama":5, "Mixed": 3}

final_model = pickle.load(open('insomnia_model.pkl', 'rb'))
st.title("🛌 Insomnia Risk Prediction")
st.write("Fill in your details below to check your risk of insomnia.")

st.markdown("### 👤 Personal Information")
age = st.number_input("What is your age?",min_value=13,max_value=100,value=25,step=1)

gender = st.radio("Select your gender", ["male", "female"])
content_type_primary = content_type_primary = st.selectbox("What type of content did you mostly consume yesterday?",
    ["Motivational", "Entertainment", "Educational", "Educational/Entertainment",  "Emotional/Drama", "Mixed"])

st.markdown("### 📱 Yesterday's Screen Usage")
usage_time_10_2 = st.time_input( "How long did you use your phone between 10 PM and 2 AM?",value=time(0, 0))
usage_time_10_2 = usage_time_10_2.hour * 60 + usage_time_10_2.minute

max_continuous_usage = st.time_input("What is your longest continuous screen usage from 10:00PM - 2:00AM? ",value=time(0, 0))
max_continuous_usage = max_continuous_usage.hour * 60 + max_continuous_usage.minute

reels_usage_time = st.time_input("How much time you spent watching short videos (Reels/Shorts)?",value=time(0, 0))
reels_usage_time = reels_usage_time.hour * 60 + reels_usage_time.minute

st.markdown("### 🧠Yesterday's Mental State")
daily_stress_level = st.slider("How stressful was your day yesterday? (1 = Very Low, 5 = Very High)",
    min_value=1,max_value=5,value=3)

overthinking_at_night = st.slider("How much did you overthink last night before sleeping? (1 =Very Less, 5 = Very Much)",
    min_value=1,max_value=5,value=3)

sleep_quality = st.slider("How would you rate your sleep quality last night?(1 = Poor, 5 = Excellent)",
    min_value=1,max_value=5,value=3)

sleep_latency = st.time_input("How long did it take you to fall asleep last night?  ",value=time(0, 0))
sleep_latency = sleep_latency.hour * 60 + sleep_latency.minute

night_awakenings = st.number_input(
    "How many times did you wake up during the night?",min_value= 0,max_value=100,step=1)


sleep_time = st.time_input("What time did you go to sleep last night?",value=time(0, 0))
wake_up_time = st.time_input("What time did you wake up today?",value=time(0, 0))

# sleep_duration 
sleep_duration = 0
sleep_minutes = sleep_time.hour * 60 + sleep_time.minute
wake_minutes = wake_up_time.hour * 60 + wake_up_time.minute
if wake_minutes >= sleep_minutes:
    sleep_duration = wake_minutes - sleep_minutes
else:
    sleep_duration = (24 * 60 - sleep_minutes) + wake_minutes


if st.button('🔍 Predict Insomnia Risk'):
    gender = d1[gender]
    content_type_primary = d2[content_type_primary]
    
    test = [[age, gender, content_type_primary, usage_time_10_2, max_continuous_usage, reels_usage_time, daily_stress_level, overthinking_at_night, sleep_latency,
    night_awakenings, sleep_quality, sleep_duration]]
    result = final_model.predict(test)
    if result == 1:
        st.error("⚠️ There are signs indicating a higher risk of insomnia.")
    else:
        st.success("✅ Your inputs do not indicate a significant risk of insomnia.")
        

