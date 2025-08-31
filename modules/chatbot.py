import aiml
import os
import joblib   # ✅ use joblib, not pickle

class WellnessBot:
    def __init__(self, aiml_path="aiml_files/", brain_file="bot_brain.brn"):
        self.kernel = aiml.Kernel()

        # 🔄 Always rebuild brain (ignore old .brn file)
        print("Loading AIML files...")
        self.kernel.bootstrap(learnFiles=os.path.join(aiml_path, "wellness.aiml"))
        self.kernel.saveBrain(brain_file)
        print("Brain rebuilt and saved!")

        # Load ML emotion model + vectorizer (with joblib)
        model_path = os.path.join("models1", "emotion_model.pkl")
        vectorizer_path = os.path.join("models1", "vectorizer.pkl")

        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def get_response(self, user_input):
        # AIML first
        aiml_response = self.kernel.respond(user_input.upper())

        if aiml_response.strip() == "" or "no match" in aiml_response.lower():
            # If AIML fails → fallback to ML model
            vec = self.vectorizer.transform([user_input])
            emotion = self.model.predict(vec)[0]
            return f"I sense you're feeling **{emotion}**. Want to talk more about it?"
        else:
            return aiml_response