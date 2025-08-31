import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Path to your CSV
TRAIN_CSV = "datasets/train.csv"   # change path if needed

def load_csv(path):
    # Load with ; as separator
    df = pd.read_csv(path, sep=";", encoding="utf-8")

    print("Raw CSV shape:", df.shape)
    print("Columns:", df.columns)
    print("First 5 rows:\n", df.head())

    # Ensure only needed columns
    df = df[["sentence", "emotion"]]

    # Drop missing rows
    df = df.dropna()

    print(f"\nFinal dataset shape: {df.shape}")
    return df

# Load dataset
train_df = load_csv(TRAIN_CSV)

# Split X and y
X = train_df["sentence"]
y = train_df["emotion"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Vectorizer
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

# Fit transform on training set, transform test set
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print(f"\nVectorized training shape: {X_train_vec.shape}")

# Train model
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_vec, y_train)

# Evaluate
y_pred = clf.predict(X_test_vec)
print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model + vectorizer
joblib.dump(clf, "models1/emotion_model.pkl")
joblib.dump(vectorizer, "models1/vectorizer.pkl")

print("\n✅ Training complete! Model and vectorizer saved.")