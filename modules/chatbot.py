import aiml
import os

class WellnessBot:
    def __init__(self, aiml_path="aiml_files/", brain_file="bot_brain.brn"):
        self.kernel = aiml.Kernel()
        if os.path.exists(brain_file):
            self.kernel.bootstrap(brainFile=brain_file)
        else:
            self.kernel.bootstrap(learnFiles=os.path.join(aiml_path, "wellness.aiml"))
            self.kernel.saveBrain(brain_file)

    def get_response(self, user_input):
        return self.kernel.respond(user_input.upper())