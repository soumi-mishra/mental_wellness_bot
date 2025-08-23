import pandas as pd
from datetime import datetime
import os

DATA_FILE = "data/journal_entries.csv"

def write_journal(entry: str):
    if not os.path.exists("data"):
        os.makedirs("data")
    df = pd.DataFrame([[datetime.now(), entry]], columns=["Date", "Entry"])
    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)

def read_journals(n=5):
    if not os.path.exists(DATA_FILE):
        print("No journal entries.")
        return
    df = pd.read_csv(DATA_FILE)
    print(df.tail(n))