import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_FILE = "data/mood_log.csv"

def log_mood(mood: int):
    if not os.path.exists("data"):
        os.makedirs("data")
    df = pd.DataFrame([[datetime.now(), mood]], columns=["Date", "Mood"])
    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)

def plot_mood():
    if not os.path.exists(DATA_FILE):
        print("No mood data available.")
        return
    df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="Date", y="Mood", data=df, marker="o")
    plt.title("Mood Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()