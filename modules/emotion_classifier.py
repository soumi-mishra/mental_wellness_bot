import joblib
from pathlib import Path

MODELS_DIR = Path(__file__).resolve().parents[1] / "models"
MODEL_PATH = MODELS_DIR / "emotion_model.pkl"

class EmotionClassifier:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, text: str) -> str:
        return self.model.predict([text])[0]

_classifier = None
def predict_emotion(text: str) -> str:
    global _classifier
    if _classifier is None:
        _classifier = EmotionClassifier()
    return _classifier.predict(text)