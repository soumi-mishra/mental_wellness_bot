import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "datasets" / "mental_health_survey.csv"
MODEL_PATH = BASE_DIR / "models1" / "health_model.pkl"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Simple preprocessing: use 'treatment' as target
target = 'treatment'
# select numeric and categorical features
features = df.drop(columns=[target])
features = pd.get_dummies(features, drop_first=True)
labels = LabelEncoder().fit_transform(df[target])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# Evaluate
pred = clf.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

# Save model
joblib.dump(clf, MODEL_PATH)
print(f"✅ Model saved at {MODEL_PATH}")