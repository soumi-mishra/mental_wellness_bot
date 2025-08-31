import joblib
from pathlib import Path
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "health_model.pkl"

class HealthPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, df: pd.DataFrame):
        # df must be preprocessed same way as training
        df_encoded = pd.get_dummies(df)
        return self.model.predict(df_encoded)

_predictor = None
def predict_health(df: pd.DataFrame):
    global _predictor
    if _predictor is None:
        _predictor = HealthPredictor()
    return _predictor.predict(df)