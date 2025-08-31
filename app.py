import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from modules.chatbot import WellnessBot
from modules.mood_tracker import log_mood, plot_mood
from modules.journal import write_journal, read_journals
from modules.sentiment import analyze_sentiment
from modules.emotion_classifier import predict_emotion
from modules.health_predictor import predict_health

st.set_page_config(page_title="🌿 Mental Wellness Companion", layout="wide")
st.title("🌿 Mental Wellness Companion")

bot = WellnessBot()

# Sidebar menu
menu = st.sidebar.radio("Navigate", ["Chatbot", "Mood Tracker", "Journaling", "Self Assessment"])

# --- Chatbot ---
if menu == "Chatbot":
    st.header("🤖 Chat with WellnessBot")
    user_input = st.text_input("Type your message:")
    if st.button("Send"):
        response = bot.get_response(user_input)
        st.success(response)

# --- Mood Tracker ---
elif menu == "Mood Tracker":
    st.header("📊 Track Your Mood")
    mood_value = st.slider("How are you feeling? (1 = very bad, 10 = great)", 1, 10, 5)
    if st.button("Log Mood"):
        log_mood(mood_value)
        st.success(f"Mood {mood_value} saved ✅")

    if st.button("Show Mood Trend"):
        if not pd.io.common.file_exists("data/mood_log.csv"):
            st.warning("No mood data yet.")
        else:
            df = pd.read_csv("data/mood_log.csv", parse_dates=["Date"])
            sns.set(style="whitegrid")
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.lineplot(x="Date", y="Mood", data=df, marker="o", ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

# --- Journaling ---
elif menu == "Journaling":
    st.header("📓 Daily Journal")
    entry = st.text_area("Write your thoughts here...")
    if st.button("Save Entry"):
        write_journal(entry)
        sentiment = analyze_sentiment(entry)
        emotion = predict_emotion(entry)
        st.success(f"Saved! 🧠 Sentiment: {sentiment}, Emotion: {emotion}")

    if st.button("Show Last Entries"):
        if not pd.io.common.file_exists("data/journal_entries.csv"):
            st.warning("No journal entries yet.")
        else:
            df = pd.read_csv("data/journal_entries.csv")
            st.write(df.tail(5))

# --- Self Assessment ---
elif menu == "Self Assessment":
    st.header("🧾 Mental Health Self Assessment")
    age = st.number_input("Age", 10, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    work_stress = st.slider("Work Stress (1=Low, 10=High)", 1, 10, 5)

    if st.button("Predict Risk"):
        # Encode gender into numbers
        gender_map = {"Male": 0, "Female": 1, "Other": 2}
        gender_encoded = gender_map[gender]

        df = pd.DataFrame([{
            "Age": age,
            "Gender": gender_encoded,
            "Work_Stress": work_stress
        }])

        result = predict_health(df)
        st.success(f"🩺 Prediction: {result[0]}")